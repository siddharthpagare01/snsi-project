import csv
import sys
from snsi_logic import calculate_snsi, advisory


# -----------------------------
# READ CSV AND FILTER BY FARMER + LOCATION
# -----------------------------
def read_csv_by_farmer(file_path, farmer_id, state, district, sub_district):
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if (
                row["farmer_id"] == farmer_id
                and row["state"].lower() == state.lower()
                and row["district"].lower() == district.lower()
                and row["sub_district"].lower() == sub_district.lower()
            ):
                return row
    return None


# -----------------------------
# MANUAL SOIL INPUT
# -----------------------------
def manual_input():
    print("\nEnter soil parameters manually:")
    return {
        "pH": float(input("Soil pH: ")),
        "N": float(input("Nitrogen (N): ")),
        "P": float(input("Phosphorus (P): ")),
        "K": float(input("Potassium (K): ")),
        "Zn": float(input("Zinc (Zn): ")),
        "organic_carbon": float(input("Organic Carbon: ")),
        "soil_moisture": float(input("Soil Moisture (%): "))
    }


# -----------------------------
# MAIN PROGRAM (CONTINUOUS MODE)
# -----------------------------
def main():
    print("\n🌾 SNSI – Soil Nutrition Advisory System (CLI)")
    print("=============================================")

    while True:
        # Step 1: Farmer & Location Input
        farmer_id = input("\nEnter Farmer ID: ").strip()
        state = input("Enter State: ").strip()
        district = input("Enter District: ").strip()
        sub_district = input("Enter Sub-district: ").strip()

        # Step 2: Data Source Selection
        print("\nChoose data source:")
        print("1. Enter soil parameters manually")
        print("2. Fetch soil data from CSV")
        print("3. Exit")

        choice = input("Enter choice (1 / 2 / 3): ").strip()

        if choice == "3":
            print("\n✅ Exiting SNSI System. Thank you!")
            break

        if choice == "1":
            soil = manual_input()

        elif choice == "2":
            if len(sys.argv) != 2:
                print("\n❌ CSV file not provided.")
                print("Usage: python advisory.py <soil_data.csv>")
                continue

            file_path = sys.argv[1]
            data = read_csv_by_farmer(
                file_path, farmer_id, state, district, sub_district
            )

            if not data:
                print("\n❌ No soil data found for given farmer and location.")
                continue

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
            print("\n❌ Invalid choice. Try again.")
            continue

        # Step 3: SNSI Calculation & Advisory
        snsi = calculate_snsi(soil)
        category, advice = advisory(soil, snsi)

        # Step 4: Report
        print("\n🌾 SOIL NUTRITION ADVISORY REPORT 🌾")
        print("-----------------------------------")
        print(f"Farmer ID          : {farmer_id}")
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
