# Reference System Guide

**Managing D&D 5e SRD content and custom stat blocks for your adventures.**

## Purpose

The `references/` folder stores system reference documents (SRD content) and custom stat blocks for your adventures. This system enables:

- **Automatic creature/spell detection** in adventure documents
- **Custom stat block validation** against SRD guidelines
- **Printer-friendly bestiary generation** with only creatures used in your adventure
- **Consistency checking** across multiple encounters
- **Quick reference** during session preparation

## Folder Structure

```
references/
├── srd/                        # D&D 5e System Reference Document
│   ├── creatures/              # Official creature stat blocks
│   │   ├── goblin.json
│   │   ├── beholder.json
│   │   └── ...
│   ├── spells/                 # Official spell descriptions
│   │   ├── fireball.json
│   │   ├── cure_wounds.json
│   │   └── ...
│   └── rules/                  # Core rules reference
│       ├── conditions.json
│       ├── combat_actions.json
│       └── ...
├── custom/                     # Custom stat blocks for this adventure
│   ├── ADVENTURE_NAME/
│   │   ├── shadow_imp.json
│   │   ├── heartbreak_devil.json
│   │   └── ...
├── bestiary/                   # Generated bestiaries (printer-friendly)
│   ├── ADVENTURE_NAME_bestiary.md
│   └── ...
├── scan_reports/               # Reference scan reports
│   ├── ADVENTURE_NAME_scan.md
│   └── ...
└── README.md                   # This file
```

## How to Use the Reference System

### Step 1: Scan Your Adventure

Use `reference_manager.py` to automatically detect all creature and spell mentions in your adventure documents:

```bash
python tools/reference_manager.py --adventure lulu_the_piggy_2 --scan
```

**Output:** A scan report in `references/scan_reports/lulu_the_piggy_2_scan.md` showing:
- All creatures mentioned
- All spells mentioned
- Which documents contain each reference
- Which references exist in SRD vs. need custom stat blocks

**Example scan report:**

```markdown
## Creatures Found

### In SRD (Ready to Use)
- **Imp** - Found in: 02_Locations.md (3 times), 01_Factions.md (1 time)
- **Hell Hound** - Found in: 02_Locations.md (1 time)

### Custom (Need Stat Blocks)
- **Shadow Imp** - Found in: 02_Locations.md (5 times), 01_Factions.md (2 times)
- **Heartbreak (Infernal Negotiator)** - Found in: 01_Factions.md (12 times), 02_Locations.md (8 times)

## Spells Found

### In SRD (Ready to Use)
- **Detect Magic** - Found in: 02_Locations.md (2 times)
- **Zone of Truth** - Found in: 02_Locations.md (1 time)

### Custom (Need Descriptions)
- **Infernal Binding** - Found in: 01_Factions.md (3 times), 03_Props.md (1 time)
```

### Step 2: Review the Scan Report

Open `references/scan_reports/ADVENTURE_NAME_scan.md` and:

1. **Verify SRD references are correct**
   - Check spelling (scanner looks for exact matches)
   - Confirm CR/level is appropriate for your adventure
   - Note if you want to reflavor official creatures

2. **Identify custom stat blocks needed**
   - Any "Custom (Need Stat Blocks)" entries require creation
   - Prioritize creatures that appear multiple times
   - Consider if similar SRD creatures can be reskinned instead

3. **Plan stat block creation**
   - High-frequency creatures first (e.g., Heartbreak appears 20 times)
   - Boss creatures (unique mechanics needed)
   - Minions (can often use SRD templates with minor tweaks)

### Step 3: Create Custom Stat Blocks

For each custom creature, create a JSON file in `references/custom/ADVENTURE_NAME/`:

**Example:** `references/custom/lulu_the_piggy_2/shadow_imp.json`

```json
{
  "name": "Shadow Imp",
  "creature_type": "fiend (devil)",
  "size": "tiny",
  "alignment": "lawful evil",
  "ac": 13,
  "hp": {"average": 10, "formula": "3d4+3"},
  "speed": {"walk": 20, "fly": 40},
  "ability_scores": {
    "str": 6, "dex": 17, "con": 13,
    "int": 11, "wis": 12, "cha": 14
  },
  "saving_throws": {},
  "skills": {"stealth": 5, "deception": 4},
  "damage_resistances": ["cold", "bludgeoning, piercing, and slashing from nonmagical attacks"],
  "damage_immunities": ["fire", "poison"],
  "condition_immunities": ["poisoned"],
  "senses": ["darkvision 120 ft.", "passive Perception 11"],
  "languages": ["Infernal", "Common"],
  "cr": 1,
  "traits": [
    {
      "name": "Devil's Sight",
      "description": "Magical darkness doesn't impede the imp's darkvision."
    },
    {
      "name": "Shadow Blend",
      "description": "While in dim light or darkness, the imp can take the Hide action as a bonus action."
    }
  ],
  "actions": [
    {
      "name": "Sting",
      "description": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4+3) piercing damage plus 3 (1d6) poison damage."
    },
    {
      "name": "Invisibility",
      "description": "The imp magically turns invisible until it attacks, or until its concentration ends (as if concentrating on a spell). Any equipment the imp wears or carries is invisible with it."
    }
  ],
  "based_on": "Imp (SRD)",
  "modifications": "Added Shadow Blend trait, increased Stealth bonus, changed size to Tiny"
}
```

**Tips for custom stat blocks:**
- **Base on similar SRD creatures** when possible (note in `based_on` field)
- **Follow CR guidelines** for HP, AC, attack bonuses (see CR Calculation below)
- **Use standard action economy** (1 action, 1 bonus action, 1 reaction per turn)
- **Include narrative flavor** in trait/action descriptions
- **Reference official stat block format** from SRD creatures

### Step 4: Validate Custom Stat Blocks

Use `reference_manager.py` to check if custom stat blocks follow D&D 5e guidelines:

```bash
python tools/reference_manager.py \
  --validate references/custom/lulu_the_piggy_2/shadow_imp.json
```

**What it checks:**
- AC within expected range for CR
- HP within expected range for CR
- Attack bonus matches proficiency + ability modifier
- Damage output appropriate for CR
- Ability scores use standard array or point buy ranges
- Required fields present (name, type, size, alignment, etc.)

**Output:**

```
[OK] references/custom/lulu_the_piggy_2/shadow_imp.json

Validation Results:
✓ AC (13) appropriate for CR 1 (expected 13-15)
✓ HP (10) appropriate for CR 1 (expected 7-35)
✓ Attack bonus (+5) matches expected for CR 1
✓ Damage (8.5 avg) appropriate for CR 1 (expected 4-8)
✓ All required fields present

Warnings:
⚠ HP (10) is on the low end for CR 1 - consider glass cannon role or increasing to 15+
```

### Step 5: Generate Bestiary

Create a printer-friendly bestiary containing ONLY creatures used in your adventure:

```bash
python tools/reference_manager.py \
  --adventure lulu_the_piggy_2 \
  --bestiary references/bestiary/lulu_the_piggy_2_bestiary.md
```

**Output:** A markdown file with:
- Table of contents
- All SRD creatures mentioned in your adventure (copied from SRD)
- All custom creatures (formatted from JSON)
- Organized by CR for easy lookup
- Printer-friendly formatting

**Example bestiary structure:**

```markdown
# Bestiary: The Brass Contract

**Creatures Used in This Adventure**

## Table of Contents
- [CR 1/8](#cr-18)
- [CR 1](#cr-1)
- [CR 5](#cr-5)

---

## CR 1/8

### Imp (SRD)
*Tiny fiend (devil), lawful evil*

**Armor Class** 13
**Hit Points** 10 (3d4+3)
[... full stat block ...]

---

## CR 1

### Shadow Imp (Custom)
*Tiny fiend (devil), lawful evil*

**Armor Class** 13
**Hit Points** 10 (3d4+3)
[... full stat block ...]

**Based On:** Imp (SRD)
**Modifications:** Added Shadow Blend trait, increased Stealth bonus

---

[... continues for all creatures ...]
```

### Step 6: Use During Sessions

**Session Prep:**
1. Print bestiary or keep it open on tablet
2. Cross-reference with encounter cheat sheets (which list creatures present)
3. Bookmark pages for creatures appearing in today's session

**During Play:**
- Reference stat blocks as needed during combat
- Use traits/actions verbatim or paraphrase
- Track HP on separate combat tracker (don't write on bestiary)

## CR Calculation Reference

When creating custom stat blocks, use these guidelines to determine Challenge Rating:

### CR by Defensive Stats

| CR | AC | HP Range |
|----|----|----|
| 0 | 10-13 | 1-6 |
| 1/8 | 13 | 7-35 |
| 1/4 | 13 | 36-49 |
| 1/2 | 13 | 50-70 |
| 1 | 13 | 71-85 |
| 2 | 13 | 86-100 |
| 3 | 13 | 101-115 |
| 4 | 14 | 116-130 |
| 5 | 15 | 131-145 |

### CR by Offensive Stats

| CR | Attack Bonus | Damage/Round |
|----|----|----|
| 0 | +3 | 0-1 |
| 1/8 | +3 | 2-3 |
| 1/4 | +3 | 4-5 |
| 1/2 | +3 | 6-8 |
| 1 | +3 | 9-14 |
| 2 | +3 | 15-20 |
| 3 | +4 | 21-26 |
| 4 | +5 | 27-32 |
| 5 | +6 | 33-38 |

**Final CR:** Average the defensive CR and offensive CR, then adjust based on:
- **Resistances/Immunities:** Increase effective HP by 50-100%
- **Saving Throw Proficiencies:** +1 to defensive CR
- **Powerful Traits:** May increase offensive CR (e.g., Pack Tactics, Sneak Attack)
- **Legendary/Lair Actions:** +1-3 to CR depending on power

**Example Calculation for Shadow Imp:**

1. **Defensive CR:** AC 13, HP 10 → CR 0-1/8
2. **Offensive CR:** Attack +5, Damage 8.5 → CR 1
3. **Average:** (0 + 1) / 2 = **CR 1/2**
4. **Adjustments:** Fire/poison immunity, cold resistance → Increase defensive CR by 1 step → **Final CR 1**

See D&D 5e Dungeon Master's Guide Chapter 9 for complete rules.

## SRD Content Management

### Downloading SRD Content

**Current Status:** The `reference_manager.py` tool has a placeholder for downloading SRD content. This feature is marked TODO and will be implemented in a future update.

**Manual Workflow:**

1. **Download Open5e API data** or use official SRD JSON files
2. **Place in `references/srd/`** following the folder structure above
3. **Use consistent naming:** lowercase, underscores (e.g., `beholder.json`, `cure_wounds.json`)

**Recommended Sources:**
- Open5e API: https://api.open5e.com/
- D&D Beyond SRD: https://www.dndbeyond.com/sources/basic-rules
- Official SRD (PDF): https://dnd.wizards.com/resources/systems-reference-document

**Legal Note:** Only use content from the official System Reference Document (SRD) released under the Open Gaming License (OGL). Do not include copyrighted content from published adventures or sourcebooks.

### Updating SRD Content

When new SRD updates are released:

1. Download updated JSON files
2. Replace existing files in `references/srd/`
3. Re-run validation on custom stat blocks to check for conflicts
4. Regenerate bestiaries to include updated stat blocks

## Best Practices

### Creating Custom Stat Blocks

**DO:**
- Base on similar SRD creatures when possible
- Document modifications in `based_on` and `modifications` fields
- Validate against CR guidelines before finalizing
- Use narrative flavor in trait descriptions
- Test in playtests to verify balance

**DON'T:**
- Copy entire stat blocks from copyrighted sources (use SRD only)
- Create overpowered creatures without playtesting
- Use vague trait descriptions (be specific about mechanics)
- Forget to include damage types (fire, slashing, etc.)
- Ignore action economy (too many bonus actions/reactions)

### Organizing References

**By Adventure:**
- Keep custom stat blocks in adventure-specific folders
- Generate separate bestiaries per adventure
- Re-use well-balanced custom creatures across adventures by copying JSON

**By Campaign:**
- Create campaign-wide custom creature library
- Reference from multiple adventures
- Track which creatures have been encountered by players (avoid repetition)

### Version Control

When updating custom stat blocks:

1. **Document changes** in git commit messages
2. **Re-run validation** after modifications
3. **Regenerate bestiary** to reflect changes
4. **Notify DM** if changes affect upcoming sessions
5. **Playtest changes** before using in actual sessions

## Troubleshooting

**Problem:** Scan report shows creature not in SRD, but it should be

- **Solution:** Check spelling and capitalization. Scan looks for exact matches. Common issues: "Hell Hound" vs "Hell hound", "Imp" vs "imp".

**Problem:** Validation fails with AC/HP out of range

- **Solution:** Adjust AC/HP to match CR guidelines or change creature's CR. Remember resistances/immunities affect effective HP.

**Problem:** Bestiary generation includes too many creatures

- **Solution:** Scan report includes creatures mentioned in backstory/flavor text. Manually edit JSON to exclude creatures that don't appear in actual encounters.

**Problem:** Custom stat block JSON format errors

- **Solution:** Validate JSON syntax using online JSON validator. Ensure all fields use correct types (numbers as numbers, not strings).

**Problem:** Reference manager can't find SRD files

- **Solution:** Verify SRD files are in `references/srd/creatures/` and `references/srd/spells/`. Use lowercase filenames with underscores (e.g., `hell_hound.json`).

## Integration with Adventure Creation

### Step 8: Reference Integration (Lead Game Designer Agent)

When using the Lead Game Designer Agent, reference integration happens automatically in Step 8:

1. **Agent scans adventure documents** using `reference_manager.py --scan`
2. **Agent presents scan report** to user for review
3. **User decides** which custom stat blocks to create vs. use SRD creatures
4. **Agent creates custom stat blocks** based on user guidance
5. **Agent validates custom stat blocks** using `reference_manager.py --validate`
6. **Agent generates bestiary** using `reference_manager.py --bestiary`
7. **User reviews bestiary** for final approval

See [.claude/agents/lead_game_designer_agent/README.md](../.claude/agents/lead_game_designer_agent/README.md) Step 8 for detailed workflow.

### Manual Workflow (Without Agent)

If creating references manually:

1. Read through Factions, Locations, and Props documents
2. Note every creature mentioned
3. Note every spell mentioned
4. Manually create scan report listing all references
5. Create custom stat block JSON files for non-SRD creatures
6. Manually format bestiary markdown file
7. Cross-reference with encounter cheat sheets to ensure all creatures have stat blocks

This process is time-consuming - using `reference_manager.py` automates most of it.

## Advanced Features

### Linking References to Encounters

Add `creatures_present` field to encounter cheat sheets:

```markdown
## Creatures Present
- **Shadow Imp** (2) - See Bestiary p.3, CR 1
- **Hell Hound** (1) - See Bestiary p.5, CR 3
```

This enables quick cross-referencing during sessions.

### Spell Reference Cards

For spellcasting NPCs, create spell reference cards similar to NPC cards:

```markdown
### Ms. Reed (Spellcaster)

**Spell Save DC:** 14
**Spell Attack Bonus:** +6

**Cantrips:** Fire Bolt, Prestidigitation, Thaumaturgy
**1st Level (4 slots):** Detect Magic, Identify, Shield
**2nd Level (3 slots):** Scorching Ray, Invisibility
**3rd Level (2 slots):** Fireball, Counterspell

**Prepared Spells:** See Bestiary p.12-15 for full descriptions
```

### Variant Stat Blocks

Create multiple versions of the same creature for different encounters:

- `shadow_imp.json` (basic version)
- `shadow_imp_elite.json` (higher CR for boss encounter)
- `shadow_imp_swarm.json` (swarm mechanics for horde encounter)

Reference appropriate version in encounter cheat sheets.

## Example: "The Brass Contract" References

See [lulu_the_piggy_2/references/](../lulu_the_piggy_2/references/) (when created) for a complete example including:
- Scan report showing 8 creatures and 5 spells
- Custom stat blocks for Shadow Imp, Heartbreak (Devil Negotiator), Infernal Contract Elemental
- Generated bestiary with 12 total creatures (3 custom, 9 SRD)

This example demonstrates best practices for reference management in a multi-faction adventure.

## Future Enhancements

Planned features for `reference_manager.py`:

- **Automatic SRD download** from Open5e API (currently TODO)
- **Stat block validation** with detailed CR calculation (currently TODO)
- **Encounter balancing calculator** based on party level + creatures present
- **Random encounter generation** using available creatures
- **Cross-adventure creature search** ("which adventures use Hell Hounds?")

See [IMPLEMENTATION_STATUS.md](../IMPLEMENTATION_STATUS.md) for current implementation status.
