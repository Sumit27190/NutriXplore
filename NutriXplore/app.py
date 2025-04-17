import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model('NutriXplore/indian_food_classifier_mobilenetv5.keras')

# Class Labels
class_labels = ["burger", "butter_naan", "chai", "chapati", "chole_bhature", 
    "dal_makhani", "dokhla", "fried_rice", "idli", "jalebi",
    "kaathi_rolls", "kadai_paneer", "kulfi", "masala_dosa", "momos",
    "paani_puri", "pakode", "pav_bhaji", "pizza", "samosa"]

# Nutritional Data & Health Suitability
nutritional_info = {
    "burger": {"Calories": 295, "Protein": 17, "Carbs": 29, "Fats": 14, "Diabetes": "❌ High carbs", "Heart": "❌ High fats", "Alternative": "Grilled Paneer Sandwich"},
    "butter_naan": {"Calories": 250, "Protein": 5, "Carbs": 40, "Fats": 8, "Diabetes": "❌ High carbs", "Heart": "⚠ Moderate", "Alternative": "Whole wheat chapati"},
    "chai": {"Calories": 105, "Protein": 3, "Carbs": 12, "Fats": 5, "Diabetes": "⚠ Moderate", "Heart": "✅ Safe", "Alternative": "Green Tea"},
    "chapati": {"Calories": 70, "Protein": 3, "Carbs": 15, "Fats": 1, "Diabetes": "✅ Safe", "Heart": "✅ Safe", "Alternative": "Multigrain Chapati"},
    "chole_bhature": {"Calories": 450, "Protein": 12, "Carbs": 55, "Fats": 20, "Diabetes": "❌ High carbs", "Heart": "❌ High fats", "Alternative": "Chole with Brown Rice"},
    "dal_makhani": {"Calories": 320, "Protein": 14, "Carbs": 32, "Fats": 16, "Diabetes": "⚠ Moderate", "Heart": "❌ High fats", "Alternative": "Dal Tadka"},
    "dokhla": {"Calories": 160, "Protein": 6, "Carbs": 25, "Fats": 5, "Diabetes": "✅ Safe", "Heart": "✅ Safe", "Alternative": "Ragi Dhokla"},
    "fried_rice": {"Calories": 350, "Protein": 7, "Carbs": 55, "Fats": 10, "Diabetes": "❌ High carbs", "Heart": "❌ Fried", "Alternative": "Brown Rice Pulao"},
    "idli": {"Calories": 39, "Protein": 2, "Carbs": 8, "Fats": 0.5, "Diabetes": "✅ Safe", "Heart": "✅ Safe", "Alternative": "Oats Idli"},
    "jalebi": {"Calories": 150, "Protein": 1, "Carbs": 40, "Fats": 8, "Diabetes": "❌ High sugar", "Heart": "❌ High fats", "Alternative": "Baked Sweet Potato"},
    "kaathi_rolls": {"Calories": 300, "Protein": 10, "Carbs": 40, "Fats": 12, "Diabetes": "⚠ Moderate", "Heart": "⚠ Moderate", "Alternative": "Whole Wheat Wrap"},
    "kadai_paneer": {"Calories": 340, "Protein": 18, "Carbs": 20, "Fats": 24, "Diabetes": "⚠ Moderate", "Heart": "❌ High fats", "Alternative": "Tofu Bhurji"},
    "kulfi": {"Calories": 220, "Protein": 4, "Carbs": 25, "Fats": 12, "Diabetes": "❌ High sugar", "Heart": "⚠ Moderate", "Alternative": "Fruit Yogurt"},
    "masala_dosa": {"Calories": 350, "Protein": 8, "Carbs": 45, "Fats": 15, "Diabetes": "⚠ Moderate", "Heart": "⚠ Moderate", "Alternative": "Oats Dosa"},
    "momos": {"Calories": 40, "Protein": 2, "Carbs": 5, "Fats": 1, "Diabetes": "✅ Safe", "Heart": "✅ Safe", "Alternative": "Steamed Vegetable Momos"},
    "paani_puri": {"Calories": 180, "Protein": 3, "Carbs": 25, "Fats": 8, "Diabetes": "❌ High carbs", "Heart": "❌ Fried", "Alternative": "Baked Puri with Sprouts"},
    "pakode": {"Calories": 250, "Protein": 5, "Carbs": 30, "Fats": 15, "Diabetes": "❌ High fats", "Heart": "❌ Fried", "Alternative": "Air Fried Pakora"},
    "pav_bhaji": {"Calories": 400, "Protein": 10, "Carbs": 50, "Fats": 18, "Diabetes": "❌ High carbs", "Heart": "❌ Butter-heavy", "Alternative": "Sprouts Bhaji"},
    "pizza": {"Calories": 285, "Protein": 12, "Carbs": 36, "Fats": 10, "Diabetes": "❌ High carbs", "Heart": "❌ High fats", "Alternative": "Whole Wheat Pizza"},
    "samosa": {"Calories": 132, "Protein": 2, "Carbs": 16, "Fats": 7, "Diabetes": "❌ High fats", "Heart": "❌ Deep-fried", "Alternative": "Baked Samosa"},
}

# UI Styling
st.markdown("""
    <style>
        .main { background-color: #FDF6EC; }
        .title { color: #D32F2F; text-align: center; font-size: 40px; font-weight: bold; }
        .stButton>button { background-color: #a9a9a9; color: white; font-size: 18px; border-radius: 10px; padding: 10px 20px; }
        .nutrition-box { background-color: #FFDAB9; padding: 15px; border-radius: 10px; text-align: center; box-shadow: 2px 2px 8px #888888; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🍽️ NutriXplore - Smart Indian Food Analysis</h1>", unsafe_allow_html=True)
st.subheader("✨ Upload an image to identify the food & analyze its health impact!")

# User selects health condition
health_condition = st.selectbox("🩺 Select your health condition:", ["None", "Diabetes", "Heart Disease", "Weight Loss"], index=0)

# Upload Image
uploaded_file = st.file_uploader("📤 Upload an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image_data = Image.open(uploaded_file)
    st.image(image_data, caption="📷 Uploaded Image", use_column_width=True)
    
    # Preprocess Image
    img = image_data.resize((224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    with st.spinner("🔍 Identifying food..."):
        prediction = model.predict(img_array)
        predicted_class = class_labels[np.argmax(prediction)]
    
    st.success(f"✅ This is **{predicted_class.capitalize()}**!")
    
    # Display Nutritional Info
    if predicted_class in nutritional_info:
        nutrition = nutritional_info[predicted_class]
        st.markdown(f"""
            <div class='nutrition-box'>
                <h3>{predicted_class.upper()}</h3>
                <p><b>Calories:</b> {nutrition['Calories']} kcal</p>
                <p><b>Protein:</b> {nutrition['Protein']}g</p>
                <p><b>Carbs:</b> {nutrition['Carbs']}g</p>
                <p><b>Fats:</b> {nutrition['Fats']}g</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Pie Chart for Nutrient Breakdown
        labels = ["Protein", "Carbs", "Fats"]
        values = [nutrition['Protein'], nutrition['Carbs'], nutrition['Fats']]
        colors = ['#FF9999','#66B3FF','#99FF99']
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
        ax.axis('equal')
        st.pyplot(fig)
        
        # Health Suitability Check
        if health_condition != "None":
            suitability = nutrition.get(health_condition, "✅ Safe")
            st.warning(f"🩺 Suitability for {health_condition}: {suitability}")
            if "❌" in suitability:
                st.info(f"💡 Healthier Alternative: {nutrition['Alternative']}")
    else:
        st.warning("ℹ️ Nutritional info not available for this food item.")

st.write("📌 Built with ❤️")
