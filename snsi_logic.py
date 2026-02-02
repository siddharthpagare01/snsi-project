# -----------------------------
# NORMALIZATION FUNCTION
# -----------------------------
def normalize(value, xmin, xopt, xmax):
    """
    Normalize a soil parameter to 0–1 scale
    Penalizes deficiency and excess
    """
    if value < xmin:
        return 0.0
    elif xmin <= value < xopt:
        return (value - xmin) / (xopt - xmin)
    elif xopt <= value <= xmax:
        return 1.0
    else:
        return max(0.0, (xmax - value) / (xmax - xopt))


# -----------------------------
# MATHEMATICAL SNSI CALCULATION
# -----------------------------
def calculate_snsi(soil):
    """
    Calculates SNSI using weighted normalized parameters
    Returns SNSI score (0–100)
    """

    parameters = {
        "pH": {
            "value": soil["pH"],
            "min": 5.5,
            "opt": 6.8,
            "max": 8.0,
            "weight": 0.15
        },
        "N": {
            "value": soil["N"],
            "min": 140,
            "opt": 280,
            "max": 400,
            "weight": 0.20
        },
        "P": {
            "value": soil["P"],
            "min": 11,
            "opt": 22,
            "max": 40,
            "weight": 0.15
        },
        "K": {
            "value": soil["K"],
            "min": 140,
            "opt": 280,
            "max": 450,
            "weight": 0.15
        },
        "Zn": {
            "value": soil["Zn"],
            "min": 0.4,
            "opt": 0.6,
            "max": 1.2,
            "weight": 0.10
        },
        "organic_carbon": {
            "value": soil["organic_carbon"],
            "min": 0.3,
            "opt": 0.6,
            "max": 1.2,
            "weight": 0.10
        },
        "soil_moisture": {
            "value": soil["soil_moisture"],
            "min": 10,
            "opt": 20,
            "max": 35,
            "weight": 0.15
        }
    }

    snsi_score = 0.0

    for p in parameters.values():
        norm = normalize(
            p["value"],
            p["min"],
            p["opt"],
            p["max"]
        )
        snsi_score += norm * p["weight"]

    return round(snsi_score * 100, 2)


# -----------------------------
# MATHEMATICAL ADVISORY LOGIC
# -----------------------------
def advisory(soil, snsi):
    advice = []

    # --- Nitrogen ---
    N_opt = 280
    if soil["N"] < N_opt:
        gap = N_opt - soil["N"]
        urea = round(gap * 2.17, 1)   # 46% N in Urea
        advice.append(f"Apply Nitrogen: Urea ≈ {urea} kg/ha")

    # --- Phosphorus ---
    P_opt = 22
    if soil["P"] < P_opt:
        gap = P_opt - soil["P"]
        dap = round(gap * 2.5, 1)
        advice.append(f"Apply Phosphorus: DAP ≈ {dap} kg/ha")

    # --- Potassium ---
    K_opt = 280
    if soil["K"] < K_opt:
        gap = K_opt - soil["K"]
        mop = round(gap * 1.7, 1)
        advice.append(f"Apply Potassium: MOP ≈ {mop} kg/ha")

    # --- Zinc ---
    Zn_opt = 0.6
    if soil["Zn"] < Zn_opt:
        advice.append("Apply Zinc Sulphate ≈ 25 kg/ha")

    # --- Organic Carbon ---
    if soil["organic_carbon"] < 0.6:
        advice.append("Apply organic manure / compost (FYM or vermicompost)")

    # --- Soil Moisture ---
    if soil["soil_moisture"] < 15:
        advice.append("Irrigation required to maintain optimal moisture")

    # --- pH correction ---
    if soil["pH"] < 5.5:
        advice.append("Apply agricultural lime to increase soil pH")
    elif soil["pH"] > 8.0:
        advice.append("Apply gypsum / organic matter to reduce alkalinity")

    # --- Soil Category ---
    if snsi >= 75:
        category = "Highly Suitable"
    elif snsi >= 50:
        category = "Moderately Suitable"
    else:
        category = "Poor Soil"

    return category, advice
