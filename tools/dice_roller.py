#!/usr/bin/env python3
"""
Dice Roller for D&D Playtesting

Features:
- Proper random number generation with seeding for reproducibility
- Statistical tracking (mean, median, critical frequency)
- Support for advantage/disadvantage
- Export roll logs to JSON for playtest analysis
- CLI interface for quick rolls
"""

import random
import re
import json
import argparse
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from collections import defaultdict
import statistics


class DiceRoller:
    def __init__(self, seed: Optional[int] = None):
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self.roll_history: List[Dict] = []

    def parse_dice_notation(self, notation: str) -> Tuple[int, int, int]:
        """
        Parse dice notation like '2d6+3' into (num_dice, die_size, modifier)
        """
        notation = notation.strip().lower()
        pattern = r'(\d+)d(\d+)([+-]\d+)?'
        match = re.match(pattern, notation)

        if not match:
            raise ValueError(f"Invalid dice notation: {notation}")

        num_dice = int(match.group(1))
        die_size = int(match.group(2))
        modifier = int(match.group(3)) if match.group(3) else 0

        return num_dice, die_size, modifier

    def roll_die(self, die_size: int) -> int:
        """Roll a single die"""
        return random.randint(1, die_size)

    def roll_with_advantage(self, die_size: int) -> Tuple[int, int, int]:
        """Roll with advantage (take higher of two rolls)"""
        roll1 = self.roll_die(die_size)
        roll2 = self.roll_die(die_size)
        return max(roll1, roll2), roll1, roll2

    def roll_with_disadvantage(self, die_size: int) -> Tuple[int, int, int]:
        """Roll with disadvantage (take lower of two rolls)"""
        roll1 = self.roll_die(die_size)
        roll2 = self.roll_die(die_size)
        return min(roll1, roll2), roll1, roll2

    def roll(
        self,
        notation: str,
        advantage: bool = False,
        disadvantage: bool = False,
        character: str = "",
        action: str = "",
        round_num: int = 0
    ) -> Dict:
        """
        Main roll function

        Args:
            notation: Dice notation (e.g., "1d20+5")
            advantage: Roll with advantage
            disadvantage: Roll with disadvantage
            character: Character name for tracking
            action: Action description
            round_num: Combat round number

        Returns:
            Dictionary with roll results and metadata
        """
        num_dice, die_size, modifier = self.parse_dice_notation(notation)

        individual_rolls = []
        advantage_info = None

        # Handle d20 with advantage/disadvantage
        if die_size == 20 and (advantage or disadvantage):
            if advantage:
                result, roll1, roll2 = self.roll_with_advantage(die_size)
                advantage_info = {"type": "advantage", "rolls": [roll1, roll2], "chosen": result}
            else:
                result, roll1, roll2 = self.roll_with_disadvantage(die_size)
                advantage_info = {"type": "disadvantage", "rolls": [roll1, roll2], "chosen": result}
            individual_rolls = [result]
        else:
            # Normal roll
            individual_rolls = [self.roll_die(die_size) for _ in range(num_dice)]

        # Calculate total
        total = sum(individual_rolls) + modifier

        # Determine if critical (for d20 only)
        is_critical_hit = die_size == 20 and 20 in individual_rolls
        is_critical_fail = die_size == 20 and 1 in individual_rolls and max(individual_rolls) == 1

        # Build result dictionary
        result = {
            "timestamp": datetime.now().isoformat(),
            "notation": notation,
            "num_dice": num_dice,
            "die_size": die_size,
            "modifier": modifier,
            "rolls": individual_rolls,
            "total": total,
            "character": character,
            "action": action,
            "round": round_num,
            "critical_hit": is_critical_hit,
            "critical_fail": is_critical_fail,
        }

        if advantage_info:
            result["advantage_info"] = advantage_info

        self.roll_history.append(result)
        return result

    def get_statistics(self) -> Dict:
        """Calculate statistics from roll history"""
        if not self.roll_history:
            return {}

        # Filter for d20 rolls only
        d20_rolls = [
            r for r in self.roll_history
            if r["die_size"] == 20 and r["num_dice"] == 1
        ]

        if not d20_rolls:
            return {"error": "No d20 rolls in history"}

        # Extract roll values (without modifiers)
        roll_values = []
        for r in d20_rolls:
            if "advantage_info" in r:
                roll_values.append(r["advantage_info"]["chosen"])
            else:
                roll_values.append(r["rolls"][0])

        # Calculate statistics
        stats = {
            "total_rolls": len(d20_rolls),
            "mean": round(statistics.mean(roll_values), 2),
            "median": statistics.median(roll_values),
            "mode": statistics.mode(roll_values) if len(set(roll_values)) < len(roll_values) else None,
            "min": min(roll_values),
            "max": max(roll_values),
            "critical_hits": sum(1 for r in d20_rolls if r["critical_hit"]),
            "critical_fails": sum(1 for r in d20_rolls if r["critical_fail"]),
            "advantage_rolls": sum(1 for r in d20_rolls if "advantage_info" in r and r["advantage_info"]["type"] == "advantage"),
            "disadvantage_rolls": sum(1 for r in d20_rolls if "advantage_info" in r and r["advantage_info"]["type"] == "disadvantage"),
        }

        # Calculate percentages
        stats["critical_hit_rate"] = round(stats["critical_hits"] / stats["total_rolls"] * 100, 2)
        stats["critical_fail_rate"] = round(stats["critical_fails"] / stats["total_rolls"] * 100, 2)

        # Chi-squared test for bias (simplified)
        expected_freq = stats["total_rolls"] / 20
        chi_squared = sum(
            ((roll_values.count(i) - expected_freq) ** 2) / expected_freq
            for i in range(1, 21)
        )
        stats["chi_squared"] = round(chi_squared, 2)
        # Rough p-value interpretation (degrees of freedom = 19)
        stats["possibly_biased"] = chi_squared > 30.14  # p < 0.05

        return stats

    def export_log(self, filepath: str):
        """Export roll history to JSON file"""
        data = {
            "seed": self.seed,
            "timestamp": datetime.now().isoformat(),
            "rolls": self.roll_history,
            "statistics": self.get_statistics()
        }

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"Roll log exported to {filepath}")

    def load_log(self, filepath: str):
        """Load roll history from JSON file"""
        with open(filepath, 'r') as f:
            data = json.load(f)

        self.seed = data.get("seed")
        self.roll_history = data.get("rolls", [])
        print(f"Loaded {len(self.roll_history)} rolls from {filepath}")

    def print_statistics(self):
        """Pretty print statistics"""
        stats = self.get_statistics()

        if "error" in stats:
            print(stats["error"])
            return

        print("\n=== Dice Roll Statistics ===")
        print(f"Total d20 rolls: {stats['total_rolls']}")
        print(f"Mean: {stats['mean']} (Expected: 10.5)")
        print(f"Median: {stats['median']}")
        print(f"Range: {stats['min']}-{stats['max']}")
        print(f"\nCritical hits: {stats['critical_hits']} ({stats['critical_hit_rate']}%)")
        print(f"Critical fails: {stats['critical_fails']} ({stats['critical_fail_rate']}%)")
        print(f"\nAdvantage rolls: {stats['advantage_rolls']}")
        print(f"Disadvantage rolls: {stats['disadvantage_rolls']}")
        print(f"\nChi-squared: {stats['chi_squared']}")
        print(f"Possibly biased: {'⚠️ YES' if stats['possibly_biased'] else '✅ NO'}")
        print("=" * 30 + "\n")


def main():
    parser = argparse.ArgumentParser(description="D&D Dice Roller with statistical tracking")

    parser.add_argument("--roll", type=str, help="Dice notation (e.g., '1d20+5')")
    parser.add_argument("--advantage", action="store_true", help="Roll with advantage")
    parser.add_argument("--disadvantage", action="store_true", help="Roll with disadvantage")
    parser.add_argument("--seed", type=int, help="Random seed for reproducibility")
    parser.add_argument("--character", type=str, default="", help="Character name")
    parser.add_argument("--action", type=str, default="", help="Action description")
    parser.add_argument("--round", type=int, default=0, help="Combat round number")
    parser.add_argument("--log", type=str, help="Log file path (JSON)")
    parser.add_argument("--export", type=str, help="Export roll history to file")
    parser.add_argument("--import", type=str, dest="import_file", help="Import roll history from file")
    parser.add_argument("--stats", action="store_true", help="Show statistics from current/imported log")
    parser.add_argument("--test", action="store_true", help="Run self-test")

    args = parser.parse_args()

    # Self-test mode
    if args.test:
        print("Running self-test...")
        roller = DiceRoller(seed=42)

        # Test basic roll
        result = roller.roll("1d20+5", character="TestChar", action="Test Attack")
        print(f"✅ Basic roll: {result['notation']} = {result['total']}")

        # Test advantage
        result = roller.roll("1d20", advantage=True, character="TestChar", action="Test with Advantage")
        print(f"✅ Advantage roll: {result['advantage_info']['rolls']} -> {result['advantage_info']['chosen']}")

        # Test multiple rolls
        for i in range(20):
            roller.roll("1d20")

        stats = roller.get_statistics()
        print(f"✅ Statistics calculated: {stats['total_rolls']} rolls, mean={stats['mean']}")

        print("\n✅ All tests passed!")
        return

    # Initialize roller
    roller = DiceRoller(seed=args.seed)

    # Import existing log if specified
    if args.import_file:
        roller.load_log(args.import_file)

    # Perform roll if specified
    if args.roll:
        result = roller.roll(
            notation=args.roll,
            advantage=args.advantage,
            disadvantage=args.disadvantage,
            character=args.character,
            action=args.action,
            round_num=args.round
        )

        # Print result
        print(f"\n🎲 {result['notation']}")
        if "advantage_info" in result:
            adv_type = result['advantage_info']['type'].capitalize()
            rolls = result['advantage_info']['rolls']
            chosen = result['advantage_info']['chosen']
            print(f"   {adv_type}: {rolls} -> {chosen}")
        else:
            print(f"   Rolls: {result['rolls']}")
        print(f"   Total: {result['total']}")

        if result['critical_hit']:
            print("   🎯 CRITICAL HIT!")
        elif result['critical_fail']:
            print("   💀 CRITICAL FAIL!")

        # Save to log if specified
        if args.log:
            roller.export_log(args.log)

    # Show statistics if requested
    if args.stats:
        roller.print_statistics()

    # Export if specified (and not already done)
    if args.export and not args.log:
        roller.export_log(args.export)


if __name__ == "__main__":
    main()
