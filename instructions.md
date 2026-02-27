# NSP Energy Rates: User Guide & Installation

## 🛠 Prerequisites: Energy Monitoring
To use this integration effectively with the Home Assistant Energy Dashboard, you **must have an energy monitoring device** (e.g., Emporia Vue, Shelly EM, Iotawatt, or a P1 Meter). This integration provides the *price* data, while your hardware provides the *usage* data.

## 🔄 Converting Power (kW) to Energy (kWh)
Most monitoring devices provide real-time power in Watts (W) or Kilowatts (kW). Home Assistant's Energy Dashboard requires cumulative Energy in **kWh**.

If your device does not provide a kWh entity, follow these steps to create one using the **[Riemann sum integral integration](https://www.home-assistant.io/integrations/integration/)**:

1. Go to **Settings > Devices & Services > Helpers**.
2. Click **Create Helper** > **Riemann sum integral sensor**.
3. **Name:** Give it a clear name like "Main House Energy kWh".
4. **Input sensor:** Select your real-time Power sensor (W or kW).
5. **Integration method:** Select **Left Riemann sum**. 
   *Note: Using "Left" is critical for power data to avoid over-calculating during spikes.*
6. **Precision:** Set to 3.
7. **Time unit:** Hours (kWh).



## 📥 Installation via HACS (Custom Repository)
1. Open **HACS** in Home Assistant.
2. Click the **three dots** (top right) > **Custom repositories**.
3. Paste: `https://github.com/avrillica/nsp_energy`
4. Category: **Integration**.
5. Click **Add**, then find 'NSP Energy Rates' and select **Download**.
6. **Restart** Home Assistant.

## 📊 Energy Dashboard Setup
1. Go to **Settings > Dashboards > Energy**.
2. Under **Electricity Grid**, click **Add Consumption**.
3. Select your newly created **kWh sensor**.
4. Choose **"Use an entity with current price"** and pick `sensor.nsp_current_price`.
