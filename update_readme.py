#!/usr/bin/env python3
"""
README Updater
Reads generated thoughts and updates README.md with today's thoughts.
"""

import json
import os
from datetime import datetime


README_TEMPLATE = """# Daily Thoughts

An automated daily thought generation and GitHub contribution system.

Every day at a scheduled time, this repository generates exactly 2 unique, reflective thoughts and commits them to GitHub, creating a continuous chain of meaningful contributions.

---

## Today's Thoughts ({date})

{thoughts}

---

*Last updated: {timestamp}*

*This README is automatically regenerated daily with fresh thoughts.*
"""


def load_thoughts():
    """Load thoughts from the temporary JSON file."""
    if not os.path.exists("thoughts_temp.json"):
        raise FileNotFoundError("thoughts_temp.json not found. Run generate_thoughts.py first.")
    
    with open("thoughts_temp.json", "r") as f:
        data = json.load(f)
    
    return data


def format_thoughts(thoughts):
    """Format thoughts as a numbered list."""
    formatted = "\n".join([f"{i}. {thought}" for i, thought in enumerate(thoughts, 1)])
    return formatted


def update_readme(thoughts_data):
    """Update README.md with the generated thoughts."""
    date = thoughts_data["date"]
    thoughts = thoughts_data["thoughts"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    thoughts_formatted = format_thoughts(thoughts)
    
    readme_content = README_TEMPLATE.format(
        date=date,
        thoughts=thoughts_formatted,
        timestamp=timestamp
    )
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    
    return readme_content


def main():
    """Load thoughts and update README."""
    try:
        thoughts_data = load_thoughts()
        readme_content = update_readme(thoughts_data)
        
        print("✓ README.md updated successfully")
        print(f"✓ Thoughts for {thoughts_data['date']} committed")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"Error reading thoughts file: {e}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
