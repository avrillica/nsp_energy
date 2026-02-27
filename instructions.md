# NSP Energy Rates: User Guide

## Configuration with Energy Monitors
If your monitor provides Watts (W), use the **Riemann sum integral** helper to convert it to Energy (kWh).

1. Go to **Settings > Devices & Services > Helpers**.
2. Click **Create Helper** > **Riemann sum integral sensor**.
3. **Input sensor:** Select your Power sensor (W).
4. **Integration method:** Select **Left Riemann sum**.



## Energy Dashboard Setup
1. Go to **Settings > Dashboards > Energy**.
2. Under **Electricity Grid**, click **Add Consumption**.
3. Select your `_kwh` sensor.
4. Choose **"Use an entity with current price"** and pick `sensor.nsp_current_price`.
