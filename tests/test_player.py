import unittest
from unittest.mock import patch
import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from player import Player
from skills import AVAILABLE_SKILLS
from enemy import Enemy

class TestPlayer(unittest.TestCase):

    def setUp(self):
        """Set up a new Player instance before each test."""
        # Patch notifications directly on the modules where they are defined and used
        # This avoids needing the mock objects passed to every test method if not used explicitly
        self.patcher_player_notification = patch('player.show_notification', autospec=True)
        self.patcher_enemy_print = patch('enemy.print', autospec=True) # Assuming enemy.py uses print for combat logs

        self.mock_player_show_notification = self.patcher_player_notification.start()
        self.mock_enemy_print = self.patcher_enemy_print.start()

        self.player = Player(name="TestHero")

    def tearDown(self):
        """Stop the patchers after each test."""
        self.patcher_player_notification.stop()
        self.patcher_enemy_print.stop()

    def test_player_creation(self):
        """Test basic Player attributes upon creation."""
        # Player is created in setUp, here we assert its initial state
        self.assertEqual(self.player.name, "TestHero")
        self.assertEqual(self.player.level, 1)
        self.assertEqual(self.player.experience, 0)
        self.assertEqual(self.player.stats["Strength"], 10)
        self.assertEqual(self.player.hp, 100) # Stamina (10) * 10
        self.assertEqual(self.player.mp, 100) # Intelligence (10) * 10
        self.assertEqual(len(self.player.skills), 0)
        self.assertEqual(self.player.stat_points_to_allocate, 0)
        self.assertEqual(self.player.experience_to_next_level, 100) # Level 1 * 100

    def test_increase_stat(self):
        """Test the increase_stat method."""
        initial_strength = self.player.stats["Strength"]
        self.player.increase_stat("Strength", 5)
        self.assertEqual(self.player.stats["Strength"], initial_strength + 5)
        self.mock_player_show_notification.assert_any_call(f"Strength increased by 5. New value: {initial_strength + 5}", self.player.name)

        initial_stamina = self.player.stats["Stamina"]
        self.player.increase_stat("Stamina", 2)
        self.assertEqual(self.player.stats["Stamina"], initial_stamina + 2)
        self.assertEqual(self.player.hp, (initial_stamina + 2) * 10)

        self.assertFalse(self.player.increase_stat("NonExistentStat", 5))
        self.mock_player_show_notification.assert_called_with("Error: Invalid stat name 'NonExistentStat'.", self.player.name)

    def test_gain_experience_and_level_up(self):
        """Test gaining experience and leveling up."""
        self.player.gain_experience(50)
        self.assertEqual(self.player.experience, 50)
        self.assertEqual(self.player.level, 1)
        self.mock_player_show_notification.assert_any_call(f"Gained 50 XP. Total XP: 50/100", self.player.name)

        self.player.gain_experience(50) # Total 100 XP
        self.assertEqual(self.player.level, 2)
        self.assertEqual(self.player.experience, 0)
        self.assertEqual(self.player.stat_points_to_allocate, 5)
        self.assertEqual(self.player.experience_to_next_level, 200)
        self.mock_player_show_notification.assert_any_call(f"LEVEL UP! You have reached Level 2!", self.player.name)
        self.mock_player_show_notification.assert_any_call(f"You have 5 stat points to allocate.", self.player.name)

    def test_level_up_multiple_times(self):
        """Test gaining enough experience for multiple level ups."""
        self.player.gain_experience(350) # L1->L2 (100), L2->L3 (200) = 300 total. 50 into L3
        self.assertEqual(self.player.level, 3)
        self.assertEqual(self.player.experience, 50)
        self.assertEqual(self.player.stat_points_to_allocate, 10) # 5 for L2, 5 for L3
        self.assertEqual(self.player.experience_to_next_level, 300) # For L3->L4

    def test_skill_acquisition_on_level_up(self):
        """Test that skills are acquired when leveling up."""
        heal_skill_name = "Minor Heal"
        stealth_skill_name = "Stealth"

        self.player.gain_experience(300) # Level to 3
        self.assertEqual(self.player.level, 3)
        self.assertTrue(any(skill['name'] == heal_skill_name for skill in self.player.skills))
        self.mock_player_show_notification.assert_any_call(f"New Skill Unlocked: {heal_skill_name}!", self.player.name)

        self.player.gain_experience(700) # Level to 5 (L3->L4 needs 300, L4->L5 needs 400)
        self.assertEqual(self.player.level, 5, f"Player level should be 5, but is {self.player.level}")
        self.assertTrue(any(skill['name'] == stealth_skill_name for skill in self.player.skills))
        self.mock_player_show_notification.assert_any_call(f"New Skill Unlocked: {stealth_skill_name}!", self.player.name)

        expected_skill_count = sum(1 for sk in AVAILABLE_SKILLS if self.player.level >= sk["level_requirement"])
        self.assertEqual(len(self.player.skills), expected_skill_count)

    def test_defeat_enemy_grants_experience(self):
        """Test that defeating an enemy grants experience."""
        enemy_xp = 50
        test_enemy = Enemy(name="TestDummy", stats={"hp": 10, "attack":1}, experience_reward=enemy_xp)

        initial_player_xp = self.player.experience
        self.player.hp = 1000 # Ensure player survives any hypothetical damage

        # Simulate attack and defeat
        while test_enemy.is_alive():
             self.player.attack_enemy(test_enemy)

        # Defeat_enemy is called by attack_enemy when enemy HP <= 0
        # It then calls gain_experience
        self.assertEqual(self.player.experience, initial_player_xp + enemy_xp)
        self.mock_player_show_notification.assert_any_call(f"You have defeated {test_enemy.name}!", self.player.name)
        # The gain_experience call will also trigger a notification
        self.mock_player_show_notification.assert_any_call(f"Gained {enemy_xp} XP. Total XP: {initial_player_xp + enemy_xp}/{self.player.experience_to_next_level}", self.player.name)

if __name__ == '__main__':
    unittest.main()
