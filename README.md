# NSP Energy Rates (Time-of-Day) for Home Assistant

![GitHub Release](https://img.shields.io/github/v/release/avrillica/nsp_energy)
![License](https://img.shields.io/github/license/avrillica/nsp_energy)
![Hassfest Validation](https://github.com/avrillica/nsp_energy/actions/workflows/hassfest.yaml/badge.svg)

Automated tracking of Nova Scotia Power Time-of-Day rates (2026 Tariff).

## Installation
1. Copy the `nsp_energy_v2` folder to your `custom_components` directory.
2. Restart Home Assistant.
3. Go to **Settings > Integrations > Add Integration** and search for **"NSP Energy Rates"**.

## Features
- Real-time pricing for Peak, Mid-Peak, and Off-Peak.
- Automatic seasonal switching (Winter/Non-Winter).
- 15% HST Toggle.
- 5 Sensors for price, period, and tax status.

## Disclaimer
This integration is not affiliated with or endorsed by Nova Scotia Power. Rates are based on public tariff information.
