# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is an LLM-assisted D&D adventure creation and playtesting system using a multi-agent workflow. The repository contains markdown-based adventure content, agent instructions, and playtesting records for creating immersive, faction-based tabletop RPG adventures.

## Core Workflow

The system uses five specialized LLM agents working asynchronously through the file system:

1. **Lead Game Designer Agent** ([.claude/agents/lead_game_designer_agent/README.md](.claude/agents/lead_game_designer_agent/README.md)) - Creates consolidated adventure documents
2. **Play Test DM Agent** ([.claude/agents/play_test_dm_agent/README.md](.claude/agents/play_test_dm_agent/README.md)) - Runs playtests as the Dungeon Master
3. **Play Test Players Agent** ([.claude/agents/play_test_players_agent/README.md](.claude/agents/play_test_players_agent/README.md)) - Roleplays as three distinct player personas
4. **Play Test Grader and Summarizer Agent** ([.claude/agents/play_test_grader_and_summarizer_agent/README.md](.claude/agents/play_test_grader_and_summarizer_agent/README.md)) - Analyzes playtest quality and provides feedback
5. **Reference Integration Agent** ([.claude/agents/reference_integration_agent/README.md](.claude/agents/reference_integration_agent/README.md)) - Downloads and validates D&D 2024 5e SRD content, validates custom stat blocks

Agents communicate through YAML frontmatter notes in markdown files, creating an auditable trail of feedback.

## Key Design Principles

### Mandatory Verbosity Requirements
- **Minimum 500 words** per major entity (faction, location, primary NPC)
- All descriptions must weave facts into compelling narratives
- Use at least 3 senses when describing locations
- Include "connective tissue" - each entity must reference at least one other named entity

### Multi-Stage Encounter Design
All encounters follow a 4-stage structure:
1. **Stage 1 (The Hook)** - Initial problem presentation
2. **Stage 2 (The Complication)** - Unexpected problem after initial player action
3. **Stage 3 (The Escalation)** - Stakes raised significantly
4. **Stage 4 (The Climax)** - Final resolution moment

Each encounter should provide 10-15 meaningful exchanges before climax.

### Consolidated Documentation
Create large, consolidated files instead of one file per entity:
- `01_Factions.md` - All factions, NPCs, timelines in one file
- `02_Locations.md` - All locations and encounters in one file
- `03_Props.md` - All text-based props and documents in one file

## Adventure Structure

```
/ADVENTURE_NAME/
├── 00_Tone_and_Immersion/
│   ├── atmosphere.md
│   ├── inspiration.md
│   └── jargon.md
├── 01_Factions/           # May be folder or single .md file
├── 02_Locations/          # May be folder or single .md file
├── 03_Props/              # May be folder or single .md file
├── dm_materials/          # NEW - Session execution aids
│   ├── session_cheatsheets/
│   ├── npc_cards/
│   ├── faction_diagram.md
│   ├── clue_tracker.md
│   └── combat_tracker_template.md
├── references/            # NEW - SRD and reference materials
│   ├── monsters_used.md
│   └── spells_used.md
├── pictures/
│   ├── style.md
│   ├── characters.md
│   ├── locations.md
│   ├── posters.md
│   └── misc.md
├── play_tests/
│   └── [ENCOUNTER_NAME]/
│       ├── playtest_N.md
│       ├── playtest_N_data.json  # NEW - Structured metrics
│       └── summary.md
├── sources/               # Raw source material and drafts
├── summary.md
├── adventure_checklist.md
├── secrets_and_clues.md
├── player_personas.md
└── rewards.md
```

## Adventure Creation Sequence

The Lead Game Designer follows this exact sequence with checkpoint feedback:

1. **Step 1: Tone and Immersion**
   - Draft `summary.md` with core conflict and themes
   - Create `00_Tone_and_Immersion` folder files
   - **Checkpoint:** Present to user for feedback

2. **Step 2: Factions**
   - Create complete consolidated `01_Factions.md` with all NPCs, backstories, timelines
   - **Checkpoint:** Present complete document for feedback

3. **Step 3: Locations**
   - Create complete consolidated `02_Locations.md` with all encounters
   - **Checkpoint:** Present complete document for feedback

4. **Step 4: Props**
   - Create complete consolidated `03_Props.md` with all text-based items
   - **Checkpoint:** Present complete document for feedback

5. **Step 5: Pictures**
   - Draft `style.md` and all picture prompts
   - **Checkpoint:** Present all picture files for feedback

After each step, update `adventure_checklist.md`, `secrets_and_clues.md`, `rewards.md`, and overall `summary.md`.

## Playtesting Process

Each playtest focuses on a **single encounter** and follows this structure:

### Setup
- Starting point description
- Characters present (annotate NPCs with faction)
- Clues, secrets, and props available
- Win conditions for all factions

### Execution
- Simulate dice rolls for checks
- Ensure each PC gets spotlight moments
- Continue until win condition met or conflict resolved
- Aim for narrative quality, not arbitrary round count

### Grading Criteria
- **Immersion:** Quality of descriptions and atmosphere
- **Character Spotlight:** Which characters contributed meaningfully
- **Clue/Prop Interaction:** What was discovered and used
- **Path to Victory:** Creativity required vs. straightforward combat

### Summary (After Multiple Runs)
Analyze across all playtests:
- Character spotlight frequency
- Clue/prop usage patterns
- Win condition difficulty balance

Playtests are stored in `play_tests/[ENCOUNTER_NAME]/playtest_N.md` with consolidated summaries.

## Faction-Based Design

Adventures feature 3-5 factions in active conflict with:
- Independent goals and timelines
- Proactive actions regardless of player intervention
- Internal conflicts that players can exploit

Players can engage, ignore, or manipulate factions. The world evolves dynamically.

## Python Utilities (tools/)

The system includes Python tools to enhance workflow:

1. **[dice_roller.py](tools/dice_roller.py)** - Reproducible dice rolling with statistical tracking
2. **[playtest_analyzer.py](tools/playtest_analyzer.py)** - Extract metrics, generate reports, identify balance issues
3. **[reference_manager.py](tools/reference_manager.py)** - SRD integration and validation (in development)
4. **[cheatsheet_generator.py](tools/cheatsheet_generator.py)** - Auto-generate DM materials (in development)

See [tools/README.md](tools/README.md) for complete documentation.

## Document Templates (templates/)

Ready-to-use templates for DM materials:
- **[encounter_cheatsheet.md](templates/encounter_cheatsheet.md)** - 1-page session quick reference
- **[npc_card.md](templates/npc_card.md)** - Stat blocks + roleplay guides
- **[clue_tracker.md](templates/clue_tracker.md)** - Session clue tracking
- **[combat_tracker.md](templates/combat_tracker.md)** - Initiative and HP tracking

## Key Reference Documents

- [README.md](README.md) - Core adventure generation instructions for LLMs
- [playtesting_guidelines.md](playtesting_guidelines.md) - Detailed playtesting procedures
- [feedback.md](feedback.md) - System analysis and improvement proposals
- [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - Quick start guide and implementation overview
- [.claude/agents/\*/README.md](.claude/agents/) - Individual agent instructions

## Example Adventures

- `lulu_the_piggy/` - "The Brass Contract" - Psychological corporate horror with infernal twist
- `lulu_the_piggy_2/` - Sequel adventure with enhanced structure
- `Shadows_Over_Havenwood/` - Fantasy town with mysterious cosmic phenomenon

These serve as reference implementations of the structure and principles.
