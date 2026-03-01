import datetime

# Correct 2026 Rates (as configured in your options)
# PEAK: 0.23821 | MID: 0.19243 | OFF: 0.11966

def get_nsp_period(now):
    month = now.month
    hour = now.hour
    weekday = now.weekday()  # 0=Monday, 6=Sunday

    # SEASON CHECK: Winter is Dec (12), Jan (1), Feb (2)
    is_winter = month in [12, 1, 2]

    # WEEKENDS & HOLIDAYS: Always Off-Peak
    if weekday >= 5:
        return "off_peak"

    # WEEKDAY LOGIC
    if is_winter:
        # Winter Peak: 7-12 & 16-23
        if (7 <= hour < 12) or (16 <= hour < 23):
            return "peak"
        return "off_peak"
    else:
        # Non-Winter (March - November)
        # Peak: 7-12 & 16-23 | Mid: 12-16
        if (7 <= hour < 12) or (16 <= hour < 23):
            return "peak"
        elif (12 <= hour < 16):
            return "mid_peak"
        return "off_peak"

# PRICE CALCULATION
# This ensures the sensor actually updates when the period changes
current_period = get_nsp_period(datetime.datetime.now())
raw_price = config_entry.options.get(f"{current_period}_price")

if config_entry.options.get("include_tax"):
    final_price = float(raw_price) * 1.15
else:
    final_price = float(raw_price)
