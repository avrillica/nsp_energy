I have expanded the instructions to make them more approachable for a typical user. I've also integrated the automation ideas as a dedicated section to help you get the most out of the integration.

As per your request, I am providing the full set of files (Code, Instructions, and Version Control) all together.

File 1: INSTRUCTIONS.md
NSP Energy Rates: User Guide & Automation Ideas

1. Why do you need this in Home Assistant?
Nova Scotia Power uses "Time-of-Day" (TOD) rates for customers with electric thermal storage or heat pumps. Electricity isn't one flat price; it's significantly more expensive during "Peak" hours. This integration brings that schedule into Home Assistant so you can:

See exactly what you are paying right now.

Automate appliances to stop running when prices are high.

Track your monthly bill accurately within the Energy Dashboard.

2. How to Configure with an Energy Monitor
Most energy monitors (like Emporia Vue, Shelly, or Iotawatt) tell you how many Watts (Power) you are using right now. However, your power bill is based on kWh (Energy).

Step A: Convert Watts to kWh
You must create a "Helper" to calculate the total energy used over time:

Go to Settings > Devices & Services > Helpers.

Click Create Helper and choose Riemann sum integral sensor.

Input sensor: Select your monitor's Power sensor (e.g., sensor.main_panel_power).

Integration method: Select Left Riemann sum (this is the most accurate for home power).

Precision: Set to 2.

This creates a new sensor (e.g., sensor.main_panel_kwh).

Step B: Link to the Energy Dashboard

Go to Settings > Dashboards > Energy.

Under Electricity Grid, click Add Consumption.

For Consumed Energy, pick the _kwh sensor you just made.

Select "Use an entity with current price".

Pick sensor.nsp_current_price from this integration.
Home Assistant will now automatically multiply your usage by the 2026 TOD rates to show you your spending in dollars.

3. Smart Ideas for your Home (Automations)
The "Traffic Light" Visual: If you have smart bulbs in the kitchen, have them turn Red during Peak, Yellow during Mid-Peak, and Green during Off-Peak. It reminds the family not to start the dryer or dishwasher.

Heat Pump "Pre-Loading": Set your thermostat to 22°C at 6:00 AM (Off-Peak) and drop it to 19°C at 7:00 AM (Peak). This uses the heat stored in your home to stay warm during the most expensive hours.

EV Charging Lockout: Create an automation that "Disables" your electric vehicle charger the moment sensor.nsp_current_period changes to "Peak" and "Enables" it at 11:00 PM for the lowest rates.

Dehumidifier/Pool Pump Control: These are "silent killers" of your power bill. Set them to run only during "Off-Peak" hours to save hundreds of dollars a year.