# Quick Start Guide

**Get up and running with the enhanced LLM D&D Adventure System in 5 minutes.**

## Prerequisites

- Python 3.8+ installed
- Basic familiarity with markdown and command line
- An LLM assistant (Claude, Gemini, etc.) with file system access

## Installation (2 minutes)

### 1. Install Python Dependencies

```bash
cd tools
pip install -r requirements.txt
```

### 2. Verify Installation

```bash
python dice_roller.py --test
python playtest_analyzer.py --help
python reference_manager.py --help
```

You should see success messages and help text.

## Your First Enhanced Adventure (3 minutes)

### Option A: Explore Existing Example

The `lulu_the_piggy_2/` folder contains a complete example with all new features:

```bash
# View the DM cheat sheet for first encounter
cat lulu_the_piggy_2/dm_materials/session_cheatsheets/01_the_first_signal.md

# View NPC cards with stats
cat lulu_the_piggy_2/dm_materials/npc_cards/01_major_npcs.md

# Analyze playtest data
python tools/playtest_analyzer.py \
  --adventure lulu_the_piggy_2 \
  --encounter The_First_Signal \
  --output lulu_the_piggy_2/play_tests/The_First_Signal/analysis_report.md
```

### Option B: Start a New Adventure

1. **Tell your LLM assistant to use the Lead Game Designer Agent:**

```
Use the Lead Game Designer Agent instructions at .claude/agents/lead_game_designer_agent/README.md
to create a new adventure called "my_adventure" about [your concept here].
```

2. **The agent will follow the 8-step creation process:**
   - Steps 1-5: Core content (tone, factions, locations, props, pictures)
   - Step 6: DM materials generation (NEW - cheat sheets, NPC cards, trackers)
   - Step 7: Content validation (NEW - verifies clues, NPCs, timelines)
   - Step 8: Reference integration (NEW - scans for creatures/spells)

3. **Run your first playtest with dice rolling:**

```
Use the Play Test DM Agent with the enhanced workflow. Use dice_roller.py
with seed 1000 to playtest the first encounter.
```

The agent will generate both narrative playtest AND structured JSON data.

## Key Features at a Glance

### For DM Preparation

- **Session Cheat Sheets** (`dm_materials/session_cheatsheets/`) - 1-page encounter references
- **NPC Cards** (`dm_materials/npc_cards/`) - Stats + roleplay guides
- **Clue Tracker** (`dm_materials/clue_tracker.md`) - Track secret discovery
- **Faction Diagram** (`dm_materials/faction_diagram.md`) - Visual relationship maps

### For Running Sessions

```bash
# Roll dice with reproducible results
python tools/dice_roller.py --roll "1d20+5" --character "Alex" \
  --action "Insight check on Ms. Reed" --seed 1000

# Track initiative
# Use templates/combat_tracker.md to track HP/initiative during combat
```

### For Playtesting Analysis

```bash
# Analyze spotlight distribution
python tools/playtest_analyzer.py \
  --adventure my_adventure \
  --encounter first_encounter \
  --output analysis.md

# Check for balance issues (characters with <15% spotlight)
python tools/playtest_analyzer.py --adventure my_adventure --detect-issues
```

### For Reference Management

```bash
# Scan adventure for creature/spell mentions
python tools/reference_manager.py --adventure my_adventure --scan

# Generate bestiary from scan results
python tools/reference_manager.py --adventure my_adventure --bestiary
```

## Templates Available

All templates are in the `templates/` folder:

- `encounter_cheatsheet.md` - Create session quick references
- `npc_card.md` - Create stat blocks with roleplay guides
- `clue_tracker.md` - Track secrets during sessions
- `combat_tracker.md` - Track initiative and HP

Simply copy a template and fill in your adventure content.

## Agent Workflow

The system uses 5 specialized agents in `.claude/agents/`:

1. **Lead Game Designer** - Creates adventures (Steps 1-8)
2. **Play Test DM** - Runs playtests with dice rolling
3. **Play Test Players** - Simulates 3 player personas
4. **Play Test Grader** - Analyzes quality + extracts metrics
5. **Reference Integration** - Manages SRD content

Each agent has detailed instructions in their README.md file.

## Next Steps

- **Read the full workflow:** [README.md](README.md) for complete adventure creation process
- **Understand the system:** [CLAUDE.md](CLAUDE.md) for architecture overview
- **See detailed improvements:** [feedback.md](feedback.md) for all v2.0 enhancements
- **Implementation status:** [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md) for what's ready vs. pending

## Common Tasks

### Create DM Materials for Existing Adventure

```bash
# 1. Ask your LLM to use Lead Game Designer Agent
# 2. Point it to existing adventure folder
# 3. Request Step 6 only (DM Materials Generation)
```

### Validate Adventure Content

```bash
# Ask LLM to use Lead Game Designer Agent
# Request Step 7 only (Content Validation)
```

### Analyze Multiple Playtests

```bash
# Run playtest_analyzer.py on each playtest
# The Grader Agent will create aggregate summaries automatically
```

## Troubleshooting

**Python encoding errors on Windows?**
- Tools are designed for file output, console display may show formatting issues
- Check generated .md and .json files directly - they will be correct

**Agent not finding templates?**
- Ensure you're running from repository root
- Templates are in `templates/` folder relative to root

**Dice roller results not reproducible?**
- Always use `--seed` parameter with same value
- Seed must be positive integer

## Support

- Report issues: https://github.com/anthropics/claude-code/issues
- Review existing examples: `lulu_the_piggy/` and `lulu_the_piggy_2/` folders
- Check agent-specific guides: `.claude/agents/*/ADDENDUM.md` and `ENHANCED_WORKFLOW.md` files
