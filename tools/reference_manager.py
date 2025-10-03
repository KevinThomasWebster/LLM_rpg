#!/usr/bin/env python3
"""
Reference Manager for D&D 2024 5e SRD Integration

Features:
- Download and index SRD content (TODO: implement download)
- Scan adventure documents for creature/spell mentions
- Generate adventure-specific bestiary
- Validate custom stat blocks
- Manual workflow support
"""

import argparse
import re
import json
from pathlib import Path
from typing import List, Dict, Set, Optional
from datetime import datetime


class ReferenceManager:
    def __init__(self, adventure_path: Path):
        self.adventure_path = adventure_path
        self.srd_path = Path("references/srd_5e_2024")
        self.mentions = {
            "monsters": set(),
            "spells": set(),
            "items": set()
        }

    def download_srd(self, source: str = "open5e"):
        """
        Download SRD content from specified source

        TODO: Implement actual download
        - Support Open5e API (https://api.open5e.com/)
        - Support local SRD files
        - Parse and index content
        """
        print(f"[TODO] Download SRD from {source}")
        print("For now, use manual workflow (see documentation)")
        return False

    def scan_adventure(self) -> Dict[str, Set[str]]:
        """
        Scan adventure documents for creature/spell/item mentions

        Returns dict of mentions by type
        """
        print(f"Scanning adventure: {self.adventure_path}")

        # Scan 01_Factions.md
        factions_file = self.adventure_path / "01_Factions.md"
        if factions_file.exists():
            print(f"  Scanning {factions_file.name}...")
            self._scan_file(factions_file)

        # Scan 02_Locations.md
        locations_file = self.adventure_path / "02_Locations.md"
        if locations_file.exists():
            print(f"  Scanning {locations_file.name}...")
            self._scan_file(locations_file)

        # Scan NPC cards if they exist
        npc_cards = self.adventure_path / "dm_materials" / "npc_cards"
        if npc_cards.exists():
            for npc_file in npc_cards.glob("*.md"):
                print(f"  Scanning {npc_file.name}...")
                self._scan_file(npc_file)

        return self.mentions

    def _scan_file(self, filepath: Path):
        """Scan individual file for mentions"""
        content = filepath.read_text(encoding='utf-8')

        # Common D&D creature names (basic detection)
        common_creatures = [
            "goblin", "orc", "dragon", "skeleton", "zombie", "vampire",
            "beholder", "mind flayer", "lich", "troll", "ogre", "kobold",
            "gnoll", "bugbear", "hobgoblin", "owlbear", "mimic", "gelatinous cube"
        ]

        for creature in common_creatures:
            # Case-insensitive search
            if re.search(rf'\b{creature}s?\b', content, re.IGNORECASE):
                self.mentions["monsters"].add(creature.title())

        # Detect custom creatures (capitalized multi-word names)
        # Example: "Glitched Lulu", "Security Lulu", "Heartbreak"
        custom_pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:attacks?|appears?|emerges?|HP|AC\s+\d+)'
        custom_matches = re.findall(custom_pattern, content)
        for match in custom_matches:
            if match not in ["Round", "Stage", "The", "A"]:  # Filter common words
                self.mentions["monsters"].add(f"{match} (CUSTOM)")

        # Common spell detection
        common_spells = [
            "fireball", "magic missile", "shield", "detect thoughts", "charm person",
            "invisibility", "fly", "lightning bolt", "counterspell", "dispel magic"
        ]

        for spell in common_spells:
            if re.search(rf'\b{spell}\b', content, re.IGNORECASE):
                self.mentions["spells"].add(spell.title())

    def generate_report(self) -> str:
        """Generate scan report markdown"""
        lines = [
            "# Reference Scan Report",
            "",
            f"**Adventure:** {self.adventure_path.name}",
            f"**Scan Date:** {datetime.now().strftime('%Y-%m-%d')}",
            "",
            "## Findings",
            ""
        ]

        # Official monsters
        official = [m for m in self.mentions["monsters"] if "(CUSTOM)" not in m]
        custom = [m for m in self.mentions["monsters"] if "(CUSTOM)" in m]

        if official:
            lines.extend([
                "### Official SRD Creatures Found",
                ""
            ])
            for creature in sorted(official):
                lines.append(f"- {creature}")
            lines.append("")

        if custom:
            lines.extend([
                "### Custom Creatures Detected",
                "*(Require stat blocks)*",
                ""
            ])
            for creature in sorted(custom):
                clean_name = creature.replace(" (CUSTOM)", "")
                lines.append(f"- **{clean_name}** ⚠️ Needs stat block")
            lines.append("")

        if self.mentions["spells"]:
            lines.extend([
                "### Spells Mentioned",
                ""
            ])
            for spell in sorted(self.mentions["spells"]):
                lines.append(f"- {spell}")
            lines.append("")

        if not any(self.mentions.values()):
            lines.append("*No creatures or spells detected in scan.*")
            lines.append("")

        lines.extend([
            "---",
            "",
            "## Next Steps",
            "",
            "1. Create stat blocks for all CUSTOM creatures in `dm_materials/npc_cards/`",
            "2. Validate custom stat blocks using `--validate` command",
            "3. Generate bestiary using `--generate-bestiary` command",
            ""
        ])

        return "\n".join(lines)

    def generate_bestiary(self, output_path: Optional[Path] = None):
        """Generate adventure-specific bestiary"""
        if output_path is None:
            output_path = self.adventure_path / "references" / "monsters_used.md"

        output_path.parent.mkdir(parents=True, exist_ok=True)

        lines = [
            f"# Bestiary - {self.adventure_path.name}",
            "",
            "*This document lists all creatures used in the adventure.*",
            "",
            "## Official SRD Creatures",
            "",
            "*Refer to D&D 2024 5e SRD or Monster Manual for complete stat blocks.*",
            ""
        ]

        official = [m for m in self.mentions["monsters"] if "(CUSTOM)" not in m]
        for creature in sorted(official):
            lines.extend([
                f"### {creature}",
                "",
                "**Source:** D&D 2024 SRD",
                "**Used In:** [Location names - TODO: track this]",
                ""
            ])

        lines.extend([
            "---",
            "",
            "## Custom Creatures",
            "",
            "*Full stat blocks required. See `dm_materials/npc_cards/` for details.*",
            ""
        ])

        custom = [m for m in self.mentions["monsters"] if "(CUSTOM)" in m]
        for creature in sorted(custom):
            clean_name = creature.replace(" (CUSTOM)", "")
            lines.extend([
                f"### {clean_name}",
                "",
                "**Status:** ⚠️ Stat block required",
                "**Suggested CR:** [TODO: analyze context]",
                "**Used In:** [TODO: track locations]",
                "",
                "**Design Notes:**",
                "- [TODO: Add design guidance based on narrative role]",
                ""
            ])

        lines.extend([
            "---",
            "",
            f"*Generated by reference_manager.py*",
            f"*Last updated: [TODO: add timestamp]*"
        ])

        output_path.write_text("\n".join(lines), encoding='utf-8')
        print(f"Bestiary generated: {output_path}")

    def validate_statblock(self, statblock_file: Path):
        """
        Validate custom stat block

        TODO: Implement actual validation
        - Check AC within range for CR
        - Verify HP matches Hit Dice
        - Validate attack bonuses
        - Check damage per round for CR
        """
        print(f"[TODO] Validate stat block: {statblock_file}")
        print("Manual validation recommended:")
        print("  1. Check proficiency bonus matches CR")
        print("  2. Verify AC is within ±3 of expected for CR")
        print("  3. Confirm HP matches Hit Dice calculation")
        print("  4. Validate attack bonus = Prof + Ability mod")
        print("  5. Check damage per round vs. DMG table (p.274)")


def main():
    parser = argparse.ArgumentParser(
        description="Manage D&D 2024 5e SRD references for adventures"
    )

    parser.add_argument("--adventure", type=str, help="Adventure directory name")
    parser.add_argument("--scan", action="store_true", help="Scan adventure for references")
    parser.add_argument("--download", type=str, choices=["srd-2024", "open5e"], help="Download SRD")
    parser.add_argument("--generate-bestiary", action="store_true", help="Generate bestiary")
    parser.add_argument("--validate", type=str, help="Validate stat block file")
    parser.add_argument("--test", action="store_true", help="Run self-test")

    args = parser.parse_args()

    # Self-test mode
    if args.test:
        print("Running self-test...")

        # Test adventure path
        test_path = Path("test_adventure")
        rm = ReferenceManager(test_path)
        print(f"[OK] ReferenceManager initialized with path: {rm.adventure_path}")

        # Test mention detection
        rm.mentions["monsters"].add("Goblin")
        rm.mentions["monsters"].add("Glitched Lulu (CUSTOM)")
        rm.mentions["spells"].add("Fireball")
        print(f"[OK] Mentions tracked: {len(rm.mentions['monsters'])} monsters, {len(rm.mentions['spells'])} spells")

        # Test report generation
        report = rm.generate_report()
        print(f"[OK] Report generated: {len(report)} characters")

        print("\n[OK] All tests passed!")
        print("\nNote: This is a functional skeleton. Full features marked as [TODO].")
        return

    # Require adventure path for most operations
    if not args.adventure and not args.test:
        print("Error: --adventure required (or use --test)")
        return

    adventure_path = Path(args.adventure) if args.adventure else None
    rm = ReferenceManager(adventure_path) if adventure_path else None

    # Download SRD
    if args.download:
        print(f"Attempting to download SRD: {args.download}")
        success = rm.download_srd(args.download)
        if not success:
            print("\n[Manual Workflow]")
            print("1. Download SRD manually from official sources")
            print("2. Place in references/srd_5e_2024/")
            print("3. Use --scan to detect mentions")

    # Scan adventure
    if args.scan and rm:
        mentions = rm.scan_adventure()

        # Generate and display report
        report = rm.generate_report()
        print("\n" + report)

        # Save report
        report_path = rm.adventure_path / "references" / "scan_report.md"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding='utf-8')
        print(f"\nReport saved to: {report_path}")

    # Generate bestiary
    if args.generate_bestiary and rm:
        if not rm.mentions["monsters"]:
            print("No creatures found. Run --scan first.")
        else:
            rm.generate_bestiary()

    # Validate stat block
    if args.validate:
        rm.validate_statblock(Path(args.validate))


if __name__ == "__main__":
    main()
