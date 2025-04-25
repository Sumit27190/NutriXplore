import streamlit as st
from utils.data import nutritional_info

st.title("📖 Nutrition Guide")

for food, info in nutritional_info.items():
    with st.expander(f"🍴 {food.capitalize()}"):
        st.write(f"**Calories:** {info['Calories']} kcal")
        st.write(f"**Protein:** {info['Protein']}g")
        st.write(f"**Carbs:** {info['Carbs']}g")
        st.write(f"**Fats:** {info['Fats']}g")
        st.write(f"**Diabetes:** {info['Diabetes']}")
        st.write(f"**Heart:** {info['Heart']}")
        st.write(f"**Healthier Alternative:** {info['Alternative']}")
