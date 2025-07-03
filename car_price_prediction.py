import streamlit as st
import pickle

st.header("Car Price Prediction App")
col1, col2 = st.columns(2)
with col1:
    year = st.number_input("Enter the year",min_value=1991,max_value=2023)
with col2:
    fuel_type_input = st.selectbox("Select the fuel type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])
col1, col2 = st.columns(2)
with col1:
    seller_type_input = st.selectbox("Select the seller's type", ["Individual","Dealer","Trustmark Deals"])
with col2:
    transmission_type_input = st.selectbox("Select the transmission type",["Manual","Automatic"])
col1, col2 = st.columns(2)
with col1:
    seats = st.selectbox("Select the seats", [4, 5, 7, 9, 11])
with col2:
    km_driven = st.slider("Enter the km driven", 0, 3800000, 5)
col1, col2 = st.columns(2)
with col1:
    mileage = st.slider("Enter the mileage", 0, 150, 2)
with col2:
    engine = st.slider("Enter the engine", 0, 7000, 100)
col1, col2 = st.columns(2)
with col1:
    max_power = st.slider("Enter the max power", 0, 700, 5)
encoding_dict = {
    "seller_type": {"Individual":2, "Dealer": 1,  "Trustmark Deals": 3},
    "fuel_type": {'Diesel': 1, 'Petrol':2, 'CNG':3, 'LPG':4, "Electric":5},
    "transmission_type":{'Manual':1, 'Automatic':2}
}
fuel_type=encoding_dict["fuel_type"][fuel_type_input]
seller_type=encoding_dict["seller_type"][seller_type_input]
transmission_type=encoding_dict["transmission_type"][transmission_type_input]

def model_pred(year, seller_type, km_driven, fuel_type, transmission_type, mileage, engine, max_power, seats,):
    with open('model', 'rb') as f:
        model=pickle.load(f)
        input_features=[[year,seller_type,km_driven,fuel_type,transmission_type,mileage,engine,max_power,seats]]
        return model.predict(input_features)
if st.button("Predict"):
    second_hand_price=model_pred(year,seller_type,km_driven,fuel_type,transmission_type,mileage,engine,max_power,seats)
    st.write("The prediction result is:",str(second_hand_price))