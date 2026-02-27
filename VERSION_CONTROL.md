# Project Version Control: NSP Energy Rates

| Version | Status | Release Date | Key Changes |
| :--- | :--- | :--- | :--- |
| **1.0.0** | Obsolete | 2025 | Initial proof of concept. Hard-coded 2025 rates and basic seasonal logic. |
| **2.0.0** | Obsolete | 2026-02-22 | **Major Architecture Shift:** Domain changed to `nsp_energy_v2` to fix HA cache bugs. Added `translations/en.json`. |
| **2.1.1** | Stable | 2026-02-23 | **Bug Fix:** Resolved 500 Internal Server Error by merging `entry.data` and `entry.options` in config flow. |
| **2.1.2** | Stable | 2026-02-25 | **UX Update:** Added comprehensive user instructions and load-shifting automation strategies. |
| **2.1.3** | **Current** | 2026-02-27 | **GitHub Launch:** Configured for `avrillica/nsp_energy`. Merged `utility.py` into `sensor.py`. Added HACS compatibility, MIT License, and Hassfest automation. |
