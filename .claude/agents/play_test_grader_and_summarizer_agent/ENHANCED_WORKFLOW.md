# Play Test Grader Agent - Enhanced Workflow with Quantitative Analysis

## NEW: Quantitative Analysis Integration

After each playtest, run `playtest_analyzer.py` to generate metrics alongside qualitative assessment.

### After Each Individual Playtest

**1. Run Analyzer on JSON Data:**
```bash
python tools/playtest_analyzer.py \
  --encounter "{ENCOUNTER_NAME}" \
  --playtest-dir "play_tests/{ENCOUNTER_NAME}"
```

**2. Include Quantitative Metrics in Grading:**

Add this section to each playtest grading:

```markdown
## Quantitative Metrics (Playtest {N})

### Spotlight Distribution
- Alex: 35% (8/23 actions)
- Casey: 39% (9/23 actions)
- Ben: 26% (6/23 actions)

**Analysis:** Ben slightly underpowered (target: ~33%). Recommend adding social encounter opportunity in Stage 2.

### Dice Statistics
- Mean d20 roll: 11.2 (expected: 10.5) ✅
- Critical success rate: 8.7% (expected: 5%) ⚠️ Slightly lucky
- Player success rate: 72% (appropriate for difficulty)

### Clue Discovery
- Primary clues: 2/2 found (100%) ✅
- Secondary clues: 1/2 found (50%)
- Tertiary clues: 0/1 found (0%) ❌ Too obscure
```

**3. Cross-Reference with Qualitative Assessment:**
- Do the numbers support your qualitative impressions?
- Flag discrepancies (e.g., "felt like Ben did a lot, but only 26% actions")
- Use data to validate or challenge assumptions

### After Multiple Playtests (5-10 Runs)

**1. Generate Aggregate Analysis:**
```bash
python tools/playtest_analyzer.py \
  --encounter "{ENCOUNTER_NAME}" \
  --output play_tests/{ENCOUNTER_NAME}/analysis_report.md
```

**2. Create Summary with Visualizations:**

```markdown
# Playtest Summary: {ENCOUNTER_NAME} (10 runs)

## Aggregate Spotlight Distribution
- **Casey:** 40.2% avg (Target: ~33.3%) ⚠️ Slightly high
- **Alex:** 35.1% avg (Target: ~33.3%) ✅
- **Ben:** 24.7% avg (Target: ~33.3%) ❌ Consistently underpowered

**Trend:** Ben's spotlight decreased over runs 1-5, stabilized runs 6-10.

## Aggregate Clue Discovery Rates
- **Rem's Journal:** 100% (10/10) ✅
- **Facility Map:** 70% (7/10) ✅
- **Hidden Messages:** 30% (3/10) ❌ Too difficult to find

## Aggregate Dice Statistics
- Mean d20 across all runs: 10.4 ✅
- Success rate: 68% avg ✅
- Chi-squared p-value: 0.42 (no bias detected) ✅

## Win Condition Frequency
- Escaped with journal: 7 times (70%)
- Escaped without journal: 2 times (20%)
- Captured by security: 1 time (10%)
```

**3. Provide Actionable Recommendations:**

```markdown
## Recommendations for {ENCOUNTER_NAME}

### High Priority
1. **Ben's Spotlight (24.7% avg across 10 runs):**
   - Add Investigation check opportunity in Stage 2
   - Create environmental puzzle requiring Athletics (Ben's strength)
   - Give Ben unique emotional connection to Rem (roleplay moment)

2. **Hidden Messages Clue (30% discovery rate):**
   - Make more prominent (currently DC 14, recommend DC 12)
   - Add Rem pointing gesture toward desk
   - Include in Empathy Lock puzzle as additional hint

### Medium Priority
3. **Casey Overrepresentation (40.2% avg):**
   - Not critical, but monitor
   - Consider if hack checks can sometimes be group efforts
   - Ensure other characters have tech-free options

### Low Priority
4. **Stage 3 Pacing (4.2 rounds avg, target 3-5):**
   - Currently well-paced
   - Continue monitoring in future iterations
```

## Enhanced Grading Rubric

### Immersion (Qualitative + Quantitative)

**Qualitative Assessment (1-5):**
- Quality of sensory descriptions
- NPC voice consistency
- Atmosphere creation
- Player engagement

**Quantitative Metrics:**
- Number of environmental interactions
- Improvised content count (higher = richer world)
- Player questions/investigations (engagement proxy)

**Example:**
```markdown
### Immersion: 5/5
**Qualitative:** Excellent sensory details (ozone smell, cold light, pneumatic whoosh). Rem's desperation palpable. Empathy Lock puzzle emotionally resonant.

**Quantitative:**
- Environmental interactions: 6 (pneumatic tubes, workstations, recycling bins, desks, posters, Blue Ribbon Lulu)
- Improvised content: 3 elements (bot personality, tube diversion, Rem's reaction)
- Player investigations: 8 specific questions asked

**Conclusion:** Highly immersive. Players explored world actively.
```

### Character Spotlight (Quantitative Focus)

**Quantitative Metrics (Primary):**
- Action count per character
- Percentage distribution
- Success rate per character
- Critical moment contributions

**Qualitative Context:**
- Quality of contributions (not just quantity)
- Character development moments
- Unique ability usage

**Example:**
```markdown
### Character Spotlight: 3/5
**Quantitative:**
- Alex: 35% (8 actions) - 7 successful
- Casey: 39% (9 actions) - 8 successful
- Ben: 26% (6 actions) - 4 successful

**Qualitative Context:**
- Alex had key Insight moment (noticing Rem)
- Casey dominated technical challenges (3 hack checks)
- Ben's Athletics check was critical in Climax, but underutilized in Stages 1-3

**Issue:** Ben below target threshold (33%). Needs more Stage 1-2 opportunities.
```

### Clue/Prop Interaction (Trackable Data)

**Quantitative Metrics:**
- Clues discovered vs. available
- Props used vs. available
- Discovery method breakdown (investigation vs. NPC vs. environmental)

**Qualitative Assessment:**
- Clever clue connections
- Creative prop usage
- Missed opportunities analysis

**Example:**
```markdown
### Clue/Prop Interaction: 4/5
**Quantitative:**
- Clues found: 3/4 (75%)
  - Rem's Journal: Yes (Empathy Lock puzzle)
  - Facility Map: Yes (hack)
  - Hidden Messages: Yes (DC 14 Investigation)
  - Alex's Emails: No (missed - didn't access tablet further)
- Props used: 3/5 (60%)
  - Empathy Lock: Yes (puzzle solved)
  - Pneumatic Tubes: Yes (creative diversion)
  - Workstations: Yes (hacking)
  - Blue Ribbon Lulu: No (not interacted with)
  - Cleaning Solution: No (Rem used, but players didn't)

**Qualitative:**
- Creative pneumatic tube usage (not in original design)
- Empathy Lock solution was emotionally engaging
- Missed opportunity: Blue Ribbon Lulu could provide additional info

**Recommendation:** Make Blue Ribbon Lulu more obviously interactive.
```

### Path to Victory (Complexity Scoring)

**Quantitative Metrics:**
- Number of meaningful decisions made
- Alternative approaches attempted
- Faction interactions count
- Creativity score (1-5, based on improvisation needed)

**Qualitative Assessment:**
- Was it straightforward combat? (Low score)
- Required social/puzzle/stealth? (Medium score)
- Required creative synthesis of clues/props/faction manipulation? (High score)

**Example:**
```markdown
### Path to Victory: 5/5
**Quantitative:**
- Meaningful decisions: 8
  - React to Rem or ignore?
  - Confront bot or stealth?
  - Solve puzzle or brute force?
  - Fight Lulus or delay/evade?
  - Use pneumatic tubes diversion?
  - Trust Rem fully or verify?
  - Escape route choice
  - What to do with journal?

- Faction interactions: 2 (Architects, Echoes)
- Creativity score: 5/5 (pneumatic tube diversion improvised)

**Qualitative:**
- Not straightforward combat (only delayed Lulus, didn't fight to death)
- Required puzzle-solving (Empathy Lock)
- Required social awareness (trusting Rem)
- Required technical skill (hacking)
- Required creative problem-solving (diversion)

**Conclusion:** Excellent multi-faceted encounter. Victory required synthesis of skills.
```

## Balance Issue Detection

**Automated Flags (from playtest_analyzer.py):**
- Character below 15% spotlight
- Clue below 30% discovery rate
- Dice mean outside 9-12 range
- Success rate below 50% or above 85%

**Manual Flags (Grader judgment):**
- Single approach dominates (e.g., "always hack")
- Faction objectives never achieved
- Win condition too easy/hard
- Stages collapse (e.g., skip Complication)

**Priority Categorization:**
- 🔴 **Critical:** Breaks encounter (e.g., unwinnable, character useless)
- 🟡 **Important:** Diminishes experience (e.g., clue rarely found)
- 🟢 **Minor:** Polish issue (e.g., slight pacing variation)

## Workflow Summary

**After Each Playtest:**
1. Run `playtest_analyzer.py` on JSON data
2. Review quantitative metrics
3. Write qualitative assessment (4 categories)
4. Cross-reference qual + quant
5. Flag any balance issues
6. Note recommendations

**After 5-10 Playtests:**
1. Run aggregate analysis
2. Identify trends across runs
3. Calculate discovery/spotlight averages
4. Create prioritized recommendation list
5. Generate summary report with charts (if available)
6. Provide clear action items for Lead Game Designer

**Integration with Lead Game Designer:**
- Recommendations drive encounter revisions
- Data validates design choices
- Trends identify systemic issues vs. one-off anomalies

---

**Remember:** Combine the precision of data with the insight of qualitative judgment. Numbers tell you *what* happened; your analysis explains *why* and *how to improve*.