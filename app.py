import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
import re

# Load trained model
with open("flight_price_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

st.title("Flight Fare Prediction")

# Sidebar inputs
st.sidebar.header("Input Flight Details")

# Departure Date and Time
dep_date = st.sidebar.date_input("Departure Date")
# Departure Time
dep_time = st.sidebar.text_input("Departure Time (HH:MM, 24-hour format)", "00:00")


# Arrival Date and Time
arrival_date = st.sidebar.date_input("Arrival Date")
arrival_time = st.sidebar.text_input("Arrival Time (HH:MM, 24-hour format)", "01:00")

# Validate if Departure Time and Arrival Time are valid
def validate_time_format(time_str):
    return bool(re.match(r"^[0-2]?[0-9]:[0-5][0-9]$", time_str))

# Validate fields
if dep_time and not validate_time_format(dep_time):
    st.sidebar.error("Departure Time should be in HH:MM format (24-hour time).")
if arrival_time and not validate_time_format(arrival_time):
    st.sidebar.error("Arrival Time should be in HH:MM format (24-hour time).")

if not dep_date or not dep_time or not arrival_date or not arrival_time:
    st.sidebar.error("Please fill all the fields. No field should be empty.")

# Ensure arrival date is after departure date
if arrival_date < dep_date:
    st.sidebar.error("Arrival date cannot be before Departure date.")
elif arrival_date == dep_date:
    dep_datetime = datetime.combine(dep_date, datetime.strptime(dep_time, "%H:%M").time())
    arrival_datetime = datetime.combine(arrival_date, datetime.strptime(arrival_time, "%H:%M").time())
    if arrival_datetime <= dep_datetime:
        st.sidebar.error("Arrival time must be after Departure time.")

# Airline, Source, Destination, Stops
airline = st.sidebar.selectbox("Airline", ["IndiGo", "Air India", "Jet Airways", "SpiceJet", "Vistara"])
source = st.sidebar.selectbox("Source", ["Delhi", "Kolkata", "Mumbai", "Chennai", "Bangalore"])
destination = st.sidebar.selectbox("Destination", ["Cochin", "Bangalore", "Delhi", "Hyderabad", "Kolkata"])

# Stops as a slider (valid values 0 to 3)
stops = st.sidebar.slider("Number of Stops", 0, 3, 1)

# Feature Engineering
journey_day = dep_date.day
journey_month = dep_date.month

# Convert times to datetime
dep_datetime = datetime.combine(dep_date, datetime.strptime(dep_time, "%H:%M").time())
arrival_datetime = datetime.combine(arrival_date, datetime.strptime(arrival_time, "%H:%M").time())
duration = arrival_datetime - dep_datetime
duration_hours = int(duration.total_seconds() // 3600)
duration_mins = int((duration.total_seconds() % 3600) // 60)

# One-Hot Encoding (same as training)
airline_dict = {"IndiGo": 0, "Air India": 1, "Jet Airways": 2, "SpiceJet": 3, "Vistara": 4}
source_dict = {"Delhi": 0, "Kolkata": 1, "Mumbai": 2, "Chennai": 3, "Bangalore": 4}
destination_dict = {"Cochin": 0, "Bangalore": 1, "Delhi": 2, "Hyderabad": 3, "Kolkata": 4}

# Create input dataframe
input_data = pd.DataFrame([{
    "Airline": airline_dict[airline],
    "Source": source_dict[source],
    "Destination": destination_dict[destination],
    "Stops": stops,
    "Journey_day": journey_day,
    "Journey_month": journey_month,
    "Dep_Time_hour": dep_datetime.hour,
    "Dep_Time_minute": dep_datetime.minute,
    "Arrival_Time_hour": arrival_datetime.hour,
    "Arrival_Time_minute": arrival_datetime.minute,
    "Duration_hours": duration_hours,
    "Duration_mins": duration_mins
}])

# **Make sure all feature names exist**
# Load training feature names from model (if available)
if hasattr(model, "feature_names_in_"):
    expected_features = list(model.feature_names_in_)
    input_data = input_data.reindex(columns=expected_features, fill_value=0)  # Ensure column order matches

# Predict
if st.sidebar.button("Predict Fare"):
    fare_prediction = model.predict(input_data)
    st.success(f"Predicted Fare: ₹{fare_prediction[0]:.2f}")
