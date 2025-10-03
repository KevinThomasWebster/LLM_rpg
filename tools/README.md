# D&D Adventure Creation Tools

Python utilities for enhancing the adventure creation and playtesting workflow.

## Installation

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Tools Overview

### 1. Dice Roller (`dice_roller.py`)

Reproducible dice rolling with statistical tracking for playtests.

#### Features
- Proper random number generation with seeding
- Support for advantage/disadvantage
- Statistical analysis (mean, critical rate, bias detection)
- JSON export for playtest data

#### Usage

```bash
# Basic roll
python dice_roller.py --roll "1d20+5"

# Roll with advantage
python dice_roller.py --roll "1d20" --advantage

# Roll with seed for reproducibility
python dice_roller.py --roll "1d20+3" --seed 12345

# Track roll with metadata
python dice_roller.py --roll "1d20+5" \
  --character "Alex" \
  --action "Perception check" \
  --round 3 \
  --log playtest_1_rolls.json

# Show statistics from log
python dice_roller.py --import playtest_1_rolls.json --stats

# Run self-test
python dice_roller.py --test
```

#### Integration with Playtesting

**For Play Test DM Agent:**

1. Before playtest, choose seed: `playtest_number × 1000`
2. For each roll, use: `python dice_roller.py --roll "XdY+Z" --seed {SEED} --log playtest_N_rolls.json`
3. After playtest, get stats: `python dice_roller.py --import playtest_N_rolls.json --stats`
4. Include roll data in playtest JSON

---

### 2. Playtest Analyzer (`playtest_analyzer.py`)

Extract quantitative metrics and generate reports from playtest data.

#### Features
- Calculate spotlight distribution (% actions per character)
- Clue discovery rate analysis
- Win condition frequency tracking
- Dice statistics aggregation
- Automated balance issue detection
- Markdown report generation

#### Usage

```bash
# Analyze encounter (auto-finds playtest directory)
python playtest_analyzer.py --encounter "Design_Studio"

# Specify custom playtest directory
python playtest_analyzer.py \
  --encounter "Design_Studio" \
  --playtest-dir "lulu_the_piggy/play_tests/Design_Studio"

# Generate report to file
python playtest_analyzer.py \
  --encounter "Design_Studio" \
  --output analysis_report.md

# Analyze specific metric
python playtest_analyzer.py \
  --encounter "Design_Studio" \
  --metric spotlight

# Run self-test
python playtest_analyzer.py --test
```

#### Required Playtest Data Format

Place JSON files in `play_tests/{ENCOUNTER_NAME}/playtest_N_data.json`:

```json
{
  "playtest_id": "playtest_1",
  "encounter": "Design_Studio",
  "character_actions": [
    {
      "round": 1,
      "character": "Alex",
      "action_type": "investigate",
      "skill_check": "Perception",
      "roll": 15,
      "modifier": 3,
      "total": 18,
      "success": true
    }
  ],
  "spotlight_distribution": {"Alex": 35, "Casey": 40, "Ben": 25},
  "clues_discovered": ["Rem's Journal", "Facility Map"],
  "win_condition": "escaped_with_journal"
}
```

#### Sample Report Output

```markdown
# Playtest Analysis: Design_Studio

**Total Playtests:** 10

## Spotlight Distribution
- **Casey:** 40.2% (Target: ~33.3%) ⚠️
- **Alex:** 35.1% (Target: ~33.3%) ✅
- **Ben:** 24.7% (Target: ~33.3%) ⚠️

## Clue Discovery Rate
- **Rem's Journal:** 100% (10/10) ✅
- **Facility Map:** 70% (7/10) ✅
- **Hidden Messages:** 30% (3/10) ❌

## Recommendations
1. **Increase Ben's spotlight:** Add skill check suited to their abilities
2. **Make 'Hidden Messages' more discoverable:** Currently 30% discovery rate
```

---

### 3. Reference Manager (`reference_manager.py`)

**Status:** 🚧 To be implemented

Download and integrate D&D 2024 5e SRD content.

**Planned Features:**
- Download SRD from official sources
- Index monsters, spells, items
- Scan adventure documents for references
- Generate adventure-specific bestiary
- Validate custom stat blocks

---

### 4. Cheat Sheet Generator (`cheatsheet_generator.py`)

**Status:** 🚧 To be implemented

Auto-generate DM session materials from consolidated adventure documents.

**Planned Features:**
- Parse consolidated markdown files
- Extract encounter data
- Generate session cheat sheets
- Create NPC stat cards
- Generate faction diagrams

---

## Workflow Integration

### For Play Test DM Agent

```bash
# 1. Before playtest - Set up dice roller with seed
SEED=$((PLAYTEST_NUM * 1000))

# 2. During playtest - Roll dice and track
python tools/dice_roller.py --roll "1d20+5" --seed $SEED \
  --character "Alex" --action "Perception" --round 1 \
  --log play_tests/Design_Studio/playtest_1_rolls.json

# 3. After playtest - Create data JSON
# (Manual or scripted from playtest narrative)

# 4. Get roll statistics
python tools/dice_roller.py \
  --import play_tests/Design_Studio/playtest_1_rolls.json \
  --stats
```

### For Play Test Grader Agent

```bash
# After N playtests (e.g., 5-10), analyze aggregate data
python tools/playtest_analyzer.py \
  --encounter "Design_Studio" \
  --output play_tests/Design_Studio/analysis_report.md

# Check for balance issues
python tools/playtest_analyzer.py \
  --encounter "Design_Studio" \
  --metric all
```

### For Lead Game Designer Agent

```bash
# After creating 01_Factions.md, 02_Locations.md
# (Reference Manager - to be implemented)
python tools/reference_manager.py \
  --scan-adventure lulu_the_piggy \
  --generate-bestiary

# Generate DM materials
# (Cheat Sheet Generator - to be implemented)
python tools/cheatsheet_generator.py \
  --generate-all lulu_the_piggy
```

---

## Data Formats

### Playtest Data JSON Schema

See `templates/schemas/playtest_data_schema.json` for complete schema.

**Minimal Required Fields:**
```json
{
  "playtest_id": "string",
  "encounter": "string",
  "character_actions": [
    {
      "character": "string",
      "roll": "number (1-20)",
      "success": "boolean"
    }
  ],
  "clues_discovered": ["string"],
  "win_condition": "string"
}
```

### Dice Roll Log Format

```json
{
  "seed": 12345,
  "timestamp": "2025-10-01T10:00:00",
  "rolls": [
    {
      "timestamp": "2025-10-01T10:05:00",
      "notation": "1d20+5",
      "rolls": [15],
      "total": 20,
      "character": "Alex",
      "action": "Perception check",
      "round": 1,
      "critical_hit": true
    }
  ],
  "statistics": {
    "total_rolls": 45,
    "mean": 10.8,
    "critical_hit_rate": 6.7
  }
}
```

---

## Troubleshooting

### ImportError: No module named 'X'
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### FileNotFoundError: playtest directory not found
```bash
# Ensure correct path structure
# Expected: play_tests/{ENCOUNTER_NAME}/playtest_N_data.json

# Or specify custom path
python playtest_analyzer.py --encounter "Name" --playtest-dir "custom/path"
```

### Statistics seem wrong
```bash
# Verify JSON data format
# Run self-test to check calculations
python playtest_analyzer.py --test
python dice_roller.py --test
```

---

## Development Roadmap

### ✅ Phase 1 (Complete)
- [x] Dice Roller with statistical tracking
- [x] Playtest Analyzer with report generation
- [x] Documentation and usage examples

### 🚧 Phase 2 (In Progress)
- [ ] Reference Manager (SRD integration)
- [ ] Cheat Sheet Generator
- [ ] Content Validator

### 📋 Phase 3 (Planned)
- [ ] Batch Playtest Runner
- [ ] Chart generation (matplotlib)
- [ ] PDF export functionality
- [ ] Web dashboard (optional)

---

## Contributing

When creating new tools:

1. **Follow the pattern:**
   - `--test` flag for self-testing
   - `--help` for documentation
   - JSON input/output for interoperability

2. **Document thoroughly:**
   - Docstrings for all functions
   - Usage examples in README
   - Sample data for testing

3. **Maintain compatibility:**
   - Work with existing file structure
   - Use consistent data formats
   - Integrate with agent workflow

---

## Support

For issues or questions:
1. Check this README
2. Run self-tests: `python {tool}.py --test`
3. Review sample data in `templates/`
4. Consult main `feedback.md` for system overview

---

*Last updated: October 2025*
