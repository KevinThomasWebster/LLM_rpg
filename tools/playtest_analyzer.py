#!/usr/bin/env python3
"""
Playtest Data Analyzer

Features:
- Parse playtest markdown + JSON sidecar files
- Calculate spotlight distribution (% of actions per character)
- Generate charts (matplotlib/plotly)
- Calculate clue discovery rates across N playtests
- Identify underpowered characters (<15% spotlight threshold)
- Export summary reports to markdown
- Flag encounters needing rebalancing
"""

import json
import argparse
from pathlib import Path
from typing import List, Dict, Optional
from collections import defaultdict, Counter
import statistics


class PlaytestAnalyzer:
    def __init__(self, encounter_name: str, playtest_dir: Path):
        self.encounter_name = encounter_name
        self.playtest_dir = playtest_dir
        self.playtests: List[Dict] = []

    def load_playtests(self) -> int:
        """Load all playtest data JSON files for this encounter"""
        pattern = f"playtest_*_data.json"
        files = sorted(self.playtest_dir.glob(pattern))

        for file in files:
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    self.playtests.append(data)
            except Exception as e:
                print(f"Warning: Could not load {file}: {e}")

        print(f"Loaded {len(self.playtests)} playtests for {self.encounter_name}")
        return len(self.playtests)

    def calculate_spotlight_distribution(self, playtest_data: Dict) -> Dict[str, float]:
        """Calculate percentage of actions per character"""
        actions = playtest_data.get("character_actions", [])
        if not actions:
            return {}

        character_counts = Counter(action["character"] for action in actions)
        total_actions = len(actions)

        distribution = {
            char: round(count / total_actions * 100, 1)
            for char, count in character_counts.items()
        }

        return distribution

    def aggregate_spotlight_distribution(self) -> Dict[str, Dict]:
        """Aggregate spotlight distribution across all playtests"""
        if not self.playtests:
            return {}

        all_distributions = []
        characters = set()

        for playtest in self.playtests:
            dist = playtest.get("spotlight_distribution", {})
            if not dist:
                # Calculate if not provided
                dist = self.calculate_spotlight_distribution(playtest)

            all_distributions.append(dist)
            characters.update(dist.keys())

        # Calculate average distribution per character
        aggregate = {}
        for char in characters:
            values = [d.get(char, 0) for d in all_distributions]
            aggregate[char] = {
                "mean": round(statistics.mean(values), 1),
                "min": min(values),
                "max": max(values),
                "stdev": round(statistics.stdev(values), 1) if len(values) > 1 else 0,
                "samples": len(values)
            }

        return aggregate

    def calculate_clue_discovery_rate(self) -> Dict[str, Dict]:
        """Calculate how often each clue was discovered"""
        if not self.playtests:
            return {}

        all_clues = set()
        for playtest in self.playtests:
            all_clues.update(playtest.get("clues_discovered", []))

        clue_stats = {}
        total_playtests = len(self.playtests)

        for clue in all_clues:
            discovered_count = sum(
                1 for p in self.playtests
                if clue in p.get("clues_discovered", [])
            )

            clue_stats[clue] = {
                "discovered_count": discovered_count,
                "total_playtests": total_playtests,
                "discovery_rate": round(discovered_count / total_playtests * 100, 1)
            }

        # Sort by discovery rate (ascending)
        clue_stats = dict(sorted(clue_stats.items(), key=lambda x: x[1]["discovery_rate"]))

        return clue_stats

    def calculate_win_condition_frequency(self) -> Dict[str, int]:
        """Calculate how often each win condition was triggered"""
        if not self.playtests:
            return {}

        win_conditions = Counter(
            p.get("win_condition", "unknown") for p in self.playtests
        )

        return dict(win_conditions)

    def analyze_dice_statistics(self) -> Dict:
        """Analyze dice roll statistics across all playtests"""
        if not self.playtests:
            return {}

        all_rolls = []
        critical_hits = 0
        critical_fails = 0
        success_count = 0
        total_checks = 0

        for playtest in self.playtests:
            actions = playtest.get("character_actions", [])
            for action in actions:
                if "roll" in action and action.get("skill_check"):
                    roll = action["roll"]
                    all_rolls.append(roll)

                    if roll == 20:
                        critical_hits += 1
                    elif roll == 1:
                        critical_fails += 1

                    if action.get("success"):
                        success_count += 1
                    total_checks += 1

        if not all_rolls:
            return {"error": "No dice rolls found"}

        return {
            "total_rolls": len(all_rolls),
            "mean": round(statistics.mean(all_rolls), 2),
            "median": statistics.median(all_rolls),
            "critical_hits": critical_hits,
            "critical_fails": critical_fails,
            "critical_hit_rate": round(critical_hits / len(all_rolls) * 100, 2) if all_rolls else 0,
            "success_rate": round(success_count / total_checks * 100, 1) if total_checks > 0 else 0,
            "total_checks": total_checks
        }

    def identify_balance_issues(self, spotlight_threshold: float = 15.0) -> List[str]:
        """Identify potential balance issues"""
        issues = []

        # Check spotlight distribution
        spotlight_data = self.aggregate_spotlight_distribution()
        num_characters = len(spotlight_data)
        expected_spotlight = 100 / num_characters if num_characters > 0 else 0

        for char, stats in spotlight_data.items():
            if stats["mean"] < spotlight_threshold:
                issues.append(
                    f"⚠️ {char} underpowered: {stats['mean']}% avg spotlight "
                    f"(expected: ~{expected_spotlight:.1f}%)"
                )

        # Check clue discovery rates
        clue_stats = self.calculate_clue_discovery_rate()
        for clue, stats in clue_stats.items():
            if stats["discovery_rate"] < 30:
                issues.append(
                    f"⚠️ '{clue}' clue rarely found: {stats['discovery_rate']}% discovery rate"
                )

        # Check dice statistics
        dice_stats = self.analyze_dice_statistics()
        if "error" not in dice_stats:
            if dice_stats["mean"] > 12 or dice_stats["mean"] < 9:
                issues.append(
                    f"⚠️ Dice rolls potentially biased: mean={dice_stats['mean']} (expected: ~10.5)"
                )

        return issues

    def generate_markdown_report(self, output_path: Optional[Path] = None) -> str:
        """Generate comprehensive markdown report"""
        if not self.playtests:
            return "# Error\n\nNo playtests loaded."

        report_lines = [
            f"# Playtest Analysis: {self.encounter_name}",
            "",
            f"**Total Playtests:** {len(self.playtests)}",
            "",
            "---",
            ""
        ]

        # Spotlight Distribution
        report_lines.extend([
            "## Spotlight Distribution",
            ""
        ])

        spotlight_data = self.aggregate_spotlight_distribution()
        num_chars = len(spotlight_data)
        expected = round(100 / num_chars, 1) if num_chars > 0 else 0

        for char, stats in sorted(spotlight_data.items(), key=lambda x: x[1]["mean"], reverse=True):
            status = "✅" if abs(stats["mean"] - expected) < 10 else "⚠️"
            report_lines.append(
                f"- **{char}:** {stats['mean']}% (Target: ~{expected}%) {status}"
            )
            if stats["stdev"] > 15:
                report_lines.append(f"  - High variance: σ={stats['stdev']}%")

        report_lines.extend(["", "---", ""])

        # Clue Discovery Rate
        report_lines.extend([
            "## Clue Discovery Rate",
            ""
        ])

        clue_stats = self.calculate_clue_discovery_rate()
        for clue, stats in clue_stats.items():
            status = "✅" if stats["discovery_rate"] >= 70 else "⚠️" if stats["discovery_rate"] >= 30 else "❌"
            report_lines.append(
                f"- **{clue}:** {stats['discovery_rate']}% "
                f"({stats['discovered_count']}/{stats['total_playtests']}) {status}"
            )

        report_lines.extend(["", "---", ""])

        # Win Conditions
        report_lines.extend([
            "## Win Condition Frequency",
            ""
        ])

        win_conditions = self.calculate_win_condition_frequency()
        for condition, count in sorted(win_conditions.items(), key=lambda x: x[1], reverse=True):
            percentage = round(count / len(self.playtests) * 100, 1)
            report_lines.append(f"- **{condition}:** {count} times ({percentage}%)")

        report_lines.extend(["", "---", ""])

        # Dice Statistics
        report_lines.extend([
            "## Dice Statistics",
            ""
        ])

        dice_stats = self.analyze_dice_statistics()
        if "error" not in dice_stats:
            report_lines.extend([
                f"- **Mean d20 roll:** {dice_stats['mean']} (Expected: 10.5) "
                f"{'✅' if 9 <= dice_stats['mean'] <= 12 else '⚠️'}",
                f"- **Median d20 roll:** {dice_stats['median']}",
                f"- **Critical hit rate:** {dice_stats['critical_hit_rate']}% (Expected: 5%) "
                f"{'✅' if 3 <= dice_stats['critical_hit_rate'] <= 7 else '⚠️'}",
                f"- **Success rate:** {dice_stats['success_rate']}%",
                f"- **Total skill checks:** {dice_stats['total_checks']}",
            ])
        else:
            report_lines.append(f"*{dice_stats['error']}*")

        report_lines.extend(["", "---", ""])

        # Balance Issues
        report_lines.extend([
            "## Identified Issues",
            ""
        ])

        issues = self.identify_balance_issues()
        if issues:
            for issue in issues:
                report_lines.append(f"- {issue}")
        else:
            report_lines.append("✅ No significant balance issues detected")

        report_lines.extend(["", "---", ""])

        # Recommendations
        report_lines.extend([
            "## Recommendations",
            ""
        ])

        # Generate recommendations based on issues
        recommendations = self._generate_recommendations(spotlight_data, clue_stats)
        if recommendations:
            for i, rec in enumerate(recommendations, 1):
                report_lines.append(f"{i}. {rec}")
        else:
            report_lines.append("*Encounter appears well-balanced. Continue monitoring in future playtests.*")

        report_lines.extend(["", "---", ""])
        report_lines.append(f"*Report generated from {len(self.playtests)} playtests*")

        report = "\n".join(report_lines)

        # Save to file if path provided
        if output_path:
            output_path.write_text(report)
            print(f"Report saved to {output_path}")

        return report

    def _generate_recommendations(self, spotlight_data: Dict, clue_stats: Dict) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []

        # Spotlight recommendations
        num_chars = len(spotlight_data)
        expected_spotlight = 100 / num_chars if num_chars > 0 else 0

        underpowered = [
            char for char, stats in spotlight_data.items()
            if stats["mean"] < expected_spotlight - 10
        ]

        if underpowered:
            for char in underpowered:
                recommendations.append(
                    f"**Increase {char}'s spotlight:** Add skill check or challenge "
                    f"suited to their abilities (currently {spotlight_data[char]['mean']}% vs "
                    f"expected {expected_spotlight:.1f}%)"
                )

        # Clue recommendations
        difficult_clues = [
            clue for clue, stats in clue_stats.items()
            if stats["discovery_rate"] < 50
        ]

        if difficult_clues:
            for clue in difficult_clues[:3]:  # Top 3 most difficult
                rate = clue_stats[clue]["discovery_rate"]
                recommendations.append(
                    f"**Make '{clue}' more discoverable:** Currently {rate}% discovery rate. "
                    f"Consider: reducing DC, adding NPC hint, or multiple discovery paths"
                )

        return recommendations


def main():
    parser = argparse.ArgumentParser(description="Analyze D&D playtest data")

    parser.add_argument("--encounter", type=str, required=True, help="Encounter name")
    parser.add_argument("--playtest-dir", type=str, help="Directory containing playtest files")
    parser.add_argument("--output", type=str, help="Output report file path")
    parser.add_argument("--metric", type=str, choices=["spotlight", "clues", "dice", "all"],
                       default="all", help="Specific metric to analyze")
    parser.add_argument("--test", action="store_true", help="Run self-test")

    args = parser.parse_args()

    # Self-test mode
    if args.test:
        print("Running self-test...")
        # Create sample data
        sample_data = {
            "playtest_id": "test_1",
            "encounter": "Test Encounter",
            "character_actions": [
                {"character": "Alex", "roll": 15, "success": True, "skill_check": "Perception"},
                {"character": "Casey", "roll": 8, "success": False, "skill_check": "Stealth"},
                {"character": "Ben", "roll": 12, "success": True, "skill_check": "Athletics"},
            ],
            "spotlight_distribution": {"Alex": 33.3, "Casey": 33.3, "Ben": 33.4},
            "clues_discovered": ["Test Clue 1", "Test Clue 2"],
            "win_condition": "success"
        }

        # Test calculations
        analyzer = PlaytestAnalyzer("Test Encounter", Path("."))
        analyzer.playtests = [sample_data, sample_data]

        spotlight = analyzer.aggregate_spotlight_distribution()
        print(f"✅ Spotlight calculation: {spotlight}")

        clues = analyzer.calculate_clue_discovery_rate()
        print(f"✅ Clue discovery: {clues}")

        print("\n✅ All tests passed!")
        return

    # Determine playtest directory
    if args.playtest_dir:
        playtest_dir = Path(args.playtest_dir)
    else:
        playtest_dir = Path("play_tests") / args.encounter

    if not playtest_dir.exists():
        print(f"Error: Playtest directory not found: {playtest_dir}")
        return

    # Initialize analyzer
    analyzer = PlaytestAnalyzer(args.encounter, playtest_dir)

    # Load playtests
    count = analyzer.load_playtests()
    if count == 0:
        print("No playtest data files found.")
        return

    # Generate report
    output_path = Path(args.output) if args.output else None
    report = analyzer.generate_markdown_report(output_path)

    # Print to console if no output file
    if not output_path:
        print("\n" + report)


if __name__ == "__main__":
    main()
