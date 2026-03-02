# NSP Energy Monitor (v2.1.7) 🇨🇦

A custom Home Assistant integration designed specifically for Nova Scotia Power (NSP) customers on the **Time-of-Day (TOD)** tariff. This integration automatically tracks electricity rates based on the official 2026 schedule, including seasonal transitions and holiday/weekend logic.

## ✨ Features
* **Automatic Season Switching:** Automatically handles the transition between Winter (Dec-Feb) and Non-Winter (Mar-Nov) schedules.
* **2026 Ready:** Pre-loaded with official NSP 2026 rates.
* **Tax Toggle:** Option to display prices with or without the 15% HST included.
* **Live Status:** Provides sensors for `Current Rate` ($/kWh) and `Current Period` (Peak, Mid-Peak, Off-Peak).
* **HACS Compatible:** Easily install and update via the Home Assistant Community Store.

---

## 📅 2026 Schedule Logic
This integration follows the NSP TOD Tariff:
* **Winter (Dec, Jan, Feb):** * **Peak:** 7am–12pm & 4pm–11pm (Weekdays)
    * **Mid-Peak:** 12pm–4pm (Weekdays)
    * **Off-Peak:** Weekends, Holidays, and Nights (11pm–7am)
* **Non-Winter (Mar – Nov):**
    * **Mid-Peak:** 7am–11pm (Weekdays)
    * **Off-Peak:** Weekends, Holidays, and Nights (11pm–7am)

---

## 🚀 Installation

### Option 1: HACS (Recommended)
1. Open **HACS** in Home Assistant.
2. Click the three dots in the top right corner and select **Custom repositories**.
3. Paste the URL of this repository.
4. Select **Integration** as the category and click **Add**.
5. Find **NSP Energy Monitor** in the list and click **Download**.
6. Restart Home Assistant.

### Option 2: Manual
1. Download the `nsp_energy_v2` folder from `custom_components/`.
2. Paste it into your Home Assistant `/config/custom_components/` directory.
3. Restart Home Assistant.

---

## ⚙️ Configuration
1. Go to **Settings > Devices & Services**.
2. Click **Add Integration** and search for **NSP Energy Monitor**.
3. Confirm your rates. **Warning:** We recommend keeping the default 2026 rates unless NSP officially updates their tariffs.
4. Use the **Configure** button at any time to toggle the 15% HST or update prices.

---

## 🛠️ Dashboard Integration
You can use the `sensor.nsp_current_rate` to drive your energy dashboards. To change icon colors based on peak status, we recommend using the **Mushroom Template Card**:
