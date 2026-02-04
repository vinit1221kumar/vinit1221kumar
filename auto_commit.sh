#!/bin/bash
# Auto Commit Script
# Orchestrates daily thought generation and GitHub commits
# Safe to run via cron

set -e  # Exit on error

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Colors for output (optional, but helpful)
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Daily Thought Automation Started ===${NC}"

# Step 1: Generate thoughts
echo -e "${BLUE}Step 1: Generating thoughts...${NC}"
python3 generate_thoughts.py
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Failed to generate thoughts${NC}"
    exit 1
fi

# Step 2: Update README
echo -e "${BLUE}Step 2: Updating README.md...${NC}"
python3 update_readme.py
if [ $? -ne 0 ]; then
    echo -e "${RED}Error: Failed to update README${NC}"
    exit 1
fi

# Step 3: First commit - Update content
echo -e "${BLUE}Step 3: Creating first commit (content update)...${NC}"
git add README.md
git commit -m "docs: update daily thoughts" || true  # Allow failure if nothing changed

# Step 4: Clean up temporary file
rm -f thoughts_temp.json

# Step 5: Second commit - Metadata reflection
echo -e "${BLUE}Step 4: Creating second commit (metadata)...${NC}"
git add -A
CURRENT_DATE=$(date '+%Y-%m-%d')
git commit -m "chore: daily automation run for $CURRENT_DATE" || true  # Allow failure if nothing changed

# Step 6: Push to main branch
echo -e "${BLUE}Step 5: Pushing changes to main...${NC}"
git push origin main || {
    echo -e "${RED}Warning: Push failed, but local commits were created${NC}"
    exit 1
}

echo -e "${GREEN}=== Daily Thought Automation Completed Successfully ===${NC}"
echo -e "${GREEN}✓ 2 thoughts generated${NC}"
echo -e "${GREEN}✓ README updated${NC}"
echo -e "${GREEN}✓ Changes pushed to GitHub${NC}"

exit 0
