# NSP Energy Rates: User Guide & Installation (v2.1.6)

## 💡 About the Billing Structure
With the full deployment of smart meters across Nova Scotia, billing has transitioned to **Time-Varying Pricing (TVP)**. This means the cost of electricity is no longer a flat rate; it changes based on *when* you use it. 

This integration is designed to help you track these shifting rates in real-time so you can automate your home (Heat Pumps, EV Chargers, Refoss/Emporia monitors) to run when rates are lowest.

## 🛠 Prerequisites: Energy Monitoring
To use this integration effectively with the Home Assistant Energy Dashboard, you **must have hardware installed** to monitor your electricity consumption. 

**Verified Compatible Hardware:**
* **Refoss EM16:** 16-channel circuit breaker monitor (using CT Clamps).
* **Emporia Vue Gen 2/3:** Whole-home and circuit-level monitoring.
* **Shelly EM / Pro 3EM:** DIN-rail mounted energy meters.

## 🔄 Converting Power (kW) to Energy (kWh)
If your monitoring device provides real-time power (W or kW) but not cumulative energy (kWh), create a helper:
1. **Settings > Helpers > Create Helper > Riemann sum integral sensor**.
2. **Input sensor:** Your real-time Power sensor (e.g., `sensor.refoss_main_power`).
3. **Integration method:** Select **Left Riemann sum** (Critical for accurate inverter/heat pump readings).
4. **Precision:** 3 | **Time unit:** Hours (kWh).

## 📥 Installation via HACS
1. Open **HACS** > **Three dots** > **Custom repositories**.
2. Paste: `https://github.com/avrillica/nsp_energy` | Category: **Integration**.
3. Download and **Restart** Home Assistant.

## 📊 Energy Dashboard Setup
1. **Settings > Dashboards > Energy**.
2. Under **Electricity Grid**, click **Add Consumption**.
3. Select your **kWh sensor**.
4. Choose **"Use an entity with current price"** and select `sensor.nsp_current_price`.
