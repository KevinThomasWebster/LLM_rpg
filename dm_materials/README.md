# DM Materials Guide

**Quick reference materials for running D&D adventure sessions at the table.**

## Purpose

The `dm_materials/` folder contains distilled, printer-friendly resources designed for actual play at the table. While the main adventure files (Factions, Locations, Props) are comprehensive world-building documents, these materials are optimized for:

- **Quick lookup during sessions** (1-page cheat sheets)
- **Combat management** (stat blocks at a glance)
- **Tracking player progress** (clue discovery, faction relationships)
- **Visual aids** (faction diagrams, relationship maps)

## Folder Structure

```
dm_materials/
├── session_cheatsheets/       # 1-page encounter quick references
│   ├── 01_encounter_name.md
│   ├── 02_encounter_name.md
│   └── ...
├── npc_cards/                 # NPC stat blocks with roleplay guides
│   ├── 01_major_npcs.md
│   ├── 02_minor_npcs.md
│   └── ...
├── clue_tracker.md            # Session tracking for secret discovery
├── faction_diagram.md         # Visual faction relationship map
└── README.md                  # This file
```

## How to Use Each Resource

### Session Cheat Sheets

**Purpose:** Run encounters without flipping between multiple documents.

**When to use:**
- Print before session
- Keep next to DM screen
- Reference during encounter execution

**What's included:**
- At-a-glance summary (setting, present NPCs, available clues)
- Stage-by-stage progression (Hook → Complication → Escalation → Climax)
- Quick NPC stats (AC, HP, key abilities)
- Secrets & clues available in this encounter
- Environmental interactivity (things players can use/investigate)
- Win conditions for all factions
- Fallback options if players get stuck
- Pacing reminders

**Example usage:**

> DM reads Stage 1 (The Hook) aloud to set the scene. Players decide to investigate the filing cabinet. DM checks "Environmental Interactivity" section: "Filing cabinet (Investigation DC 12) - Contains encrypted journal, clue to Secret #2". Player rolls 15, DM reveals the clue from "Secrets & Clues Available" section.

**Tips:**
- Highlight sections you expect players to reach
- Add sticky notes with custom adjustments
- Cross-reference with full Location document for improvisation needs

### NPC Cards

**Purpose:** Roleplay NPCs consistently and run combat encounters smoothly.

**When to use:**
- During social encounters (reference roleplay guide)
- During combat (reference stats and tactics)
- When NPCs appear across multiple encounters (maintain consistency)

**What's included:**

Per NPC:
- **Quick Stats:** AC, HP, Speed, Initiative modifier
- **Combat Actions:** Attack bonuses, damage dice, special abilities
- **Roleplay Guide:** Motivation, voice/mannerisms, secrets they know
- **Faction Context:** Loyalty, betrayal conditions, faction goals
- **Combat Tactics:** Opening move, preferred strategy, retreat conditions
- **Revelations & Secrets:** What they can reveal and under what conditions

**Example usage:**

> Players attempt to intimidate Ms. Reed into revealing information about the 4th floor. DM checks "Revelations & Secrets" section: "Reveals 4th floor containment breach only if: threatened with exposure to superiors OR players demonstrate they already know about infernal contract." Player mentions finding contract in previous scene - DM has Ms. Reed break down and reveal the truth.

**Tips:**
- Note which secrets have been revealed during session
- Track NPC HP on combat tracker, not on the card itself
- Use voice/mannerism notes to stay in character

### Clue Tracker

**Purpose:** Track which secrets players have discovered during sessions.

**When to use:**
- After each session (update discovery status)
- During session planning (identify which secrets are still hidden)
- When players are stuck (check which clues they've missed)

**What's included:**
- **Core Secrets Status:** All secrets with discovery status and notes
- **Quick Lookup by Location:** Which secrets are accessible in each location
- **Quick Lookup by NPC:** Which secrets each NPC knows
- **Clue Interconnections:** How secrets relate to each other

**Example usage:**

> End of session 2: Players discovered Secret #1 (filing cabinet) and Secret #3 (Ms. Reed confession) but missed Secret #2 (encrypted journal requires Arcana check). DM updates tracker, notes they haven't attempted Arcana checks yet. Plans to have Rem offer to decode journal next session as a hook.

**Tips:**
- Update during session breaks or at end of session
- Add player theories to "Notes" column (even wrong theories help you)
- Use interconnections to plan clue chains across sessions

### Faction Diagram

**Purpose:** Visualize complex faction relationships at a glance.

**When to use:**
- Session planning (anticipate faction reactions)
- During session (determine NPC loyalties on the fly)
- When players manipulate factions (track changing relationships)

**What's included:**
- **Mermaid Diagram:** Visual graph of faction relationships
- **Relationship Details:** What each connection means narratively
- **Player Exploitation Strategies:** How players can use faction conflicts
- **Timeline Conflicts:** When factions' proactive goals clash

**Example usage:**

> Players convince Rem to betray the Shadow Court. DM checks faction diagram: "Rem (Independent) has strained relationship with Shadow Court but cooperative relationship with Corporate (Heartbreak's faction). Betraying Court strengthens Corporate ties but makes Rem a target." DM notes this affects future encounters - Corporate NPCs will be friendlier, Court NPCs hostile.

**Tips:**
- Print diagram for visual reference
- Update relationships as players change the world
- Use timeline conflicts to create urgency

## Workflow: Preparing for a Session

### 1-2 Days Before Session (15-30 minutes)

1. **Review session cheat sheets** for planned encounters
2. **Check clue tracker** to see what secrets players have discovered
3. **Review NPC cards** for NPCs likely to appear
4. **Update faction diagram** if relationships changed in previous session
5. **Read full Location documents** for encounters you're planning (for improv context)

### Day of Session (5-10 minutes)

1. **Print session cheat sheets** for planned encounters
2. **Print NPC cards** for NPCs appearing this session
3. **Bring clue tracker** to mark new discoveries
4. **Optional:** Print faction diagram if faction politics are central to session

### During Session

- **Use session cheat sheets** as primary reference
- **Reference NPC cards** for roleplay consistency and combat stats
- **Update clue tracker** when secrets are discovered
- **Improvise from memory** for minor details, check full documents during breaks

### After Session (5-10 minutes)

1. **Update clue tracker** with all new discoveries
2. **Note NPC relationship changes** on faction diagram
3. **Review what players bypassed** - adjust future cheat sheets if needed
4. **Update any custom notes** on printed materials for continuity

## Tips for Table Use

### Print-Friendly Formatting

All DM materials are designed for black-and-white printing:
- Use markdown headings for visual hierarchy
- Bold key stats/DCs for easy scanning
- Bullet points for quick reading
- Avoid images/colors (use faction diagram text if no printer)

### Digital Use

If using tablet/laptop at table:
- Open multiple markdown files in tabs (cheat sheet + NPC cards + clue tracker)
- Use split-screen view for cheat sheet + clue tracker
- Enable markdown preview mode for formatting

### Hybrid Approach

Many DMs prefer:
- **Printed:** Session cheat sheets (frequent reference, no scrolling)
- **Digital:** Clue tracker (easy to update), NPC cards (searchable)
- **Visual Aid:** Faction diagram on separate monitor/tablet for players to see

## Creating Custom DM Materials

### For New Adventures

The Lead Game Designer Agent automatically generates DM materials in Step 6 of adventure creation. See [.claude/agents/lead_game_designer_agent/README.md](../.claude/agents/lead_game_designer_agent/README.md) for details.

### For Existing Adventures

Use the templates in `templates/` folder:

1. **Encounter Cheat Sheet:** Copy `templates/encounter_cheatsheet.md` and fill in from Location document
2. **NPC Card:** Copy `templates/npc_card.md` and fill in from Faction document
3. **Clue Tracker:** Copy `templates/clue_tracker.md` and list all secrets from `secrets_and_clues.md`
4. **Faction Diagram:** Copy `templates/faction_diagram_template.md` and create Mermaid diagram from Faction document

### Manual Workflow

If creating without LLM assistance:

1. Read through the full adventure documents (Factions, Locations, Props)
2. Extract key information for each encounter:
   - Which NPCs appear?
   - What can players investigate?
   - What secrets are accessible here?
   - What are the stage progressions?
3. Fill in templates with extracted information
4. Cross-reference with `secrets_and_clues.md` to ensure all clues are represented
5. Validate NPC stats match Faction document

See [.claude/agents/lead_game_designer_agent/ADDENDUM.md](../.claude/agents/lead_game_designer_agent/ADDENDUM.md) for detailed manual workflow.

## Quality Checklist

Before running a session, verify your DM materials:

- [ ] **Session cheat sheet exists** for each planned encounter
- [ ] **All NPCs have stat blocks** in npc_cards/
- [ ] **Clue tracker includes all secrets** from secrets_and_clues.md
- [ ] **Faction diagram reflects current relationships** (if factions changed in previous sessions)
- [ ] **Quick stats are accurate** (match full Faction/Location documents)
- [ ] **Win conditions are clear** for all factions in encounter
- [ ] **Fallback options exist** if players get stuck
- [ ] **Environmental interactivity is listed** for all major set pieces

## Common Issues

**Problem:** Session cheat sheet too long (>2 pages)

- **Solution:** Focus on stage progressions and key stats only. Link to full Location document for deep improvisation needs.

**Problem:** NPC card missing key ability

- **Solution:** Cross-reference with Faction document. If ability is critical to encounter, add it to card. Update template for consistency.

**Problem:** Players discovered secret not on clue tracker

- **Solution:** Add custom secret to tracker immediately. Update main `secrets_and_clues.md` after session.

**Problem:** Faction diagram outdated after player actions

- **Solution:** Draw updated relationships on printed diagram during session. Digitize changes after session. Consider creating session-specific versions.

**Problem:** Too much to print for long session

- **Solution:** Print only first 2-3 encounters. Use digital materials for later encounters. Print additional sheets during session break if needed.

## Integration with Other Systems

### VTT (Virtual Tabletop) Use

- Import NPC stat blocks into Roll20/Foundry character sheets
- Share faction diagram image with players via VTT
- Use clue tracker in shared Google Doc for player visibility

### Note-Taking Apps

- Copy DM materials into Notion/Obsidian for linking
- Use clue tracker as checklist in to-do app (Todoist, etc.)
- Embed session cheat sheets in session planning documents

### Session Recaps

- Reference clue tracker to write "what players discovered" recaps
- Use faction diagram to explain relationship changes to players
- Link to specific NPC cards when players ask "who was that person again?"

## Example: Running "The First Signal" Encounter

See [lulu_the_piggy_2/dm_materials/](../lulu_the_piggy_2/dm_materials/) for a complete example of all DM materials for a multi-stage encounter.

**What's included:**
- Session cheat sheet: `session_cheatsheets/01_the_first_signal.md`
- NPC cards: `npc_cards/01_major_npcs.md`
- Clue tracker: `clue_tracker.md`
- Faction diagram: `faction_diagram.md`

Study this example to understand how materials work together during actual play.
