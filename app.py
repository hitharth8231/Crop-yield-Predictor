import streamlit as st
import pickle
import numpy as np

# Load the trained model
try:
    with open('crop_yield_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please make sure 'crop_yield_model.pkl' is in the directory.")
    st.stop()

# App title and description
st.title("🌾 Crop Yield Prediction App")
st.write("🧠 Predict expected **crop yield (Q/acre)** based on environmental and agricultural factors.")

# Input section
st.header("📋 Enter Input Features")

# Inputs - make sure these match training data features
temperature = st.number_input("🌡️ Temperature (encoded)", min_value=0.0)
rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0.0)
soil_type = st.selectbox("🧪 Soil Type (encoded)", [0, 1, 2])  # Example encoded values
fertilizer = st.number_input("💊 Fertilizer Used (kg/acre)", min_value=0.0)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0)
crop_type = st.selectbox("🌱 Crop Type (encoded)", [0, 1, 2])  # Example encoded values

# Predict button
if st.button("🔍 Predict Yield"):
    try:
        input_data = np.array([[temperature, rainfall, soil_type, fertilizer, humidity, crop_type]])
        prediction = model.predict(input_data)
        st.success(f"🌱 Predicted Crop Yield: **{prediction[0]:.2f} Q/acre**")
    except Exception as e:
        st.error(f"⚠️ Error in prediction: {e}")

# Footer / watermark
st.markdown("""
    <style>
    .footer {
        color: #bbb;
        font-style: italic;
        text-align: center;
        margin-top: 60px;
        font-size: 13px;
    }
    </style>
    <div class="footer">
        🚜 Created by Gurudeep Soni, Hitharth Jain, Aditya Modi, Aditya Bhaskar • Machine Learning Project • 2025 
    </div>
""", unsafe_allow_html=True)


































































































# # app.py

# import streamlit as st
# import pickle
# import numpy as np
# import pandas as pd
# from datetime import datetime
# import altair as alt
# import plotly.express as px
# from track_utils import *

# # Init DB Tables
# create_page_visited_table()
# create_prediction_table()

# # Load Model
# try:
#     model = pickle.load(open('crop_yield_model.pkl', 'rb'))
# except FileNotFoundError:
#     st.error("❌ Model file not found. Please ensure 'crop_yield_model.pkl' is in the same directory.")
#     st.stop()

# # Streamlit App
# st.set_page_config(page_title="Crop Yield Prediction", layout="centered")
# menu = ["🏠 Home", "📊 Monitor", "ℹ️ About"]
# choice = st.sidebar.selectbox("📋 Menu", menu)

# if choice == "🏠 Home":
#     add_page_visited_details("Home", datetime.now(IST))
#     st.title("🌾 Crop Yield Prediction")
#     st.write("📈 Predict expected **crop yield (Q/acre)** based on input features.")

#     temperature = st.text_input("🌡️ Temperature (encoded):")
#     rainfall = st.number_input("🌧️ Rainfall (mm):", min_value=0.0)
#     soil_type = st.selectbox("🧪 Soil Type (encoded):", [0, 1, 2, 3])
#     fertilizer = st.number_input("💊 Fertilizer Used (kg/acre):", min_value=0.0)

#     if st.button("🔍 Predict Yield"):
#         if temperature.strip() != "":
#             try:
#                 temp = float(temperature)
#                 input_data = np.array([[temp, rainfall, soil_type, fertilizer]])
#                 prediction = model.predict(input_data)[0]

#                 add_prediction_details(temp, rainfall, soil_type, fertilizer, prediction, datetime.now(IST))
#                 st.success(f"🌱 Predicted Crop Yield: **{prediction:.2f} Q/acre**")
#             except Exception as e:
#                 st.error(f"⚠️ Error in prediction: {e}")
#         else:
#             st.warning("⚠️ Please enter all input fields.")

# elif choice == "📊 Monitor":
#     add_page_visited_details("Monitor", datetime.now(IST))
#     st.title("📊 Monitoring Dashboard")

#     with st.expander("📌 Page Visits"):
#         visit_data = pd.DataFrame(view_all_page_visited_details(), columns=['Page Name', 'Time of Visit'])
#         st.dataframe(visit_data)

#         visit_count = visit_data['Page Name'].value_counts().rename_axis('Page Name').reset_index(name='Count')
#         bar_chart = alt.Chart(visit_count).mark_bar().encode(x='Page Name', y='Count', color='Page Name')
#         st.altair_chart(bar_chart, use_container_width=True)

#     with st.expander("📊 Yield Predictions"):
#         pred_data = pd.DataFrame(view_all_prediction_details(), columns=['Temperature', 'Rainfall', 'Soil Type', 'Fertilizer', 'Prediction', 'Time of Visit'])
#         st.dataframe(pred_data)

#         pred_chart = px.line(pred_data, x='Time of Visit', y='Prediction', title='Yield Prediction Over Time')
#         st.plotly_chart(pred_chart, use_container_width=True)

# elif choice == "ℹ️ About":
#     add_page_visited_details("About", datetime.now(IST))
#     st.title("ℹ️ About This Project")
#     st.write("This is a machine learning-based application for predicting crop yields based on environmental conditions.")

#     st.markdown("""
#     ### 💡 Features:
#     - 🌡️ Encoded temperature input
#     - 🌧️ Rainfall & fertilizer metrics
#     - 📈 Yield prediction & tracking
#     - 📊 Monitoring dashboard with charts

#     ### 👨‍💻 Team Members:
#     - Gurudeep Soni ✨
#     - Hitharth Jain 🚀
#     - Aashika Pandey 🌸
#     - Ishant Goyal 🔥
#     """)

# st.markdown("""
#     <hr>
#     <div style="text-align: center; font-size: 14px; color: gray;">
#         🚜 <strong>Crop Yield Predictor – Poornima College Project</strong> • 2025
#     </div>
# """, unsafe_allow_html=True)
