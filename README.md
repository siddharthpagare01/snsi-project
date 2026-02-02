
---

# 🌾 SNSI – Soil Nutrition Advisory System (CLI Based)

## 📌 Project Overview

The **SNSI (Soil Nutrition Suitability Index) CLI Project** is a command-line based decision support system for farmers and agricultural officers.
It analyzes soil parameters provided **manually or via CSV files** and generates **crop-independent soil nutrition advisories** based on an SNSI score.


---

## 🎯 Key Features

* 📥 Accepts **soil data from CSV files**
* ✍️ Allows **manual soil parameter input**
* 📍 Location-based filtering (State → District → Sub-district)
* 🧮 Calculates **SNSI score (0–100)**
* 📊 Classifies soil as *Poor / Moderate / Highly Suitable*
* 🌱 Generates **fertilizer & irrigation advisories**
* 🧑‍🌾 Supports **multiple farmers in one CSV**

---

## 🗂️ Project Structure

```
new-project/
│
├── advisory.py                     # Main CLI application
├── snsi_logic.py                   # SNSI calculation & advisory rules
├── soil_data_maharashtra_500.csv   # Sample dataset (500 farmers)
├── sample_soil.csv                 # Small sample CSV
├── README.md                       # Project documentation
└── __pycache__/
```

---

## 📄 Input CSV Format

Each row represents **one farmer / plot**.

```csv
farmer_id,state,district,sub_district,pH,N,P,K,Zn,organic_carbon,soil_moisture
F001,Maharashtra,Pune,Haveli,6.5,220,18,140,0.40,0.48,18
```

### 📌 Column Description

| Column         | Description           |
| -------------- | --------------------- |
| farmer_id      | Unique farmer ID      |
| state          | State name            |
| district       | District name         |
| sub_district   | Taluka / Sub-district |
| pH             | Soil pH               |
| N              | Nitrogen (kg/ha)      |
| P              | Phosphorus (kg/ha)    |
| K              | Potassium (kg/ha)     |
| Zn             | Zinc (ppm)            |
| organic_carbon | Organic Carbon (%)    |
| soil_moisture  | Soil moisture (%)     |

---

## ⚙️ Prerequisites

* Python **3.8+**
* Linux / WSL / macOS / Windows
* No external libraries required (pure Python)

Check Python version:

```bash
python3 --version
```

---

## ▶️ How to Run the Project

### 🔹 Option 1: Manual Soil Input

```bash
python3 advisory.py
```

Flow:

1. Enter State
2. Enter District
3. Enter Sub-district
4. Choose **manual input**
5. Enter soil parameters

---

### 🔹 Option 2: CSV-Based Advisory (Recommended)

```bash
python3 advisory.py soil_data_maharashtra_500.csv
```

Flow:

1. Enter State
2. Enter District
3. Enter Sub-district
4. Choose **CSV input**
5. System fetches matching data and generates advisory

---

## 🖥️ Sample Output

```
🌾 SOIL NUTRITION ADVISORY REPORT 🌾
-----------------------------------
State              : Maharashtra
District           : Nashik
Sub-district       : Sinnar
SNSI Score         : 61/100
Soil Category      : Moderately Suitable

📌 Recommendations:
 - Apply Nitrogen fertilizer (Urea: 120 kg/ha)
 - Apply Phosphorus (DAP: 60 kg/ha)
 - Apply Zinc Sulphate (25 kg/ha)
```

---

## 🧠 SNSI Logic (Summary)

SNSI is calculated based on:

* Soil pH
* Macronutrients (N, P, K)
* Micronutrients (Zn)
* Organic Carbon
* Soil Moisture

**SNSI Categories:**

| Score  | Category            |
| ------ | ------------------- |
| 0–39   | Poor                |
| 40–69  | Moderately Suitable |
| 70–100 | Highly Suitable     |

---

## ❗ Error Handling

* Invalid location → lists available sub-districts
* Missing CSV → shows correct usage
* Incorrect choice → exits safely

---

## 🚀 Future Enhancements

* Crop-specific advisories (Wheat, Cotton, etc.)
* Machine Learning–based SNSI prediction
* Web / Flask-based UI
* GIS-based district maps
* PDF / CSV advisory export

---


