#Project 01: Unit Convertor
#Build a google Unit Convertor using Python and Streamlit:

import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: grey;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    h1 {
        color:black;
        text-align: center;
        font-size: 48px;
    }
    st.Button>button{
        background: linear-gradient(45deg, blue, purple);
        color: white;
        font-size: 20px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: transform 0.3s ease;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    st.button:hover {
        background: linear-gradient(45deg, purple, blue);
    }
    st.Button>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        background: rgba(255, 255, 255, 0.1);
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 13px rgba(0, 201, 255, 0.3);
        margin-top: 20px;
    }
    .footer{
        text-align: center;
        padding: 50px;
        font-size: 15px;
        color: black;
    }
    </style>
    """,
unsafe_allow_html=True
)

#title and description:
st.markdown("<h1>Unit Convertor using Python and Streamlit </h1>", unsafe_allow_html=True)
st.write("Easily convert units between different measurements like length, weight, temperature.")

#sidebar menu:
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilometers", "Meters","Centimeters", "Millimeters","Miles","yards","feet","inches"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilometers", "Meters", "Centimeters", "Millimeters","Miles","yards","feet","inches"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
        
 #converted function:
def length_convertor(value, from_unit, to_unit):
    length_unit = {
           "Kilometers":1, "Meters": 1000,"Centimeters":100000, "Millimeters":1000000, 
           "Miles":0.6213, "yards":1.09361, "feet":3.28, "inches":39.3701 
    }
    return (value * length_unit[to_unit]) / length_unit[from_unit]
    


def weight_convertor(value, from_unit, to_unit):
    weight_unit = {
         "Kilograms":1, "Grams":1000, "Milligrams":1000000, "Pounds":2.20462, "Ounces":35.274
      }
    return (value / weight_unit[from_unit]) * weight_unit[to_unit]

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    else:
        return value
    
                
#Button for Conversion:
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result= weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_convertor(value, from_unit, to_unit)
        
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)    
   
st.markdown("<div class='footer'>Developed by Asma Khan </div>", unsafe_allow_html=True)