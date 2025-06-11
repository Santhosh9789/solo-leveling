class Enemy:
    def __init__(self, name, stats, experience_reward, loot_drops=None):
        self.name = name
        self.stats = stats
        # Make a copy of hp to current_hp to allow for taking damage
        self.current_hp = stats.get("hp", 0)
        self.experience_reward = experience_reward
        self.loot_drops = loot_drops if loot_drops else []

    def is_alive(self):
        return self.current_hp > 0

    # Basic take_damage method for future combat system
    def take_damage(self, damage_amount):
        self.current_hp -= damage_amount
        if self.current_hp < 0:
            self.current_hp = 0
        print(f"{self.name} took {damage_amount} damage. Current HP: {self.current_hp}") # Using print for now
        if not self.is_alive():
            print(f"{self.name} has been defeated.") # Using print for now

# Example of creating an enemy instance (for testing, can be removed)
# goblin = Enemy("Goblin", {"hp": 30, "attack": 5, "defense": 2}, 10, ["goblin_ear"])
# print(f"Created {goblin.name} with {goblin.current_hp} HP, rewarding {goblin.experience_reward} XP.")
