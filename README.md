# SAT-SPEAK

Track satellites from your terminal. Real-time positions, pass predictions, orbital data — all from free APIs.

No coding experience needed.

![Banner](assets/banner_menu.svg)

---

## What it does

| | |
|---|---|
| **orbital element data** | Look up any satellite's TLE and orbital stats from space-track.org |
| **live position** | Real-time lat/lon/altitude and whether it's visible from where you are |
| **pass predictions** | Find out exactly when a satellite will fly over your location |
| **TLE parser** | Paste or load TLE data and get every parameter decoded |

---

## Screenshots

### First-time setup
Walks you through getting API keys, saves them so you never have to enter them again

![Setup](assets/setup_wizard.svg)

### Orbital data
Look up any satellite by NORAD ID

![Orbital Elements](assets/orbital_elements.svg)

### Live position
Where is it right now

![Live Position](assets/live_position.svg)

### Pass predictions
Know when to look up

![Pass Predictions](assets/pass_predictions.svg)

### TLE parser

![TLE Parser](assets/tle_parser.svg)

---

## Requirements

- Python 3.8+ — [python.org/downloads](https://www.python.org/downloads/)
- Free [space-track.org](https://www.space-track.org/auth/createAccount) account
- Free [n2yo.com](https://www.n2yo.com/) account + API key

Everything else installs itself on first run.

---

## How to run it

```bash
git clone https://github.com/danialrobieiwong/SAT-SPEAK
cd SAT-SPEAK
./setup.sh
./run.sh
```

First launch will ask for your API keys and save them to a `.env` file. After that just run `./run.sh`.

---

## Getting your API keys

**Space-Track** — Register at [space-track.org/auth/createAccount](https://www.space-track.org/auth/createAccount), your login is just the email and password you sign up with

**N2YO** — Register at [n2yo.com](https://www.n2yo.com/), then find your API key on [this page](https://www.n2yo.com/login/edit/) after logging in

---

## Useful NORAD IDs

| Satellite | ID |
|---|---|
| ISS | 25544 |
| Hubble | 20580 |
| James Webb | 50463 |
| Tiangong | 48274 |

More at [celestrak.org](https://celestrak.org/SOCRATES/)

---

## Troubleshooting

**Python3 not found** — Install from [python.org](https://www.python.org/downloads/)

**Permission denied on setup.sh**
```bash
chmod +x setup.sh run.sh
```

**Space-Track login fails** — Double check your email/password at space-track.org

**N2YO returns nothing** — Make sure your API key is correct, find it at n2yo.com/login/edit/

---

## Use cases

**Spotting satellites with your eyes** — Use pass predictions for the ISS or Starlink, set minimum visibility to 300s+ to filter out short passes. Go outside 2 mins early and face the direction shown under "start azimuth". Best time is 30-90 mins after sunset when the sky is dark but the satellite is still lit up.

**Amateur radio** — If you're into ham radio, use the radio pass predictions to plan contact windows with satellites like SO-50 or AO-91. Set minimum elevation to around 10-15 degrees.

**OSINT / research** — Space-Track has the full catalog, over 20,000 objects. You can look up military, government and commercial satellites by NORAD ID and cross-reference their orbital elements to figure out what they're probably doing. High inclination means polar orbit, roughly circular apogee/perigee means it's not doing anything sneaky with its altitude.

**Journalism** — Verifying whether a satellite was overhead at a specific time and place. Pull the orbital period, run a pass prediction around the date in question.

**Learning orbital mechanics** — TLE parser is good for this. Grab a TLE from celestrak, paste it in, and you get all 19 parameters decoded. Eccentricity near 0 = circular orbit. Inclination over 80 = polar. The rest you can look up.

---

## Tips

- Use your actual GPS coordinates, not a rough approximation — it makes a noticeable difference in pass accuracy
- For visual spotting, passes with max elevation above 40-50 degrees are the ones worth going outside for
- New launches get NORAD IDs within a few days, you can track them on celestrak before most apps catch up
- Back up your `.env` file if you ever plan to reinstall

- :)
