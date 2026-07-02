import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl

# model = pkl.load(open("oil_prob_xgb.pkl","rb"))
from pathlib import Path
import pickle as pkl

BASE_DIR = Path(__file__).resolve().parent
from xgboost import XGBClassifier

model = XGBClassifier(enable_categorical=True)
model.load_model(BASE_DIR / "oil_prob_xgb.json")
scaler = pkl.load(open(BASE_DIR / "scaler.pkl", "rb"))
feature_columns = pkl.load(open(BASE_DIR / "feature_columns.pkl", "rb"))


st.set_page_config(
    page_title="Oil Presence Prediction",
    page_icon="🛢",
    layout="wide"
)

st.title(
    "Oil Presence Prediction"
)
st.warning(
    """
⚠ **Disclaimer**

The prediction model has been trained using a **synthetic geological dataset** and therefore should **not** be considered a substitute for professional reservoir evaluation or exploration decisions.

Predictions, probabilities, and engineering indicators are intended only to demonstrate the application of **Machine Learning in Petroleum Engineering**. Actual reservoir behaviour may differ significantly from the values predicted by this model.
"""
)
st.markdown(
    """
Predict the probability of **oil occurrence** using
geological, seismic and reservoir engineering properties.

The prediction model is based on a **Tuned XGBoost Classifier**
combined with **Petroleum Engineering Feature Engineering**.
"""
)
st.divider()

st.write(
    """
This application predicts the
probability of **oil occurrence**
using Machine Learning.

**Model Used**

Tuned XGBoost

**Dataset**

Synthetic Geological Dataset

**Application**

Reservoir Screening &
Exploration Analysis
"""
)

st.sidebar.markdown("---")

st.sidebar.header("Feature Information")

with st.sidebar.expander("Rock Type"):
    st.write("""
**Sandstone**
- Excellent Reservoir
- Features relatively high porosity (10–30%) and good permeability, allowing fluids to flow. In seismic surveys, they exhibit moderate-to-high acoustic impedance  

**Limestone**
- Moderate Reservoir
- Tends to have complex "dual porosity" (matrix pores plus fractures and vugs). Density and sonic velocities are noticeably higher than in sandstones.

**Shale**
- Low Reservoir Quality
-: Exhibits very low permeability but high porosity . It has high electrical conductivity and low sonic velocity.
""")
    
with st.sidebar.expander("Porosity"):
    st.write(
        """
Porosity is the ratio of pore (void) volume to the bulk volume(total volume)
        porosity = ((total volume) - (grain volume))/(total volume)
"""
    )

with st.sidebar.expander("Permeability"):
    st.write(
        """
    Permeability in the petroleum industry refers to the ability of a rock or sediment to transmit fluids (such as oil, gas, or water) through its interconnected pore network
        """
    )
with st.sidebar.expander("Trap Type"):
    st.write("""
• Anticline

• Fault

• Dome

• Unknown
""")
    
with st.sidebar.expander("Seismic Score"):
    st.write("""
    It is usually a composite score derived from seismic survey data to indicate how likely a subsurface location is to contain hydrocarbons.
Higher seismic score indicates
a higher probability of
hydrocarbon accumulation.
""")  
    
with st.sidebar.expander("Reservoir Depth"):
    st.write("""
Typical depth

500 m – 5000 m
""")
st.sidebar.markdown("---")

st.sidebar.info("""
Developed using

• Streamlit

• XGBoost

• Petroleum Engineering

• Machine Learning
""")


st.subheader("📌 About This Project")

st.write("""
This application predicts the likelihood of oil occurrence using
geological and reservoir engineering properties.

The prediction pipeline combines geological measurements,
machine learning, and petroleum engineering concepts.

In addition to the raw input features, the application
automatically computes several engineered reservoir properties,
including:

- Reservoir Quality
- Pore Connectivity Index
- Reservoir Flow Capacity
- Hydrocarbon Prospect Score

These engineered parameters improve prediction quality by
capturing important reservoir characteristics used in petroleum
engineering.
""")

st.subheader("About the Engineered Features")

st.info(
"""
The application computes several **engineered reservoir indicators**
to help the Machine Learning model better understand relationships
between geological properties.

These indicators are **simplified engineering-inspired metrics**
created specifically for the project.

They are **not standard petroleum engineering equations**
and should not be interpreted as field-calibrated engineering calculations.

Their primary purpose is to improve the predictive capability of the machine learning model by combining multiple geological variables into meaningful features.
"""
)
st.sidebar.header("DESCRIPTION")
with st.sidebar.expander("Reservoir Quality"):
    st.write("""


Reservoir Quality is a rule-based classification
created using porosity and permeability.

Excellent
• Porosity ≥ 20%
• Permeability ≥ 300 mD

Good
• Porosity ≥ 15%
• Permeability ≥ 150 mD

Average
• Porosity ≥ 10%
• Permeability ≥ 50 mD

Poor
• Below the above thresholds

This is a simplified engineering classification
used for this project.
""")
    
with st.sidebar.expander("Pore Connectivity Index"):
    st.write("""

Formula

Square root of (Porosity × Permeability)

Purpose

Represents the combined influence of
storage capacity and fluid connectivity.

Higher values generally indicate
better reservoir characteristics.
"""

        )
    
with st.sidebar.expander("Reservoir Flow Capacity"):
    st.write("""

Formula

(Permeability × Porosity)
/ Reservoir Depth

Purpose

Provides a simplified indicator of
potential reservoir productivity.

Greater permeability and porosity
increase flow capacity,
while greater depth reduces it.
""")

with st.sidebar.expander("Hydrocarbon Prospect Score"):
    st.write("""

Formula

35% (Normalized Porosity) +

35% (Normalized Permeability)+

30% (Seismic Score)

Purpose

A simplified composite score combining
reservoir properties and seismic interpretation
to estimate exploration potential.

This score was specifically designed for
machine learning feature engineering and
is **not an industry-standard petroleum metric**.
""")

st.divider()

left_col, right_col = st.columns([1,1])

with left_col:

    st.header("Geological Inputs")

    rock_type = st.selectbox(
        "ROCK TYPE",
        ["Sandstone","Limestone","Shale"]
    )

    trap_type = st.selectbox(
        "TRAP TYPE",
        ["Anticline","Fault","Dome","Unknown"]
    )
    porosity = st.slider(
        "Porosity(in %)",
        min_value=0.0,
        max_value=30.0,
        value=15.0,
        step=0.1)

    
    permeability = st.number_input(
    "Permeability (mD)",
    min_value=1.0,
    max_value=1000.0,
    value=250.0)

    seismic_score = st.slider(
    "Seismic Score",
    min_value=0.0,
    max_value=1.0,
    value=0.50,
    step=0.01)

    distance = st.number_input(
    "Distance to Oil Field (km)",
    min_value=0.0,
    max_value=20.0,
    value=5.0)

    depth = st.number_input(
    "Estimated Reservoir Depth (m)",
    min_value=500,
    max_value=5000,
    value=2500)

    st.write("")

    predict = st.button("🔍 Predict Oil Presence")


if predict:

    if porosity >= 20 and permeability >= 300:
        reservoir_quality = "Excellent"

    elif porosity >= 15 and permeability >= 150:
            reservoir_quality = "Good"

    elif porosity >= 10 and permeability >= 50:
        reservoir_quality = "Average"

    else:
        reservoir_quality = "Poor"

    pore_connectivity = (
        np.sqrt(porosity * permeability)
    )

    reservoir_flow_capacity = (
        (permeability * porosity)/depth
    )

    poro = porosity/30
    perm = permeability/1000

    hydrocarbon_prospect_score = (
        0.35 * poro +
    0.35 * perm +
    0.30 * seismic_score
    )

    input_df = pd.DataFrame({

        "Porosity": [porosity],

        "Permeability": [permeability],

        "Seismic_Score": [seismic_score],

        "Proximity_to_Oil_Field": [distance],

        "Estimated_Reservoir_Depth": [depth],

        "Reservoir_Quality": [reservoir_quality],

        "Pore_Connectivity_Index": [pore_connectivity],

        "Reservoir_Flow_Capacity": [reservoir_flow_capacity],

        "Hydrocarbon_Prospect_Score": [hydrocarbon_prospect_score],

        "Rock_Type": [rock_type],

        "Trap_Type": [trap_type]

    })


    input_df = pd.get_dummies(

    input_df,

    columns=[
        "Rock_Type",
        "Trap_Type",
        "Reservoir_Quality"
    ],

    dtype=int)

    for col in feature_columns:

        if col not in input_df.columns:

            input_df[col] = 0

    input_df = input_df[feature_columns]
    scaled_cols = [
    "Pore_Connectivity_Index",
    "Reservoir_Flow_Capacity",
    "Hydrocarbon_Prospect_Score"
]
    input_df[scaled_cols] = scaler.transform(input_df[scaled_cols])
    input_df = input_df[feature_columns]
    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    prediction_results = {

        "prediction": prediction,

        "probability": probability,

        "reservoir_quality": reservoir_quality,

        "pore_connectivity": pore_connectivity,

        "reservoir_flow": reservoir_flow_capacity,


    }







    




with right_col:

    st.header("📊 Prediction Results")

    if predict:

        probability_percent = probability * 100

    

        if prediction == 1:

            st.success("🟢 Oil Presence Detected")

        else:

            st.error("🔴 No Significant Oil Presence")

    

        st.subheader("Prediction Confidence")

        st.progress(int(probability_percent))

        st.metric(
        "Probability of Oil Presence",
        f"{probability_percent:.2f}%"
    )

        st.divider()

    
        st.subheader("🛢 Reservoir Engineering Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
            "Reservoir Quality",
            reservoir_quality
        )

            st.metric(
            "Hydrocarbon Prospect Score",
            f"{hydrocarbon_prospect_score:.3f}"
        )

        with col2:

            st.metric(
            "Pore Connectivity Index",
            f"{pore_connectivity:.2f}"
        )

            st.metric(
            "Reservoir Flow Capacity",
            f"{reservoir_flow_capacity:.2f}"
        )

        st.divider()

    

        st.subheader("🚩 Drilling Recommendation")

        if probability >= 0.80:

            st.success(
            """
### 🟢 HIGH PRIORITY

Recommended for exploration.

Reasons

✔ High probability of oil occurrence

✔ Favorable geological characteristics

✔ Strong hydrocarbon prospect
"""
        )

        elif probability >= 0.60:

            st.warning(
            """
### 🟡 MEDIUM PRIORITY

Further geological investigation recommended.

Additional seismic interpretation and
well log analysis may improve confidence.
"""
        )

        else:

            st.error(
            """
### 🔴 LOW PRIORITY

Current geological evidence suggests
low hydrocarbon potential.

Further exploration is not recommended.
"""
        )

        st.divider()

    

        with st.expander("📋 View Input Summary"):

            summary = pd.DataFrame({

            "Feature":[

                "Rock Type",

                "Trap Type",

                "Porosity",

                "Permeability",

                "Seismic Score",

                "Distance to Oil Field",

                "Reservoir Depth"

            ],

            "Value":[

                rock_type,

                trap_type,

                porosity,

                permeability,

                seismic_score,

                distance,

                depth

            ]

        })

            st.dataframe(
            summary,
            use_container_width=True
        )

    #
        with st.expander("⚙ Engineered Features"):

                engineered = pd.DataFrame({

            "Feature":[

                "Reservoir Quality",

                "Pore Connectivity Index",

                "Reservoir Flow Capacity",

                "Hydrocarbon Prospect Score"

            ],

            "Value":[

                reservoir_quality,

                round(pore_connectivity,2),

                round(reservoir_flow_capacity,2),

                round(hydrocarbon_prospect_score,3)

            ]

        })

                st.dataframe(
            engineered,
            use_container_width=True
        )
    else:
        st.info("Enter the geological parameters.")






    


    






