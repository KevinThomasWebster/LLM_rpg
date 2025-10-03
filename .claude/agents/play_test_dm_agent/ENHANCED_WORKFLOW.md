# Play Test DM Agent - Enhanced Workflow

## NEW: Dice Rolling Protocol

### Using dice_roller.py

For ALL dice rolls in playtests, use the dice roller tool for reproducibility and statistical tracking.

**Before Playtest - Set Seed:**
```bash
# Use playtest number × 1000 as seed
# Playtest 1: seed 1000
# Playtest 2: seed 2000
# Playtest 3: seed 3000
# etc.

SEED=$((PLAYTEST_NUM * 1000))
```

**During Playtest - For Each Roll:**
```bash
python tools/dice_roller.py --roll "1d20+5" --seed {SEED} \
  --character "{CHARACTER_NAME}" \
  --action "{ACTION_DESCRIPTION}" \
  --round {ROUND_NUMBER} \
  --log play_tests/{ENCOUNTER}/playtest_{N}_rolls.json
```

**Examples:**
```bash
# Alex makes a Perception check in Round 1
python tools/dice_roller.py --roll "1d20+3" --seed 1000 \
  --character "Alex" \
  --action "Perception check to notice Rem's signals" \
  --round 1 \
  --log play_tests/Design_Studio/playtest_1_rolls.json

# Casey hacks workstation with advantage in Round 2
python tools/dice_roller.py --roll "1d20+5" --seed 1000 --advantage \
  --character "Casey" \
  --action "Technology check to hack workstation" \
  --round 2 \
  --log play_tests/Design_Studio/playtest_1_rolls.json

# Ben makes Athletics check in Round 3
python tools/dice_roller.py --roll "1d20+1" --seed 1000 \
  --character "Ben" \
  --action "Athletics check to delay security Lulus" \
  --round 3 \
  --log play_tests/Design_Studio/playtest_1_rolls.json
```

**Recording in Narrative:**
Always include roll results in the playtest narrative:

```markdown
**Round 3**
- **DM:** The security Lulus are just a few feet away from you now.
- **Ben:** Ben yelps and scrambles back as the Lulus advance. He attempts to use his athleticism to delay them (Athletics check).
- **Roll:** 1d20+1 = 15 (success)
- **DM:** Ben successfully interposes himself between the Lulus and his companions, giving them precious seconds.
```

**After Playtest - Get Statistics:**
```bash
python tools/dice_roller.py \
  --import play_tests/{ENCOUNTER}/playtest_{N}_rolls.json \
  --stats

# Output will show:
# - Mean d20 roll
# - Critical hit/fail rates
# - Bias detection (chi-squared test)
```

## NEW: Structured Data Output

### JSON Sidecar Files

Alongside each playtest narrative (`playtest_N.md`), create a structured data file (`playtest_N_data.json`).

**File Location:**
```
play_tests/{ENCOUNTER_NAME}/
├── playtest_1.md          # Narrative playtest
├── playtest_1_data.json   # Structured metrics (NEW)
├── playtest_1_rolls.json  # Dice roll log
├── playtest_2.md
├── playtest_2_data.json
├── playtest_2_rolls.json
└── summary.md
```

**Required Data Structure:**

```json
{
  "playtest_id": "playtest_1",
  "encounter": "{ENCOUNTER_NAME}",
  "metadata": {
    "date": "2025-10-01",
    "duration_minutes": 28,
    "stages_completed": 4,
    "dice_seed": 1000,
    "pc_approach": "mixed"
  },
  "character_actions": [
    {
      "round": 1,
      "character": "Alex",
      "action_type": "investigate",
      "skill_check": "Perception",
      "roll": 15,
      "modifier": 3,
      "total": 18,
      "success": true,
      "description": "Alex notices Rem's frantic signals"
    },
    {
      "round": 1,
      "character": "Casey",
      "action_type": "hack",
      "skill_check": "Technology",
      "roll": 13,
      "modifier": 5,
      "total": 18,
      "success": true,
      "description": "Casey hacks workstation, finds facility map"
    },
    {
      "round": 1,
      "character": "Ben",
      "action_type": "investigate",
      "skill_check": "Perception",
      "roll": 8,
      "modifier": 1,
      "total": 9,
      "success": false,
      "description": "Ben too distracted admiring tech to notice Rem"
    }
  ],
  "spotlight_distribution": {
    "Alex": 8,
    "Casey": 9,
    "Ben": 6
  },
  "clues_discovered": [
    "Rem's Journal (from Alex's tablet)",
    "Facility Map (from hacked workstation)",
    "Hidden Messages (from under desk)"
  ],
  "props_used": [
    "Alex's Tablet",
    "Empathy Lock",
    "Pneumatic Tubes (diversion)"
  ],
  "win_condition": "escaped_with_journal",
  "stages": {
    "hook": {
      "rounds": 2,
      "duration_estimate": "6 minutes"
    },
    "complication": {
      "rounds": 2,
      "duration_estimate": "8 minutes"
    },
    "escalation": {
      "rounds": 4,
      "duration_estimate": "10 minutes"
    },
    "climax": {
      "rounds": 2,
      "duration_estimate": "4 minutes"
    }
  },
  "improvised_content": [
    "Added First Day Jitters bot personality quirks",
    "Created pneumatic tube diversion opportunity",
    "Rem's emotional reaction to players helping"
  ]
}
```

**Action Types:**
- `attack` - Combat attack
- `investigate` - Investigation/Perception checks
- `social` - Persuasion/Deception/Insight checks
- `hack` - Technology/hacking
- `cast_spell` - Spellcasting
- `movement` - Pure movement/positioning
- `other` - Anything else

### Tracking During Playtest

**Round-by-Round Tracking:**
1. Note which character acts
2. Record action type
3. Record skill check (if any)
4. Record roll result
5. Record success/failure
6. Brief description

**Spotlight Counting:**
Keep a tally of meaningful actions per character:
- Alex: ||||
- Casey: |||||
- Ben: |||

**Clues and Props:**
List when discovered/used:
- "Rem's Journal" - discovered Round 5
- "Empathy Lock" - used Round 4-5
- "Pneumatic Tubes" - used Round 6 (diversion)

**Stage Timing:**
Note when each stage ends:
- Hook: Rounds 1-2
- Complication: Rounds 3-4
- Escalation: Rounds 5-7
- Climax: Rounds 8-10

## Quick Reference Access

### Before Starting Playtest

1. **Read Encounter Cheat Sheet** (if available):
   - `dm_materials/session_cheatsheets/{encounter_name}.md`
   - Contains stage triggers, NPC objectives, win conditions
   - Has fallback options if players stuck

2. **Have NPC Cards Ready** (if available):
   - `dm_materials/npc_cards/`
   - Quick stat block access
   - Roleplay reminders (voice, motivation)

3. **Review Faction Goals:**
   - Check `01_Factions.md` for proactive timelines
   - Note what each faction will do if players are passive

4. **Note Available Clues:**
   - Check `secrets_and_clues.md` or clue tracker
   - Know discovery methods and DCs

### During Playtest

**Consult Cheat Sheet For:**
- Stage progression triggers
- NPC proactive actions
- Win conditions
- Environmental interactivity options
- Fallback options if players stuck

**Don't Reveal Meta-Information:**
- Don't tell Play Test Players Agent what the "stages" are
- Don't reveal win conditions directly
- Don't hint at planned NPC actions

**Use Fallback Options:**
If players seem stuck for 2+ rounds:
- Escalate NPC proactive action
- Introduce environmental clue
- Have friendly NPC provide hint
- Create new complication that pushes forward

## Pacing Guidelines

### 10-15 Meaningful Exchanges Target

**What Counts as "Meaningful":**
✅ Player makes a skill check
✅ Player interacts with NPC
✅ Player discovers clue or uses prop
✅ Player makes tactical decision
✅ NPC takes proactive action

❌ Pure movement without challenge
❌ Routine discussion without decisions
❌ Repetitive failed attempts (use "Falling Forward" instead)

**Stage Breakdown (Example for 12-round encounter):**
- **Hook (Rounds 1-3):** 3 exchanges
  - Initial observation
  - First investigation attempt
  - NPC introduction

- **Complication (Rounds 4-5):** 2 exchanges
  - Unexpected problem introduced
  - Players react/adapt

- **Escalation (Rounds 6-9):** 4 exchanges
  - Stakes raised
  - Multiple challenges
  - Faction timeline events
  - Creative solutions attempted

- **Climax (Rounds 10-12):** 3 exchanges
  - Final confrontation/puzzle
  - Resolution moment
  - Immediate consequences

### Pacing Techniques

**Don't Rush:**
- Let players explore environment
- Give time for roleplaying
- Allow creative problem-solving
- Build tension gradually

**Do Progress:**
- Use faction proactive timelines
- Introduce complications when pace lags
- Make failures lead to new challenges
- Keep countdown timers (explicit or implicit)

**Signs You're Rushing:**
- Fewer than 8 total rounds
- Skipping straight to climax
- Not using all 4 stages
- Players don't use environment
- No improvisation needed

**Signs You're Dragging:**
- More than 20 rounds
- Repetitive failed checks
- Players stuck in analysis paralysis
- No forward progress for 3+ rounds
- Reusing same challenges

## Integration with Analysis

### After Playtest Completion

1. **Export Dice Statistics:**
   ```bash
   python tools/dice_roller.py \
     --import play_tests/{ENCOUNTER}/playtest_{N}_rolls.json \
     --stats
   ```

2. **Create Structured Data JSON:**
   - Use template above
   - Fill in all required fields
   - Save as `playtest_{N}_data.json`

3. **Include Statistics in Frontmatter:**
   ```yaml
   ---
   playtest_id: playtest_1
   encounter: Design_Studio
   dice_seed: 1000
   dice_stats:
     mean_roll: 10.8
     critical_hits: 2
     critical_fails: 1
   spotlight_distribution:
     Alex: 35%
     Casey: 39%
     Ben: 26%
   ---
   ```

4. **Note Improvised Content:**
   - What did you create that wasn't in the adventure documents?
   - What worked well?
   - What should be added to official documents?

### Workflow Example

**Complete playtest workflow:**

```bash
# 1. Set seed
SEED=1000

# 2. Run playtest, using dice_roller for all rolls
# (Throughout playtest, use python tools/dice_roller.py ...)

# 3. After completion, get statistics
python tools/dice_roller.py \
  --import play_tests/Design_Studio/playtest_1_rolls.json \
  --stats

# 4. Create structured data JSON manually
# Save to play_tests/Design_Studio/playtest_1_data.json

# 5. Write narrative playtest
# Save to play_tests/Design_Studio/playtest_1.md

# 6. Both files ready for Play Test Grader Agent analysis
```

## Best Practices Summary

✅ **DO:**
- Use dice_roller.py for all rolls
- Create structured data JSON
- Track spotlight distribution
- Note improvised content
- Use encounter cheat sheets
- Aim for 10-15 meaningful exchanges
- Use "Falling Forward" principle
- Consult faction proactive timelines

❌ **DON'T:**
- Skip dice roller (breaks reproducibility)
- Forget to create data JSON (breaks analysis)
- Rush to climax (aim for depth)
- Let players get stuck (use fallback options)
- Reveal meta-information to players
- Ignore faction timelines
- Make failures dead ends

---

**Remember:** Quality over speed. A rich, 12-round playtest with structured data is far more valuable than a rushed 6-round playtest without metrics.
