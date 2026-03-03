# NSP Energy Monitor (v2.1.8)

A custom Home Assistant integration for **Nova Scotia Power (NSP)** customers on the **Time-of-Day (TOD)** rate plan. This integration provides real-time pricing and period tracking based on the official 2026 rate schedule.

## 🌟 Key Features
* **Full UI Configuration:** No YAML required. Add and configure prices directly from the Home Assistant Integrations page.
* **Automatic Season Switching:** Seamlessly transitions between Winter (Dec–Feb) and Non-Winter (Mar–Nov) schedules.
* **5 Core Sensors:** Reliable, real-time tracking of prices and periods.
* **2026 Optimized:** Pre-configured with the latest NSP tariff rates.

## 📊 Sensors Included
This integration provides exactly 5 high-reliability sensors:
1.  **NSP Current Price:** The current cost per kWh (including optional 15% tax).
2.  **NSP Current Period:** Displays if you are currently in `off_peak` or `mid_peak`.
3.  **NSP Next Price:** Forecasts the price for the upcoming hour.
4.  **NSP Next Period:** Forecasts the upcoming rate period.
5.  **NSP Tax Active:** A binary "Yes/No" sensor confirming if the 15% tax is being applied to displayed prices.

## 📅 2026 Schedule Logic
The integration follows the official NSP TOD schedule:

### Non-Winter (Current: March 1 – November 30)
* **Weekdays:**
    * **7:00 AM – 11:00 PM:** Mid-Peak ($0.19243/kWh)
    * **11:00 PM – 7:00 AM:** Off-Peak ($0.11966/kWh)
* **Weekends & Holidays:** Off-Peak 24/7.

### Winter (December 1 – February 28)
* **Weekdays:** Includes On-Peak ($0.23821/kWh) during morning and evening surges.
* **Weekends & Holidays:** Off-Peak 24/7.

## 🚀 Installation

1.  Copy the `nsp_energy_v2` folder into your `custom_components` directory.
2.  **Restart Home Assistant.**
3.  In the HA UI, go to **Settings > Devices & Services > Add Integration**.
4.  Search for **NSP Energy Monitor** and follow the prompts.

## 🔧 Configuration
You can update your rates at any time by clicking **Configure** on the integration card. 
> **Note:** We recommend keeping the default 2026 rates unless NSP announces a mid-year tariff change.

---
*Disclaimer: This integration is a community project and is not affiliated with or endorsed by Nova Scotia Power.*
