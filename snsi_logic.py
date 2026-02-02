def calculate_snsi(soil):
    score = 0

    # pH
    if 6.0 <= soil["pH"] <= 7.5:
        score += 15

    # Nitrogen
    if soil["N"] >= 280:
        score += 20
    elif soil["N"] >= 140:
        score += 12

    # Phosphorus
    if soil["P"] >= 22:
        score += 15
    elif soil["P"] >= 11:
        score += 8

    # Potassium
    if soil["K"] >= 280:
        score += 15
    elif soil["K"] >= 140:
        score += 8

    # Zinc
    if soil["Zn"] >= 0.6:
        score += 10
    elif soil["Zn"] >= 0.4:
        score += 5

    # Organic Carbon
    if soil["organic_carbon"] >= 0.5:
        score += 10

    # Soil Moisture
    if soil["soil_moisture"] >= 20:
        score += 15
    elif soil["soil_moisture"] >= 12:
        score += 8

    return min(score, 100)


def advisory(soil, snsi):
    advice = []

    if soil["N"] < 280:
        advice.append("Apply Nitrogen fertilizer (Urea: 120 kg/ha)")

    if soil["P"] < 22:
        advice.append("Apply Phosphorus (DAP: 60 kg/ha)")

    if soil["K"] < 280:
        advice.append("Apply Potassium (MOP: 40 kg/ha)")

    if soil["Zn"] < 0.6:
        advice.append("Apply Zinc Sulphate (25 kg/ha)")

    if soil["organic_carbon"] < 0.5:
        advice.append("Add organic manure / compost")

    if soil["soil_moisture"] < 15:
        advice.append("Irrigation required")

    if snsi >= 70:
        category = "Highly Suitable"
    elif snsi >= 40:
        category = "Moderately Suitable"
    else:
        category = "Poor Soil"

    return category, advice
