How to use the NSP Energy Rates Integration

Overview
This integration provides the real-time pricing structure for Nova Scotia Power’s Time-of-Day (TOD) tariff. It is essential for Home Assistant users in Nova Scotia who want to shift heavy loads (electric vehicles, heat pumps, or appliances) to off-peak hours to save money.

Initial Setup
Ensure the nsp_energy_v2 folder is in your custom_components directory.

Restart Home Assistant.

Go to Settings > Integrations > Add Integration and search for NSP Energy Rates.

Warning: Use the pre-filled 2026 rates. Do not change these unless NSP officially updates their tariff.

Calculating Cost (W to kWh to $)
To see your actual dollar spend in the Energy Dashboard, you need to convert raw power (Watts) to energy (kWh).

Step A: Power to Energy (Riemann Sum Integral)
If your monitor (e.g., Emporia Vue, Shelly) only provides Watts (W), use the Riemann Sum Integral helper:

Go to Settings > Devices & Services > Helpers.

Create a Riemann sum integral sensor.

Input sensor: Your Power sensor (W).

Integration method: Left Riemann sum.

Step B: Energy Dashboard

Go to Settings > Dashboards > Energy.

Under Electricity Grid, click Add Consumption.

Select your _kwh sensor.

Select "Use an entity with current price" and pick sensor.nsp_current_price.

Automation Ideas
Visual Cues: Change smart bulb colors (Red for Peak, Green for Off-Peak).

Load Shifting: Delay EV charging or Dishwashers until 11:00 PM (Off-Peak).

Thermal Battery: Pre-heat your home at 6:00 AM before Peak rates start at 7:00 AM.
