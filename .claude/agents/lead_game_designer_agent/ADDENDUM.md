# Lead Game Designer Agent - Tool Integration Addendum

## Using Python Utilities

### After Step 2 (Factions) and Step 3 (Locations)

**Reference Manager Integration:**
```bash
# Scan adventure for creature/spell mentions
python tools/reference_manager.py --scan-adventure {adventure_name}

# Review the report of what was found
# Create custom stat blocks for creatures not in SRD
# Request validation from Reference Integration Agent
```

**Manual Process (if tool not available):**
1. Read through `01_Factions.md` and `02_Locations.md`
2. List all creature mentions
3. Categorize as official SRD or custom
4. Create stat blocks for custom creatures in `dm_materials/npc_cards/`
5. Request Reference Integration Agent validation

### After Step 6 (DM Materials)

**Cheat Sheet Generator (when available):**
```bash
# Auto-generate all DM materials
python tools/cheatsheet_generator.py --generate-all {adventure_name}

# Generate specific materials
python tools/cheatsheet_generator.py --encounter "{ENCOUNTER_NAME}"
python tools/cheatsheet_generator.py --npc-cards --faction "{FACTION_NAME}"
python tools/cheatsheet_generator.py --faction-diagram --format mermaid
```

**Manual Process (current):**
1. Use templates from `templates/` folder
2. Copy template to `dm_materials/` appropriate subfolder
3. Fill in placeholders with data from consolidated documents
4. Example workflow:
   - Copy `templates/encounter_cheatsheet.md`
   - Extract encounter data from `02_Locations.md`
   - Fill in all {PLACEHOLDER} values
   - Save to `dm_materials/session_cheatsheets/{encounter_name}.md`

### After Step 7 (Content Validation)

**Content Validator (when available):**
```bash
# Run automated validation
python tools/content_validator.py --adventure {adventure_name}

# Review report
# Fix flagged issues
# Re-run until all checks pass
```

**Manual Process (current):**
1. Create checklist from `templates/content_validation_checklist.md`
2. Manually verify each item:
   - Check secrets have findable clues
   - Check NPCs have stat blocks
   - Check faction timelines complete
   - Check all references resolved
3. Document results
4. Fix any gaps found

## Integration with Other Agents

### With Reference Integration Agent

**After 01_Factions.md completed:**
- Request: "Reference Integration Agent, please scan 01_Factions.md for creature and spell mentions"
- Receive report of official vs. custom content
- Create stat blocks for custom NPCs
- Request validation: "Please validate the stat blocks in dm_materials/npc_cards/01_major_npcs.md"

**After 02_Locations.md completed:**
- Request: "Reference Integration Agent, please update scan to include 02_Locations.md"
- Review updated mentions report
- Create/update bestiary: `references/monsters_used.md`

### With Play Test Agents

**Before playtesting begins:**
- Ensure `player_personas.md` is complete
- Provide Play Test DM Agent with encounter cheat sheets
- Provide Play Test Grader Agent with validation criteria

## Template Usage Guide

### Creating Encounter Cheat Sheets

**Source:** `templates/encounter_cheatsheet.md`
**Destination:** `dm_materials/session_cheatsheets/{encounter_name}.md`

**Data Extraction Process:**
1. Find encounter in `02_Locations.md`
2. Extract:
   - Location name and description
   - Factions present
   - Key NPCs (with stat block references)
   - 4-stage structure (Hook, Complication, Escalation, Climax)
   - Secrets and clues available
   - Win conditions for each faction
   - Environmental interactivity elements
3. Fill template placeholders
4. Add improvisation hooks from playtesting (if available)

### Creating NPC Cards

**Source:** `templates/npc_card.md`
**Destination:** `dm_materials/npc_cards/{category}_npcs.md`

**Data Extraction Process:**
1. Find NPC in `01_Factions.md`
2. Extract:
   - Stat block information
   - Roleplay details (voice, mannerisms, motivation)
   - Faction context
   - Combat tactics
   - Secrets they know
3. Fill template placeholders
4. Request Reference Integration Agent validation if custom creature

### Creating Clue Tracker

**Source:** `templates/clue_tracker.md`
**Destination:** `dm_materials/clue_tracker.md`

**Data Extraction Process:**
1. Use `secrets_and_clues.md` as primary source
2. For each secret:
   - List all associated clues
   - Note location where found
   - Note discovery method and DC
   - Track revelation progress boxes
3. Create quick lookups by location and NPC
4. Include session notes section

### Creating Faction Diagram

**Destination:** `dm_materials/faction_diagram.md`

**Creation Process:**
1. List all factions from `01_Factions.md`
2. Identify relationships:
   - Allied
   - Hostile
   - Neutral
   - Complicated
3. Create Mermaid diagram or text representation
4. Include faction goals summary
5. Note player exploitation opportunities

## File Organization Best Practices

### dm_materials/ Structure
```
dm_materials/
├── session_cheatsheets/
│   ├── 01_opening_encounter.md
│   ├── 02_next_encounter.md
│   └── ...
├── npc_cards/
│   ├── 01_major_npcs.md (faction leaders, key antagonists)
│   ├── 02_minor_npcs.md (supporting characters)
│   └── 03_monsters.md (recurring creatures)
├── faction_diagram.md
├── clue_tracker.md
└── combat_tracker_template.md
```

### references/ Structure
```
references/
├── srd_5e_2024/ (if using reference_manager.py)
│   ├── monsters/
│   ├── spells/
│   └── index.json
├── monsters_used.md
├── spells_used.md
└── reference_sources.md (attribution)
```

## Quality Checklist

Before presenting DM materials (Step 6):
- [ ] All encounters have cheat sheets
- [ ] All major NPCs have cards
- [ ] Faction diagram shows all relationships
- [ ] Clue tracker lists all secrets
- [ ] Stat blocks validated (or flagged for validation)
- [ ] All templates filled completely (no {PLACEHOLDERS} remaining)
- [ ] Cross-references verified (e.g., NPC card references match encounter cheat sheets)

Before content validation (Step 7):
- [ ] Every secret in `secrets_and_clues.md` has at least 2 clues
- [ ] Every clue has a findable location in `02_Locations.md`
- [ ] Every faction has a complete timeline with 3+ proactive actions
- [ ] Every major NPC has a stat block or reference
- [ ] All creatures mentioned have stat blocks or placeholders
- [ ] All spells mentioned have descriptions or references

---

**Remember:** Your goal is thoroughness and quality. Take time to create comprehensive DM materials that make session execution effortless.
