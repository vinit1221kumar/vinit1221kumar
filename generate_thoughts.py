#!/usr/bin/env python3
"""
Daily Thought Generator
Generates 2 unique, reflective thoughts for the day.
"""

import json
import os
from datetime import datetime
import random

# Thought templates to ensure originality
THOUGHT_SEEDS = [
    "The greatest discoveries often come from the intersection of curiosity and persistence.",
    "Success is not a destination; it's the accumulation of meaningful decisions made daily.",
    "Every problem contains the seed of an equal or greater opportunity.",
    "Growth happens when we choose to embrace challenge over comfort.",
    "The only way to do great work is to care deeply about what you do.",
    "Innovation thrives at the boundary between what is known and what is possible.",
    "True learning requires us to unlearn what we thought we knew.",
    "The smallest actions, repeated consistently, create the greatest transformations.",
    "Mastery is not about perfection; it's about the relentless pursuit of improvement.",
    "Purpose is found not in what we seek, but in what we become in the seeking.",
    "The obstacles we face are the raw material for our greatest achievements.",
    "Clarity of vision emerges from honest reflection, not from endless planning.",
    "Real progress is measured by the depth of understanding, not the speed of execution.",
    "Failure is not the opposite of success—it's a prerequisite for it.",
    "The power to change begins with the courage to see things differently.",
    "Wisdom is knowing which battles to fight and which to let go.",
    "Every moment is a choice to move closer to or further from your potential.",
    "Connection with others amplifies what we can achieve alone.",
    "The future belongs to those who build instead of merely observe.",
    "Excellence is a journey of incremental improvements woven together with intent.",
    "Patience and persistence are the foundation upon which lasting achievements are built.",
    "The questions we ask shape the answers we discover and the paths we take.",
    "Creativity flourishes when we give ourselves permission to explore without judgment.",
    "Meaningful impact comes from consistent effort applied over time, not from sudden bursts.",
    "The willingness to be vulnerable is the gateway to authentic growth.",
    "Systems and habits free our minds to focus on what truly matters.",
    "Empathy is the bridge that transforms ideas into solutions that serve others.",
    "The quality of our attention determines the quality of our work and relationships.",
    "Adversity reveals our character and refines our capabilities in ways comfort never could.",
    "True confidence comes from accepting both our strengths and our limitations.",
    "The stories we tell ourselves shape the reality we create.",
    "Learning to say no protects the space needed to say yes to what truly matters.",
    "Progress is not linear; every setback carries lessons that propel us forward.",
    "The discipline to start is important, but the discipline to finish is transformative.",
    "Collaboration multiplies possibilities that individual effort alone cannot reach.",
    "Reflection is not a luxury; it's the compass that keeps us moving in the right direction.",
    "The best time to plant a tree was yesterday; the second best time is now.",
    "Complexity is often the enemy of execution; simplicity creates momentum.",
    "Our greatest limitations often exist only in the boundaries of our imagination.",
    "The courage to experiment is what turns theory into practice and dreams into reality.",
]


def generate_thoughts(count=2):
    """Generate unique thoughts for the day."""
    selected = random.sample(THOUGHT_SEEDS, min(count, len(THOUGHT_SEEDS)))
    return selected


def save_thoughts(thoughts):
    """Save thoughts with today's date to a temporary JSON file."""
    today = datetime.now().strftime("%Y-%m-%d")
    thoughts_data = {
        "date": today,
        "thoughts": thoughts,
        "generated_at": datetime.now().isoformat()
    }
    
    # Save to a temporary file that update_readme.py will read
    with open("thoughts_temp.json", "w") as f:
        json.dump(thoughts_data, f, indent=2)
    
    return thoughts_data


def main():
    """Generate and save daily thoughts."""
    thoughts = generate_thoughts()
    data = save_thoughts(thoughts)
    
    print(f"Generated thoughts for {data['date']}:")
    for i, thought in enumerate(thoughts, 1):
        print(f"{i}. {thought}")


if __name__ == "__main__":
    main()
