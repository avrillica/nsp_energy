NSP Energy Rates: User Guide & Setup

1. Why use this in Home Assistant?
Nova Scotia Power TOD rates vary by hour. This integration tracks those rates so you can automate your home to save money.

2. Configuration with Energy Monitors
Step A: Convert Watts to kWh
If your monitor (Emporia, Shelly, etc.) provides Watts, you must convert it to Energy (kWh) to calculate cost.

Go to Settings > Devices & Services > Helpers.

Click Create Helper > Riemann sum integral sensor.

Input sensor: Select your Power sensor (W).

Integration method: Select Left Riemann sum.

Step B: Link to the Energy Dashboard

Go to Settings > Dashboards > Energy.

Under Electricity Grid, click Add Consumption.

Select your new _kwh sensor.

Choose "Use an entity with current price" and select sensor.nsp_current_price.
