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
