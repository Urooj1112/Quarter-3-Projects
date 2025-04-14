import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Conversion Units ---
units_in_meters = {
    'Foot (ft)': 0.3048,
    'Yard (yd)': 0.9144,
    'Mile (mi)': 1609.34,
    'Inch (in)': 0.0254,
    'Kilometer (km)': 1000.0,
    'Meter (m)': 1.0,
    'Centimeter (cm)': 0.01,
    'Millimeter (mm)': 0.001,
    'Micrometer (um)': 1e-6,
    'Nanometer (nm)': 1e-9
}

# --- History Storage ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Conversion Function ---
def convert_length(value, from_unit, to_unit):
    meters = value * units_in_meters[from_unit]
    return meters / units_in_meters[to_unit]

# Streamlit settings
st.set_page_config(page_title="Unit Converter", page_icon="U.S", layout="centered")

# --- Branding ---
st.markdown("""
    <h1 style='text-align: center; background: linear-gradient(to right, #2c3e50, #3498db); 
    -webkit-background-clip: text; color: transparent;'>StatSwap: Converting Units with Data Precision</h1>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; font-size: 16px; color: black;">
        Effortlessly switch between modern and classic length units — instant, intuitive, and crafted for precision!
    </div>
""", unsafe_allow_html=True)

# --- Input Section ---
with st.form("converter_form"):
    value = st.number_input("Enter a value", min_value=0.0, format="%.6f")
    from_unit = st.selectbox("From unit", list(units_in_meters.keys()))
    to_unit = st.selectbox("To unit", list(units_in_meters.keys()))
    submit = st.form_submit_button("Convert Now")

# --- Conversion Result ---
if submit:
    if from_unit == to_unit:
        st.warning("⚠️ Choose two different units.")
    else:
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value:,.6f} {from_unit} = {result:,.6f} {to_unit}")

        # Save history
        st.session_state.history.append({
            "Value": value,
            "From": from_unit,
            "To": to_unit,
            "Result": result
        })

# --- History Section ---
if st.session_state.history:
    st.markdown("### Conversion History")
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True)

    # --- Chart ---
    fig, ax = plt.subplots()
    ax.plot(df["Result"], marker='o', color='#FF6363')
    ax.set_title("Result Trend")
    ax.set_xlabel("Conversions")
    ax.set_ylabel("Converted Value")
    st.pyplot(fig)

# --- Footer ---
st.markdown("""
    <div style="text-align: center; font-size: 14px; color: gray;">
        Designed by Urooj Saeed | A Creative Journey in Every Click
    </div>
""", unsafe_allow_html=True)
