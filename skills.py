AVAILABLE_SKILLS = [
    {
        "name": "Stealth",
        "description": "Temporarily become invisible.",
        "level_requirement": 5,
        "type": "Active",
        "effects": {"status": "invisible", "duration": 10}
    },
    {
        "name": "Berserk Mode",
        "description": "Increases Strength by 50% for 30 seconds.",
        "level_requirement": 10,
        "type": "Buff",
        "effects": {"stat_buff": {"Strength": 1.5}, "duration": 30}
    },
    {
        "name": "Minor Heal",
        "description": "Heals a small amount of HP.",
        "level_requirement": 3,
        "type": "Active",
        "effects": {"heal_amount": 25} # Heal 25 HP
    }
]
