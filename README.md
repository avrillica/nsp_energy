# NSP Energy Monitor (v2.1.7) 🇨🇦

A custom Home Assistant integration designed specifically for Nova Scotia Power (NSP) customers on the **Time-of-Day (TOD)** tariff. This integration automatically tracks electricity rates based on the official 2026 schedule, including seasonal transitions and weekend/holiday logic.

## 🆕 What's New in v2.1.7
* **March Transition Logic:** Implemented the automatic shift to the **Non-Winter Schedule**. As of March 1st, the integration correctly bypasses the high-cost "Peak" rate and utilizes the "Mid-Peak" rate for weekday daytime hours.
* **Price Accuracy:** Refined decimal precision for the 15% HST calculation to ensure seamless integration with the Home Assistant Energy Dashboard.
* **HACS Ready:** Full support for the HACS Custom Repository workflow.

---

## 📅 2026 Season Schedule
The integration automatically toggles between these schedules so you don't have to:

### ❄️ Winter (December, January, February)
* **Peak ($0.23821):** 7:00 AM – 12:00 PM & 4:00 PM – 11:00 PM (Weekdays)
* **Mid-Peak ($0.19243):** 12:00 PM – 4:00 PM (Weekdays)
* **Off-Peak ($0.11966):** Weekends, Holidays, and Nights (11:00 PM – 7:00 AM)

### 🌿 Non-Winter (March – November) - *Current Season*
* **Mid-Peak ($0.19243):** 7:00 AM – 11:00 PM (Weekdays)
* **Off-Peak ($0.11966):** Weekends, Holidays, and Nights (11:00 PM – 7:00 AM)

---

## 🚀 Installation

### via HACS (Recommended)
1. Open **HACS** > **Integrations**.
2. Click the three dots (top right) > **Custom repositories**.
3. Paste this Repository URL and select **Integration**.
4. Download and **Restart Home Assistant**.

---

## ⚙️ Configuration
Go to **Settings > Devices & Services > Add Integration** and search for **NSP Energy Monitor**.

**Note on Rates:** The integration comes pre-loaded with official 2026 rates. If you use the **Configure** button to change them, a warning will appear. We recommend sticking to the defaults unless NSP officially announces a tariff change.

---

## 📊 Dashboard Usage
Use the `sensor.nsp_current_rate` for your Energy Dashboard "Static Price." For a dynamic visual alert, use this logic in a Mushroom Template Card:

```yaml
icon_color: >
  {% set period = states('sensor.nsp_current_period') %}
  {% if period == 'peak' %} red
  {% elif period == 'mid_peak' %} amber
  {% else %} green
  {% endif %}
