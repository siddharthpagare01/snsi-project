import csv
import sys
from snsi_logic import calculate_snsi, advisory


# -----------------------------
# READ CSV AND FILTER BY LOCATION
# -----------------------------
def read_csv_by_location(file_path, state, district, sub_district):
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (
                row["state"].lower() == state.lower()
                and row["district"].lower() == district.lower()
                and row["sub_district"].lower() == sub_district.lower()
            ):
                return row
    return None


# -----------------------------
# MANUAL SOIL INPUT
# -----------------------------
def manual_input():
    print("\nEnter soil parameters:")

    soil = {
        "pH": float(input("Soil pH: ")),
        "N": float(input("Nitrogen (N): ")),
        "P": float(input("Phosphorus (P): ")),
        "K": float(input("Potassium (K): ")),
        "Zn": float(input("Zinc (Zn): ")),
        "organic_carbon": float(input("Organic Carbon: ")),
        "soil_moisture": float(input("Soil Moisture (%): "))
    }
    return soil


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():
    print("\n🌾 SNSI – Soil Nutrition Advisory System (CLI)")
    print("=============================================")

    # Step 1: Location input
    state = input("Enter State: ").strip()
    district = input("Enter District: ").strip()
    sub_district = input("Enter Sub-district: ").strip()

    # Step 2: Data source choice
    print("\nChoose data source:")
    print("1. Enter soil parameters manually")
    print("2. Use CSV soil data")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        soil = manual_input()

    elif choice == "2":
        if len(sys.argv) != 2:
            print("\n❌ CSV file not provided.")
            print("Usage: python advisory.py <soil_data.csv>")
            sys.exit(1)

        file_path = sys.argv[1]
        data = read_csv_by_location(file_path, state, district, sub_district)

        if not data:
            print("\n❌ No matching soil data found for given location.")
            sys.exit(1)

        soil = {
            "pH": float(data["pH"]),
            "N": float(data["N"]),
            "P": float(data["P"]),
            "K": float(data["K"]),
            "Zn": float(data["Zn"]),
            "organic_carbon": float(data["organic_carbon"]),
            "soil_moisture": float(data["soil_moisture"])
        }

    else:
        print("\n❌ Invalid choice.")
        sys.exit(1)

    # Step 3: SNSI & Advisory
    snsi = calculate_snsi(soil)
    category, advice = advisory(soil, snsi)

    # Step 4: Output
    print("\n🌾 SOIL NUTRITION ADVISORY REPORT 🌾")
    print("-----------------------------------")
    print(f"State              : {state}")
    print(f"District           : {district}")
    print(f"Sub-district       : {sub_district}")
    print(f"SNSI Score         : {snsi}/100")
    print(f"Soil Category      : {category}\n")

    print("📌 Recommendations:")
    if advice:
        for a in advice:
            print(f" - {a}")
    else:
        print(" Soil is well balanced. Maintain current practices.")


if __name__ == "__main__":
    main()
