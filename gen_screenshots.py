#!/usr/bin/env python3
"""Generates SVG screenshots for the README."""
import os
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.rule import Rule
from rich import box

OUT = Path("assets")
OUT.mkdir(exist_ok=True)

BANNER = r"""
  *    .  .       *    .        .      *    .     .    .  *
.       .   .    .  *  .   .         .   .    .       .
   *  .    .   .          .    .   *      .       *       .

   ███████╗ █████╗ ████████╗      ███████╗██████╗ ███████╗ █████╗ ██╗  ██╗
   ██╔════╝██╔══██╗╚══██╔══╝      ██╔════╝██╔══██╗██╔════╝██╔══██╗██║ ██╔╝
   ███████╗███████║   ██║   █████╗███████╗██████╔╝█████╗  ███████║█████╔╝
   ╚════██║██╔══██║   ██║   ╚════╝╚════██║██╔═══╝ ██╔══╝  ██╔══██║██╔═██╗
   ███████║██║  ██║   ██║         ███████║██║     ███████╗██║  ██║██║  ██╗
   ╚══════╝╚═╝  ╚═╝   ╚═╝         ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

.       .   .  *  .        .   .         .     *    .     .   .
  .  *     .      .     .    *    .    .          .    .
   *    .      .    .            .   *    .    .      *    .
"""

MENU = r"""
  ┌─────────────────────────────────────────────────────────────┐
  │                       MAIN MENU                             │
  │                                                             │
  │  [1]  Orbital Element Data     — TLE & catalog lookup       │
  │  [2]  Satellite Position       — Real-time lat/lon/alt      │
  │  [3]  Orbital Pass Predictions — When will it fly over?     │
  │  [4]  TLE Parser               — Decode TLE strings/files   │
  │                                                             │
  │  [S]  Setup / Change API Keys                               │
  │  [0]  Exit                                                  │
  └─────────────────────────────────────────────────────────────┘
"""

STARS = r"""
  .   *   .    .   *     .    .   .    *    .   .     *    .   .   *
      .       .      *      .      .     .      *    .      .      *
  *      .       .      .       *     .      .      .    *      .
"""


def make_console(width=80):
    return Console(record=True, width=width, force_terminal=True,
                   force_jupyter=False, highlight=False)


# ── Screenshot 1: Banner + Menu ──────────────────────────────────────────────
c = make_console(width=82)
c.print(BANNER, style="bright_white")
c.print("[dim white]  Satellite OSINT Intelligence Tool[/dim white]")
c.print(STARS, style="dim white")
c.print(MENU, style="bright_white")
(OUT / "banner_menu.svg").write_text(
    c.export_svg(title="SAT-SPEAK")
)
print("✓ banner_menu.svg")

# ── Screenshot 2: Setup Wizard ────────────────────────────────────────────────
c = make_console(width=82)
c.print()
c.print(Rule("[bold white]FIRST-TIME SETUP[/bold white]", style="white"))
c.print()
c.print("[white]SAT-SPEAK needs API keys to pull satellite data.[/white]")
c.print()
c.print("[white]Step 1 — Space-Track (free account)[/white]")
c.print("[dim white]  → Go to: https://www.space-track.org/auth/createAccount[/dim white]")
c.print()
c.print("[white]Step 2 — N2YO (free account)[/white]")
c.print("[dim white]  → Go to: https://www.n2yo.com/[/dim white]")
c.print("[dim white]  → API key: https://www.n2yo.com/login/edit/[/dim white]")
c.print()
c.print("  [white]Space-Track username (email)[/white]: danial@example.com")
c.print("  [white]Space-Track password[/white]: ••••••••••••")
c.print("  [white]N2YO API key[/white]: XXXX-XXXX-XXXX")
c.print()
c.print("[bold white]✓ Credentials saved to .env[/bold white]")
(OUT / "setup_wizard.svg").write_text(
    c.export_svg(title="SAT-SPEAK — Setup")
)
print("✓ setup_wizard.svg")

# ── Screenshot 3: Orbital Element lookup ─────────────────────────────────────
c = make_console(width=82)
c.print()
c.print(Rule("[bold white]ORBITAL ELEMENT DATA[/bold white]", style="white"))
c.print()

info_table = Table(box=box.SIMPLE_HEAVY, border_style="white",
                   header_style="bold white", show_header=False, show_lines=True)
info_table.add_column("Field", style="dim white", min_width=28)
info_table.add_column("Value", style="bright_white")

fields = [
    ("Satellite Name",         "ISS (ZARYA)"),
    ("NORAD ID",               "25544"),
    ("International Designator", "1998-067A"),
    ("Object Type",            "PAYLOAD"),
    ("Epoch",                  "2026-04-25T06:12:00"),
    ("Inclination (°)",        "51.6435"),
    ("Eccentricity",           "0.0001240"),
    ("Apogee (km)",            "422"),
    ("Perigee (km)",           "418"),
    ("Orbital Period (min)",   "92.89"),
    ("Mean Motion (rev/day)",  "15.49"),
    ("Revolutions at Epoch",   "144141"),
    ("Country of Origin",      "ISS"),
    ("Launch Date",            "1998-11-20"),
    ("Decay Date",             "Still orbiting"),
    ("RCS Object",             "LARGE"),
]
for field, val in fields:
    info_table.add_row(field, val)

c.print(Panel(info_table, title="[bold bright_white]ISS (ZARYA)[/bold bright_white]",
              border_style="white"))
c.print()
c.print("  [dim white]TLE Lines:[/dim white]")
c.print("  [white]1 25544U 98067A   26115.25833333  .00015000  00000-0  27000-3 0  9990[/white]")
c.print("  [white]2 25544  51.6435 120.4321 0001240  88.1234 271.9876 15.49012345144141[/white]")
(OUT / "orbital_elements.svg").write_text(
    c.export_svg(title="SAT-SPEAK — Orbital Elements")
)
print("✓ orbital_elements.svg")

# ── Screenshot 4: Live Position ───────────────────────────────────────────────
c = make_console(width=82)
c.print()
c.print(Rule("[bold white]SATELLITE POSITION & TELEMETRY[/bold white]", style="white"))
c.print()

pos_table = Table(box=box.SIMPLE_HEAVY, border_style="white",
                  header_style="bold white",
                  title="Live Position — ISS (ZARYA)",
                  title_style="bold bright_white",
                  show_header=False, show_lines=True)
pos_table.add_column("Parameter", style="dim white", min_width=28)
pos_table.add_column("Value",     style="bright_white")

pos_table.add_row("Satellite Name",      "ISS (ZARYA)")
pos_table.add_row("NORAD ID",            "25544")
pos_table.add_row("Latitude (°)",        "3.8812")
pos_table.add_row("Longitude (°)",       "98.2341")
pos_table.add_row("Altitude (km)",       "421.47")
pos_table.add_row("Azimuth (°)",         "232.14")
pos_table.add_row("Elevation (°)",       "28.93")
pos_table.add_row("Right Ascension (°)", "112.4412")
pos_table.add_row("Declination (°)",     "47.2209")
pos_table.add_row("Timestamp (UTC)",     "2026-04-25 06:14:22 UTC")
pos_table.add_row("Visibility",          "VISIBLE above your horizon")

c.print(pos_table)
(OUT / "live_position.svg").write_text(
    c.export_svg(title="SAT-SPEAK — Live Position")
)
print("✓ live_position.svg")

# ── Screenshot 5: Pass Predictions ───────────────────────────────────────────
c = make_console(width=90)
c.print()
c.print(Rule("[bold white]ORBITAL PASS PREDICTIONS[/bold white]", style="white"))
c.print()

pass_table = Table(
    title="Visual Passes — ISS (ZARYA)  (5 passes over 3 day(s))",
    box=box.SIMPLE_HEAVY,
    border_style="white",
    header_style="bold white",
    title_style="bold bright_white",
)
for col in ("Start UTC", "Max UTC", "End UTC", "Max El (°)", "Start Az (°)", "End Az (°)", "Mag", "Duration (s)"):
    pass_table.add_column(col, style="white")

passes = [
    ("2026-04-25 19:42:11", "19:44:38", "19:47:05", "67", "311", "128", "-3.2", "294"),
    ("2026-04-25 21:18:44", "21:20:12", "21:21:41", "21", "295", "241", "-1.0", "177"),
    ("2026-04-26 19:01:03", "19:03:55", "19:06:48", "43", "320", "142", "-2.1", "345"),
    ("2026-04-26 20:37:29", "20:39:14", "20:41:00", "32", "308", "157", "-1.7", "331"),
    ("2026-04-27 18:22:17", "18:25:06", "18:27:55", "58", "307", "135", "-2.8", "338"),
]
for row in passes:
    pass_table.add_row(*row)

c.print(pass_table)
(OUT / "pass_predictions.svg").write_text(
    c.export_svg(title="SAT-SPEAK — Pass Predictions")
)
print("✓ pass_predictions.svg")

# ── Screenshot 6: TLE Parser ──────────────────────────────────────────────────
c = make_console(width=82)
c.print()
c.print(Rule("[bold white]TLE PARSER[/bold white]", style="white"))
c.print()

tle_table = Table(
    title="TLE Data — ISS (ZARYA)",
    box=box.SIMPLE_HEAVY,
    border_style="white",
    header_style="bold white",
    title_style="bold bright_white",
    show_lines=True,
)
tle_table.add_column("Parameter", style="white", min_width=22)
tle_table.add_column("Value",     style="bright_white", min_width=20)

tle_fields = [
    ("Satellite Number",    "25544"),
    ("Classification",      "U"),
    ("Int'l Designator",    "98067A"),
    ("Epoch Year",          "2026"),
    ("Epoch Day",           "115.25833333"),
    ("1st Derivative MM",   ".00015000"),
    ("2nd Derivative MM",   "00000-0"),
    ("BSTAR Drag Term",     "27000-3"),
    ("Ephemeris Type",      "0"),
    ("Element Set No.",     "999"),
    ("Inclination (°)",     "51.6435"),
    ("RAAN (°)",            "120.4321"),
    ("Eccentricity",        "0.0001240"),
    ("Arg of Perigee (°)",  "88.1234"),
    ("Mean Anomaly (°)",    "271.9876"),
    ("Mean Motion (rev/d)", "15.49012345"),
    ("Revolution No.",      "14414"),
    ("Checksum L1",         "0"),
    ("Checksum L2",         "1"),
]
for k, v in tle_fields:
    tle_table.add_row(k, v)

c.print(tle_table)
(OUT / "tle_parser.svg").write_text(
    c.export_svg(title="SAT-SPEAK — TLE Parser")
)
print("✓ tle_parser.svg")

print("\nAll screenshots saved to assets/")
