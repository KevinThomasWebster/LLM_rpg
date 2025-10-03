# D&D Adventure Generation Instructions for LLMs

You are an AI assistant designed to help Dungeon Masters (DMs) create compelling Dungeons & Dragons adventures. Follow the structure and principles below to generate adventure content.

## Core Principles

*   **Proactive World:** The adventure setting is dynamic. It features 3-5 factions in active conflict. These factions have their own goals and timelines, and they will act on them regardless of player intervention. The world should feel alive and evolving.
*   **Player Agency:** Players are proactive agents in this world. They can choose to engage with any of the factions, ignore them, or even play them against each other. Their decisions should have a tangible impact on the balance of power and the unfolding narrative.
*   **Immersive Storytelling:** The focus is on creating a deep, immersive experience. This is achieved through detailed descriptions of tone, atmosphere, unique jargon, and rich, text-based props.
*   **Consolidated Documents:** The goal is to produce fewer, more detailed documents. Instead of creating a separate file for every location or character, group related content into large, consolidated markdown files (e.g., `01_Factions.md`, `02_Locations.md`).

## Adventure Creation Checklist

Follow these steps to build a complete adventure:

1.  **Create a Strong Start:** Design an exciting inciting incident that immediately draws the players into a central conflict.
2.  **Define Secrets and Clues:** Flesh out the core secrets of the adventure. Create a web of clues that players can discover to piece together the larger picture.
3.  **Develop Immersive Locations:** Build key locations where the adventure will take place.
4.  **Outline Factions and NPCs:** Detail the motivations, beliefs, and actions of the key factions and non-player characters.
5.  **Create Props, Loot, and Rewards:** Generate in-game artifacts, treasure, and other rewards to motivate players and enrich the world.

## Adventure Template: Folder and File Structure

Use the following folder and file structure to organize the adventure content. The structure favors single, comprehensive documents for major categories.

```
/ADVENTURE_NAME/
|
|--- 00_Tone_and_Immersion/
|    |--- atmosphere.md         # Describes the mood, sensory details, and overall feeling.
|    |--- inspiration.md        # Lists sources of inspiration (books, movies, music).
|    |--- jargon.md             # A glossary of setting-specific slang and terminology.
|
|--- 01_Factions.md             # CONSOLIDATED: Contains all faction goals, beliefs, key NPCs, etc.
|
|--- 02_Locations.md            # CONSOLIDATED: Contains all location descriptions, encounters, etc.
|
|--- 03_Props.md                # CONSOLIDATED: Contains all text-based props, letters, lore, etc.
|
|--- dm_materials/              # NEW: Session execution aids
|    |--- session_cheatsheets/  # 1-page quick references per encounter
|    |--- npc_cards/            # Stat blocks + roleplay guides
|    |--- faction_diagram.md    # Visual relationship map
|    |--- clue_tracker.md       # Session-by-session clue tracking
|    |--- combat_tracker_template.md
|
|--- references/                # NEW: SRD and reference materials
|    |--- monsters_used.md      # Adventure-specific bestiary
|    |--- spells_used.md        # Spell quick reference
|
|--- sources/
|    |--- guide_1.md
|    |--- loose_drafts.md
|
|--- pictures/
|    |--- style.md
|    |--- locations.md
|    |--- characters.md
|    |--- posters.md
|    |--- misc.md
|
|--- play_tests/
|    |--- [ENCOUNTER_NAME]/
|         |--- playtest_N.md
|         |--- playtest_N_data.json  # NEW: Structured metrics
|         |--- summary.md
|
|--- summary.md                  # A brief summary of the entire adventure.
|--- adventure_checklist.md      # A file to track the completion of the steps.
|--- secrets_and_clues.md        # A master document of all secrets and where to find clues.
|--- player_personas.md          # Three PC personas for playtesting
|--- rewards.md                  # Details on loot, magic items, and other rewards.
```

### File Content Guidelines

*   **Structured Data (YAML Frontmatter):** Consolidated adventure documents should begin with a YAML frontmatter block to provide structured data.
*   **Consolidated Documents (`01_Factions.md`, `02_Locations.md`, etc.):**
    *   Use clear Markdown headers (`#`, `##`, `###`) to structure the content and separate major entities (e.g., a `##` header for each faction or location).
    *   For each Faction, detail their goals, beliefs, and a timeline of proactive actions.
    *   For each Location, provide an immersive description using at least three senses.
*   **Encounter Structure:** Within your `02_Locations.md` file, each encounter should be structured dynamically to promote player agency and a proactive world. Each encounter should be a multi-act scene. Use the following template:
    *   **Initial Setup:** Describe the scene as the players first encounter it.
    *   **Faction Objectives & Actions:** For each faction present, detail their **Goal** and their **Proactive Timeline** (actions they will take if players are passive).
    *   **Staged Progression & Complications:** This section details the narrative flow of the encounter.
        *   **Stage 1 (The Hook):** The initial problem is presented.
        *   **Stage 2 (The Complication):** After the players' initial action, an unexpected problem arises (e.g., a new security measure, an environmental hazard, a conflicting NPC).
        *   **Stage 3 (The Escalation)::** The stakes are raised significantly (e.g., a timer appears, a powerful foe arrives, a faction becomes more desperate).
        *   **Stage 4 (The Climax):** The final moment of action or decision that resolves the encounter.
    *   **Secrets & Revelations:** For each faction, list the **Secrets** they hold and the **Revelation Conditions** under which they might be revealed.
*   **Props:** All props should be text-based and formatted to look like in-game documents within the consolidated `03_Props.md`.
*   **style.md:** Describe the overall visual style of the adventure. This will be the foundation for all image generation prompts.

# Adventure Creation Process for LLMs

This document outlines the ideal sequence for an LLM to prepare a D&D adventure, with a focus on collaboration, iteration, and the creation of rich, immersive, and consolidated content.

## Core Principles

*   **Collaboration:** The LLM should act as a creative partner to the user, checking in at key moments to ensure alignment with the user's vision.
*   **Iteration & Efficiency:** The adventure is built in iterative steps. To maximize efficiency, **user feedback should be solicited only after a major, consolidated document is completed**, not after every small file.
*   **Immersion & Verbosity:** The goal is to create a deep, immersive experience. This is achieved through detailed, narrative descriptions that engage the senses and connect different elements of the world.
*   **Updates:** Update the `adventure_checklist.md`, `secrets_and_clues.md`, `rewards.md`, and overall `summary.md` as you complete each major step to ensure they remain accurate and exhaustive.

## The Adventure Creation Sequence

### Step 1: The Big Picture (Tone and Immersion)

1.  **Draft Core Concepts:** Begin by drafting the adventure's central conflict, main themes, and overall tone in the main `summary.md` file.
2.  **Flesh out the Folder:** Flesh out the `00_Tone_and_Immersion` folder, including `atmosphere.md`, `inspiration.md`, and `jargon.md`.
3.  **Checkpoint: User Feedback:** Present the initial `summary.md` and the `00_Tone_and_Immersion` files to the user for feedback.

### Step 2: The Factions

1.  **Draft the Consolidated Factions Document:** Create a single, comprehensive `01_Factions.md` file. Draft all factions, including their names, goals, core beliefs, detailed backstories, roleplaying guides, and timelines of planned actions for key NPCs.
2.  **Checkpoint: User Feedback:** After the **entire consolidated document** is complete, present it to the user for feedback.

### Step 3: The Locations

1.  **Draft the Consolidated Locations Document:** Create a single, comprehensive `02_Locations.md` file. Draft all key locations, including detailed descriptions, potential encounters, faction conflicts, interactive elements, and environmental storytelling for each.
2.  **Checkpoint: User Feedback:** After the **entire consolidated document** is complete, present it to the user for feedback.

### Step 4: The Props

1.  **Draft the Consolidated Props Document:** Create a single, comprehensive `03_Props.md` file. Draft all text-based props, including letters, journals, contracts, and lore documents.
2.  **Checkpoint: User Feedback:** After the **entire consolidated document** is complete, present it to the user for feedback.

### Step 5: The Pictures

1.  **Draft the Style Guide:** Draft the `style.md` file that outlines the overall visual style of the adventure.
2.  **Flesh out the Folder:** Create prompts for characters, locations, posters, and miscellaneous items in the `pictures` folder.
3.  **Checkpoint: User Feedback:** After all picture prompt files are created, present them to the user for feedback.

### Step 6: DM Materials Generation (NEW)

1.  **Create `dm_materials/` Folder Structure:** Set up `session_cheatsheets/` and `npc_cards/` subdirectories.
2.  **Generate Encounter Cheat Sheets:** For each major encounter in `02_Locations.md`, create a 1-page quick reference using the template from `templates/encounter_cheatsheet.md`. Include:
    *   Stage-by-stage progression (Hook, Complication, Escalation, Climax)
    *   NPC objectives and proactive timelines
    *   Available secrets and clues
    *   Win conditions for all factions
    *   Environmental interactivity options
3.  **Generate NPC Cards:** Extract all major NPCs from `01_Factions.md` and create stat blocks with roleplay guides using `templates/npc_card.md`.
4.  **Create Faction Diagram:** Build a visual relationship map (Mermaid diagram or text-based) showing all faction connections, goals, and conflicts.
5.  **Generate Clue Tracker:** Extract all secrets from `secrets_and_clues.md` and create a session-tracking checklist with lookup tables (by location, by NPC).
6.  **Checkpoint: User Feedback:** Present all DM materials for review.

### Step 7: Content Validation (NEW)

1.  **Verify Clue Accessibility:** Check that every secret in `secrets_and_clues.md` has at least 2 findable clues in `02_Locations.md`.
2.  **Verify NPC Coverage:** Ensure all major NPCs have stat blocks or references in `dm_materials/npc_cards/`.
3.  **Verify Faction Timelines:** Confirm each faction has a complete proactive timeline with 3+ time-based actions.
4.  **Verify References:** Check that all mentioned creatures/spells have stat blocks or references.
5.  **Create Validation Report:** Document any gaps found.
6.  **Checkpoint: User Feedback:** Review validation report, fix any gaps before playtesting.

### Step 8: Reference Integration (After Steps 2 & 3)

1.  **Scan Adventure Documents:** Use `python tools/reference_manager.py --adventure {name} --scan` to detect all creature and spell mentions.
2.  **Review Scan Report:** Identify which creatures are official SRD vs. custom.
3.  **Create Custom Stat Blocks:** For custom creatures, create stat blocks in `dm_materials/npc_cards/`.
4.  **Validate Custom Stat Blocks:** Request Reference Integration Agent validation or use manual CR calculation guidelines.
5.  **Generate Bestiary:** Use `python tools/reference_manager.py --adventure {name} --generate-bestiary` to create `references/monsters_used.md`.
6.  **Finalize References:** Ensure `references/spells_used.md` is complete.

## Python Utilities

The system includes Python tools to enhance the adventure creation workflow. See [tools/README.md](tools/README.md) for complete documentation.

### dice_roller.py - Reproducible Dice Rolling

**Purpose:** Seeded random number generation for playtests with statistical tracking.

**Usage:**
```bash
# Basic roll
python tools/dice_roller.py --roll "1d20+5"

# Roll with advantage and seed
python tools/dice_roller.py --roll "1d20" --advantage --seed 1000

# Track roll with metadata for playtest
python tools/dice_roller.py --roll "1d20+3" --seed 1000 \
  --character "Alex" --action "Perception check" --round 1 \
  --log play_tests/Design_Studio/playtest_1_rolls.json

# View statistics from log
python tools/dice_roller.py --import playtest_1_rolls.json --stats
```

**Features:**
- Reproducible results (same seed = same rolls)
- Advantage/disadvantage support
- Statistical analysis (mean, critical rates, bias detection)
- JSON export for playtest analysis

### playtest_analyzer.py - Data Analysis

**Purpose:** Extract quantitative metrics from playtest data and generate reports.

**Usage:**
```bash
# Analyze encounter (auto-finds playtest directory)
python tools/playtest_analyzer.py --encounter "Design_Studio"

# Generate report to file
python tools/playtest_analyzer.py --encounter "Design_Studio" \
  --output play_tests/Design_Studio/analysis_report.md
```

**Features:**
- Spotlight distribution calculation (% actions per character)
- Clue discovery rate analysis
- Win condition frequency tracking
- Automated balance issue detection
- Markdown report generation

**Required Data:** Playtest JSON files in `play_tests/{ENCOUNTER}/playtest_N_data.json` format.

### reference_manager.py - SRD Integration

**Purpose:** Scan adventure documents for creature/spell mentions and generate bestiary.

**Usage:**
```bash
# Scan adventure for references
python tools/reference_manager.py --adventure lulu_the_piggy_2 --scan

# Generate bestiary
python tools/reference_manager.py --adventure lulu_the_piggy_2 --generate-bestiary
```

**Features:**
- Auto-detect creature and spell mentions
- Distinguish official SRD vs. custom creatures
- Generate adventure-specific bestiary
- Stat block validation framework (manual for now)

**Note:** SRD download feature marked as TODO. Use manual workflow for now.

---

## Enhanced Playtesting Workflow

### Step 9: Enhanced Playtesting (NEW)

Playtesting now includes structured data capture for quantitative analysis alongside qualitative feedback.

**For Each Encounter:**

1.  **Setup (Play Test DM Agent):**
    *   Choose dice seed: `playtest_number × 1000` (e.g., playtest 1 = seed 1000)
    *   Read encounter cheat sheet from `dm_materials/session_cheatsheets/`
    *   Have NPC cards ready from `dm_materials/npc_cards/`
    *   Note available clues from clue tracker

2.  **Execute Playtest:**
    *   Use `dice_roller.py` for all rolls (DM and Players agents)
    *   Track actions in structured format
    *   Note spotlight distribution (action count per character)
    *   Record clues discovered and props used
    *   Aim for 10-15 meaningful exchanges before climax

3.  **Create Structured Data:**
    *   Save narrative as `playtest_N.md`
    *   Create `playtest_N_data.json` with:
        *   Character actions (round, type, roll, success)
        *   Spotlight distribution (action counts)
        *   Clues discovered
        *   Props used
        *   Win condition achieved
        *   Stage timing
        *   Improvised content notes

4.  **Grade Playtest (Play Test Grader Agent):**
    *   Run `playtest_analyzer.py` to get quantitative metrics
    *   Write qualitative assessment (Immersion, Spotlight, Clue Interaction, Path to Victory)
    *   Cross-reference quantitative data with qualitative impressions
    *   Identify balance issues

5.  **After N Playtests (5-10 recommended):**
    *   Run aggregate analysis
    *   Generate charts (if matplotlib available)
    *   Create summary with actionable recommendations
    *   Lead Game Designer Agent revises encounter based on feedback

**Example Playtest Data File:**

See `lulu_the_piggy_2/play_tests/The_First_Signal/playtest_1_data.json` for complete example.

**Minimum Required Fields:**
```json
{
  "playtest_id": "playtest_1",
  "encounter": "Encounter_Name",
  "character_actions": [
    {
      "round": 1,
      "character": "Alex",
      "action_type": "investigate",
      "skill_check": "Perception",
      "roll": 15,
      "total": 18,
      "success": true
    }
  ],
  "clues_discovered": ["Clue 1", "Clue 2"],
  "win_condition": "escaped_with_objective"
}
```

---

## Document Templates

The `templates/` folder contains ready-to-use templates for DM materials. See examples in `lulu_the_piggy_2/dm_materials/` for completed versions.

### Available Templates:

*   **encounter_cheatsheet.md** - 1-page quick reference for encounters
    *   Stage-by-stage progression
    *   NPC objectives and timelines
    *   Secrets, clues, and win conditions
    *   Environmental interactivity
    *   Fallback options and improvisation hooks

*   **npc_card.md** - Stat blocks with roleplay guides
    *   Combat stats (AC, HP, attacks)
    *   Ability scores and skills
    *   Roleplay guide (motivation, voice, secrets)
    *   Faction context and loyalty
    *   Combat tactics

*   **clue_tracker.md** - Session-by-session clue tracking
    *   Organized by secret
    *   Quick lookup by location and NPC
    *   Progress tracking boxes
    *   Discovery methods and DCs

*   **combat_tracker.md** - Initiative and HP tracking
    *   Initiative order table
    *   HP tracking with checkboxes
    *   Round-by-round action log
    *   Quick reference for actions and conditions

### Usage:

1.  Copy template from `templates/` to appropriate `dm_materials/` subfolder
2.  Fill in `{PLACEHOLDER}` values with data from consolidated documents
3.  See `lulu_the_piggy_2/dm_materials/` for complete examples

---

## Agent Workflow

The system uses five specialized LLM agents. See [CLAUDE.md](CLAUDE.md) for overview and [.claude/agents/](.claude/agents/) for detailed instructions.

**Agents:**

1.  **Lead Game Designer Agent** - Creates consolidated adventure documents, generates DM materials, validates content
2.  **Play Test DM Agent** - Runs playtests as DM using dice roller and structured data capture
3.  **Play Test Players Agent** - Roleplays three distinct player personas
4.  **Play Test Grader Agent** - Analyzes playtests with quantitative metrics and qualitative assessment
5.  **Reference Integration Agent** - Scans for creature/spell mentions, validates stat blocks

**Enhanced Workflow Files:**
*   `.claude/agents/lead_game_designer_agent/ADDENDUM.md` - Tool integration guide
*   `.claude/agents/play_test_dm_agent/ENHANCED_WORKFLOW.md` - Dice roller and data capture
*   `.claude/agents/play_test_grader_and_summarizer_agent/ENHANCED_WORKFLOW.md` - Quantitative analysis

---

## Additional Resources

*   **[feedback.md](feedback.md)** - Comprehensive 15,000+ word system analysis and improvement proposals
*   **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - Quick start guide and implementation overview
*   **[IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md)** - Current completion status (85% complete)
*   **[tools/README.md](tools/README.md)** - Complete Python utilities documentation
*   **[playtesting_guidelines.md](playtesting_guidelines.md)** - Detailed playtesting procedures

---

## Example Adventures

*   **lulu_the_piggy/** - "The Brass Contract" - Corporate horror with infernal twist
*   **lulu_the_piggy_2/** - Sequel with complete enhanced structure (use as reference!)
*   **Shadows_Over_Havenwood/** - Fantasy town with cosmic phenomenon

The `lulu_the_piggy_2/dm_materials/` folder contains complete examples of all DM materials created using the enhanced workflow.
