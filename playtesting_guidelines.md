    # Playtesting Guidelines for LLMs

This document outlines the ideal process for an LLM to run a playtest of a D&D adventure, with a focus on creating a detailed and useful feedback loop for the adventure designer.

## Core Principles

*   **Simulation:** The LLM should act as both the Dungeon Master and a party of three Player Characters, simulating a real playtest session.
*   **Focus on Player Agency:** The playtest should focus on player actions and how the story and the factions react to their decisions.
*   **Data-Driven Feedback:** The goal of the playtest is to generate data that can be used to improve the encounter. This means tracking which characters shine, which clues are used, and which win conditions are met.

## The Playtesting Process

### The Unit of a Playtest: The Encounter

Each playtest should focus on a single encounter. The playtests do not need to connect to each other, and they can use different starting points if necessary. This allows for a more focused and granular analysis of each encounter.

### Step 1: The Setup

For each encounter, the LLM should begin by setting the scene. This includes:

*   **Starting Point:** A brief description of how the players arrived at this encounter.
*   **Characters Present:** A list of all the player characters and non-player characters present in the encounter. Annotate each NPC with their faction.
*   **Clues, Secrets, and Props:** A list of all the clues, secrets, and props that are present in the encounter.
*   **Win Conditions:** A list of the possible win conditions for the encounter, for both the players and the other factions. Ensure all present factions have a win condition.

### Step 2: The Encounter

The LLM should then play through the encounter, narrating the actions of the DM and the three PCs. The LLM should:

*   **Simulate Dice Rolls Using dice_roller.py:** For reproducibility and statistical analysis, use the `dice_roller.py` tool with a consistent seed. See the **Dice Rolling Protocol** section below.
*   **Track Structured Data:** Create a JSON sidecar file alongside the narrative playtest to enable quantitative analysis. See the **Structured Data Requirements** section below.
*   **Narrative Pacing:** Guide the encounter to a satisfying narrative conclusion. The encounter ends when a win condition is met or the central conflict of the scene is resolved. Focus on the quality of roleplaying and meaningful progression, not an arbitrary number of rounds.
*   **Give Each Character a Chance to Shine:** The LLM should ensure that each character has an opportunity to use their unique skills and abilities during the encounter.
*   **Play to the Win Condition:** The LLM should play through the encounter until one or more of the win conditions are met.

#### Dice Rolling Protocol

**All dice rolls during playtests MUST use the `dice_roller.py` tool** to ensure reproducibility and enable statistical analysis:

```bash
python tools/dice_roller.py --roll "1d20+5" --seed {SEED} \
  --character "{CHARACTER_NAME}" \
  --action "{ACTION_DESCRIPTION}" \
  --round {ROUND_NUMBER} \
  --log play_tests/{ENCOUNTER}/playtest_{N}_rolls.json
```

**Parameters:**
- `--roll`: Dice notation (e.g., "1d20+5", "2d6", "1d20 advantage", "1d20 disadvantage")
- `--seed`: Use the same seed throughout the entire playtest (e.g., 1000, 1001, 1002 for sequential playtests)
- `--character`: Name of the character making the roll
- `--action`: Brief description of what they're attempting
- `--round`: Current round number (for sequencing)
- `--log`: Path to JSON log file (one per playtest)

**Example:**

```bash
# Round 1: Alex tries to detect lies
python tools/dice_roller.py --roll "1d20+3" --seed 1000 \
  --character "Alex" \
  --action "Insight check on Ms. Reed's explanation" \
  --round 1 \
  --log play_tests/The_First_Signal/playtest_1_rolls.json

# Output: Rolled 1d20+3 = 14+3 = 17
```

Then incorporate the result into your narrative:

> Alex studies Ms. Reed's face carefully as she explains the containment protocols. [Insight 17] Her micro-expressions betray genuine fear when she mentions the 4th floor - whatever is happening up there, she's terrified of it.

**Benefits:**
- **Reproducibility:** Re-running the same encounter with the same seed produces identical rolls
- **Statistical Analysis:** The Grader Agent can analyze roll distributions for bias or balance issues
- **Audit Trail:** Every roll is logged with context for later review

#### Structured Data Requirements

In addition to the narrative playtest markdown file, create a JSON sidecar file named `playtest_{N}_data.json` with the following structure:

```json
{
  "playtest_id": "playtest_1",
  "encounter": "The_First_Signal",
  "metadata": {
    "duration_minutes": 32,
    "stages_completed": 4,
    "dice_seed": 1000,
    "pc_approach": "mixed|stealth|combat|social"
  },
  "character_actions": [
    {
      "round": 1,
      "character": "Alex",
      "action_type": "investigate|combat|social|stealth|support",
      "skill_check": "Insight",
      "roll": 14,
      "modifier": 3,
      "total": 17,
      "success": true,
      "description": "Studies Ms. Reed for deception",
      "impact": "high|medium|low",
      "spotlight_moment": true
    }
  ],
  "spotlight_distribution": {
    "Alex": 7,
    "Casey": 9,
    "Ben": 5
  },
  "clues_discovered": [
    {
      "clue_id": "secret_1",
      "discovery_round": 3,
      "discovered_by": "Casey",
      "method": "Investigation check on filing cabinet"
    }
  ],
  "props_used": [
    {
      "prop_id": "encrypted_journal",
      "used_round": 8,
      "used_by": "Alex",
      "usage": "Attempted decryption with Arcana check"
    }
  ],
  "win_condition": "escaped_with_journal_and_rem_contact",
  "stages_reached": ["stage_1_hook", "stage_2_complication", "stage_3_escalation", "stage_4_climax"]
}
```

**Key Fields to Track:**

1. **character_actions**: Every meaningful PC action with skill checks
   - Use `spotlight_moment: true` for actions that significantly impacted the encounter
   - Track `impact` level (high/medium/low) for each action

2. **spotlight_distribution**: Count of meaningful actions per character
   - Used to identify balance issues (characters with <15% of total actions)

3. **clues_discovered**: Which secrets were revealed and how
   - Track discovery method for clue accessibility analysis

4. **props_used**: Which props were interacted with
   - Track usage patterns to identify underutilized props

5. **win_condition**: Which win condition was achieved
   - Used to analyze win condition frequency across multiple playtests

This structured data enables the `playtest_analyzer.py` tool to generate quantitative reports automatically.

### Step 3: The Grading

After each playtest, the LLM should grade the encounter based on both **qualitative criteria** and **quantitative analysis**. Please supply concrete examples for each category.

#### Qualitative Assessment

*   **Immersion:** How immersive was the encounter? Did the descriptions and the dialogue create a strong sense of atmosphere?
*   **Character Spotlight:** Which characters got to shine in the encounter? Did each character have a meaningful impact on the outcome?
*   **Clue and Prop Interaction:** Which secrets or props did the characters interact with? Were the clues easy to find? Were the props useful?
*   **Path to Victory:** How interesting was the path to the win condition? Was it a straightforward slugfest, or did the players have to be clever and creative to succeed?

#### Quantitative Analysis

**Use the `playtest_analyzer.py` tool** to generate data-driven insights from the JSON sidecar file:

```bash
python tools/playtest_analyzer.py \
  --adventure {ADVENTURE_NAME} \
  --encounter {ENCOUNTER_NAME} \
  --output play_tests/{ENCOUNTER_NAME}/playtest_{N}_analysis.md
```

This generates a report with:

1. **Spotlight Distribution**
   - Percentage of meaningful actions per character
   - Flags characters with <15% spotlight as potential balance issues
   - Example: "Alex: 33% (7/21), Casey: 43% (9/21), Ben: 24% (5/21)"

2. **Clue Discovery Rates**
   - Which clues were discovered vs. missed
   - Discovery methods used (Investigation, Insight, Persuasion, etc.)
   - Example: "Secret #1: 100% (discovered in all playtests), Secret #3: 0% (never discovered)"

3. **Prop Usage Patterns**
   - Which props were used vs. ignored
   - How props were used creatively
   - Example: "Encrypted journal: Used in 3/3 playtests, Always via Arcana check"

4. **Win Condition Frequency**
   - Which win conditions are achieved most often
   - Difficulty balance across factions
   - Example: "Player victory: 2/3, Shadow Court victory: 1/3, Draw: 0/3"

5. **Dice Roll Statistics**
   - Average rolls, success rates, critical hit/miss frequency
   - Bias detection (chi-squared test for fair distribution)
   - Example: "Average d20 roll: 10.2 (expected 10.5), no significant bias detected"

**Combining Qualitative + Quantitative:**

Your grading should reference both narrative observations AND hard data:

> **Character Spotlight:** Casey dominated this playtest with 43% of meaningful actions, particularly in social encounters. Ben felt overshadowed at only 24% - he attempted several Investigation checks but rolled poorly (average 8.5 vs. DC 12). Consider lowering Investigation DCs or providing alternative clue discovery methods that favor his Athletics/Survival strengths.

This approach provides actionable feedback for the adventure designer.

### Step 4: The Summary

After running multiple playtests of the same encounter, the LLM should create a summary that analyzes the data from all of the playtests. This summary should be included in the same consolidated playtest file.

The summary should focus on:

*   **Character Spotlight:** How often was a given character allowed to shine? Is there a character that is consistently being overshadowed?
*   **Clue and Prop Usage:** How often was a given secret or prop used? Is there a clue that is consistently being missed? Is there a prop that is not as useful as it could be?
*   **Win Condition Frequency:** How often was a given win condition triggered? Is there a win condition that is too easy or too difficult to achieve?

## Suggested Folder Structure

All playtesting files should be stored in a `play_tests` folder. Within that folder, create a subfolder for each encounter containing:
- Narrative playtest markdown files
- JSON data files (one per playtest)
- Dice roll logs (one per playtest)
- Analysis reports (generated by `playtest_analyzer.py`)
- Consolidated summary across all playtests

```
/ADVENTURE_NAME/
|
|--- play_tests/
|    |--- ENCOUNTER_NAME_1/
|    |    |--- playtest_1.md              # Narrative playtest
|    |    |--- playtest_1_data.json       # Structured data
|    |    |--- playtest_1_rolls.json      # Dice roll log
|    |    |--- playtest_1_analysis.md     # Generated analysis report
|    |    |--- playtest_2.md
|    |    |--- playtest_2_data.json
|    |    |--- playtest_2_rolls.json
|    |    |--- playtest_2_analysis.md
|    |    |--- summary.md                 # Aggregate summary across all playtests
|    |
|    |--- ENCOUNTER_NAME_2/
|    |    |--- ...
```

**File Descriptions:**

- **playtest_N.md**: Narrative description of the playtest with DM narration, player actions, and dialogue
- **playtest_N_data.json**: Structured data for quantitative analysis (see Structured Data Requirements above)
- **playtest_N_rolls.json**: All dice rolls logged by `dice_roller.py` during the playtest
- **playtest_N_analysis.md**: Auto-generated report from `playtest_analyzer.py` with spotlight distribution, clue discovery rates, etc.
- **summary.md**: Manual summary by the Grader Agent analyzing patterns across all playtests of this encounter

## Further Guidelines

*   **Be Expansive and Detailed:** The more detailed the playtest, the more useful the feedback will be. The LLM should not be afraid to add a fair bit of content to each playtest and improvise if needed.
*   **Explore Different Player Options:** The LLM should run multiple playtests of the same encounter, exploring different player options each time. This will help to identify any potential balance issues or dead ends in the adventure.
*   **Focus on the "Why":** When summarizing the playtests, the LLM should not just focus on what happened, but also on *why* it happened. This will help the adventure designer to understand the underlying issues and to make more effective revisions. Emphasize when the LLM had to improvise, so that the designer can potentially incorporate the ideas in the adventure notes.
