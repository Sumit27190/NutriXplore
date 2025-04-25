# data.py

food_classes = [
    "burger",           # 0
    "butter_naan",      # 1
    "chai",             # 2
    "chapati",          # 3
    "chole_bhature",    # 4
    "dal_makhani",      # 5
    "dhokla",           # 6
    "fried_rice",       # 7
    "idli",             # 8
    "jalebi",           # 9
    "kaathi_rolls",     # 10
    "kadai_paneer",     # 11
    "kulfi",            # 12
    "masala_dosa",      # 13
    "momos",            # 14
    "paani_puri",       # 15
    "pakode",           # 16
    "pav_bhaji",        # 17
    "pizza",            # 18
    "samosa"            # 19
]


# utils/data.py
class_labels = [
    "burger", "butter_naan", "chai", "chapati", "chole_bhature", 
    "dal_makhani", "dhokla", "fried_rice", "idli", "jalebi", 
    "kaathi_rolls", "kadai_paneer", "kulfi", "masala_dosa", 
    "momos", "paani_puri", "pakode", "pav_bhaji", "pizza", "samosa"
]





# nutrients.py

nutritional_info ={
    "burger": {"Calories": 295, "Protein": 17, "Carbs": 29, "Fats": 14, "Diabetes": "⚠ Moderate carbs", "Heart": "❌ High saturated fats", "Alternative": "Whole Wheat Veggie Burger"},
    "butter_naan": {"Calories": 250, "Protein": 5, "Carbs": 40, "Fats": 8, "Diabetes": "❌ High glycemic carbs", "Heart": "⚠ Moderate saturated fats", "Alternative": "Whole wheat chapati"},
    "chai": {"Calories": 105, "Protein": 3, "Carbs": 12, "Fats": 5, "Diabetes": "⚠ Moderate sugar", "Heart": "⚠ Moderate saturated fats", "Alternative": "Green Tea (unsweetened)"},
    "chapati": {"Calories": 70, "Protein": 3, "Carbs": 15, "Fats": 1, "Diabetes": "✅ Low glycemic carbs", "Heart": "✅ Low saturated fats", "Alternative": "Multigrain Chapati"},
    "chole_bhature": {"Calories": 450, "Protein": 12, "Carbs": 55, "Fats": 20, "Diabetes": "❌ High glycemic carbs", "Heart": "❌ High saturated and trans fats (deep-fried)", "Alternative": "Chole with Brown Rice"},
    "dal_makhani": {"Calories": 320, "Protein": 14, "Carbs": 32, "Fats": 16, "Diabetes": "⚠ Moderate glycemic carbs", "Heart": "❌ High saturated fats", "Alternative": "Dal Tadka (less butter/oil)"},
    "dhokla": {"Calories": 160, "Protein": 6, "Carbs": 25, "Fats": 5, "Diabetes": "✅ Moderate glycemic carbs", "Heart": "✅ Low saturated fats", "Alternative": "Ragi Dhokla"},
    "fried_rice": {"Calories": 350, "Protein": 7, "Carbs": 55, "Fats": 10, "Diabetes": "❌ High glycemic carbs", "Heart": "❌ High saturated and trans fats (fried)", "Alternative": "Brown Rice Pulao with more vegetables"},
    "idli": {"Calories": 65, "Protein": 2, "Carbs": 13, "Fats": 1, "Diabetes": "✅ Low glycemic carbs", "Heart": "✅ Low saturated fats", "Alternative": "Oats Idli"},
    "jalebi": {"Calories": 150, "Protein": 1.5, "Carbs": 38, "Fats": 8, "Diabetes": "❌ Very high sugar", "Heart": "❌ High saturated fats", "Alternative": "Small portion of fresh fruit"},
    "kaathi_rolls": {"Calories": 300, "Protein": 10, "Carbs": 40, "Fats": 12, "Diabetes": "⚠ Moderate glycemic carbs", "Heart": "⚠ Moderate saturated fats", "Alternative": "Whole Wheat Vegetable Wrap"},
    "kadai_paneer": {"Calories": 340, "Protein": 18, "Carbs": 20, "Fats": 24, "Diabetes": "⚠ Moderate glycemic carbs", "Heart": "❌ High saturated fats", "Alternative": "Tofu Bhurji (less oil)"},
    "kulfi": {"Calories": 220, "Protein": 4, "Carbs": 25, "Fats": 12, "Diabetes": "❌ High sugar", "Heart": "⚠ Moderate saturated fats", "Alternative": "Fruit Yogurt (low sugar)"},
    "masala_dosa": {"Calories": 350, "Protein": 8, "Carbs": 45, "Fats": 15, "Diabetes": "⚠ Moderate glycemic carbs", "Heart": "⚠ Moderate saturated fats", "Alternative": "Oats Dosa with less potato filling"},
    "momos": {"Calories": 70, "Protein": 3, "Carbs": 10, "Fats": 2, "Diabetes": "✅ Moderate glycemic carbs", "Heart": "✅ Low saturated fats (steamed)", "Alternative": "Steamed Vegetable Momos (whole wheat)"},
    "paani_puri": {"Calories": 180, "Protein": 3, "Carbs": 25, "Fats": 8, "Diabetes": "❌ High glycemic carbs", "Heart": "❌ High saturated and trans fats (fried)", "Alternative": "Baked Puri with Sprouts"},
    "pakode": {"Calories": 250, "Protein": 5, "Carbs": 30, "Fats": 15, "Diabetes": "❌ High fats", "Heart": "❌ High saturated and trans fats (fried)", "Alternative": "Air Fried Vegetable Fritters"},
    "pav_bhaji": {"Calories": 400, "Protein": 10, "Carbs": 50, "Fats": 18, "Diabetes": "❌ High glycemic carbs", "Heart": "❌ High saturated fats (butter-heavy)", "Alternative": "Sprouts Bhaji with whole wheat bread/pav (less butter)"},
    "pizza": {"Calories": 285, "Protein": 12, "Carbs": 36, "Fats": 10, "Diabetes": "❌ High glycemic carbs", "Heart": "⚠ Moderate saturated fats", "Alternative": "Whole Wheat Pizza with more vegetables and less cheese"},
    "samosa": {"Calories": 132, "Protein": 2, "Carbs": 16, "Fats": 7, "Diabetes": "❌ High fats", "Heart": "❌ High saturated and trans fats (deep-fried)", "Alternative": "Baked Samosa (whole wheat)"}
}
