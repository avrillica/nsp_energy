# NSP Energy Rates: User Guide & Installation

## 🛠 Installation via HACS (Custom Repository)
Since this is a specialized integration, you can add it to HACS manually:
1. Open **HACS** in Home Assistant.
2. Click the **three dots** in the top right corner and select **Custom repositories**.
3. Paste the URL: `https://github.com/avrillica/nsp_energy`
4. Under 'Category', select **Integration**.
5. Click **Add**, then click the new 'NSP Energy Rates' card and select **Download**.
6. **Restart** Home Assistant.

## ⚙️ Configuration
1. Go to **Settings > Integrations > Add Integration**.
2. Search for **NSP Energy Rates**.
3. **Warning:** The 2026 rates are pre-filled. Recommend not to change unless you know what you are doing, in case NSP changes the rates in the future.

## 📊 Energy Dashboard Setup
If your power monitor provides Watts (W), use the **Riemann sum integral** helper to convert it to Energy (kWh).
1. Go to **Settings > Helpers > Create Helper > Riemann sum integral sensor**.
2. **Input sensor:** Your Power sensor (W). **Method:** Left Riemann sum.
3. In the **Energy Dashboard**, add your new kWh sensor and select `sensor.nsp_current_price` as the price entity.
