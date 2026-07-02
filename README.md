# 🛢 Oil Presence Prediction

An end-to-end **Machine Learning** project that predicts the probability of oil occurrence using geological, seismic, and petroleum engineering parameters. This project combines **Machine Learning**, **Deep Learning**, **Petroleum Engineering concepts**, **Feature Engineering**, **Model Explainability**, and **Streamlit Deployment** to simulate an intelligent reservoir screening system.

> **⚠ Disclaimer**
>
>
> The model has been trained using a **synthetic geological dataset**, therefore the predictions, engineered features, and drilling recommendations should **not** be interpreted as real-world petroleum exploration decisions. Actual reservoir evaluation requires detailed geological, geophysical, geochemical, and reservoir engineering studies.

---

# Live Demo
-[link](https://oilpresencepredictor-nxgzpsnjjtqbqthcyfb6ij.streamlit.app/)
---
# LinkedIn Profile
-[link](https://www.linkedin.com/in/sayan-das-1466b1369/)
---

# 🚀 Features

- Predicts probability of oil occurrence
- Interactive Streamlit Web Application
- Petroleum Engineering inspired Feature Engineering
- Reservoir Quality Classification
- Hydrocarbon Prospect Score
- Reservoir Engineering Summary
- Prediction Confidence Visualization
- Drilling Recommendation System
- SHAP Explainability
- Responsive Two-Column User Interface
- Feature Information Sidebar
- Educational Reservoir Screening Tool

---

# 📊 Dataset

The project uses a **synthetic geological dataset** containing reservoir and seismic parameters including:

- Rock Type
- Trap Type
- Porosity
- Permeability
- Seismic Score
- Estimated Reservoir Depth
- Distance to Existing Oil Field

---

# ⚙ Petroleum Engineering Feature Engineering

Several engineering-inspired features were created to improve model performance.

## Reservoir Quality

A rule-based classification using Porosity and Permeability.

Classification:

- Excellent
- Good
- Average
- Poor

---

## Pore Connectivity Index

Measures the combined influence of porosity and permeability.

**Formula**

```text
Pore Connectivity Index = sqrt of(Porosity × Permeability)
```

**Significance**

Higher values indicate better interconnected pore spaces, improving hydrocarbon flow potential.

---

## Reservoir Flow Capacity

Represents simplified reservoir productivity.

**Formula**

```text
Reservoir Flow Capacity =
(Permeability × Porosity)
/ Reservoir Depth
```

**Significance**

Higher permeability and porosity improve reservoir productivity, while greater reservoir depth reduces flow capacity.

---

## Hydrocarbon Prospect Score

Composite exploration score combining reservoir quality and seismic information.

**Formula**

```text
Hydrocarbon Prospect Score

=
0.35 × Normalized Porosity
+
0.35 × Normalized Permeability
+
0.30 × Seismic Score
```

**Significance**

Provides a simplified estimate of hydrocarbon potential by combining reservoir properties with seismic interpretation.

> **Note**
>
> These engineered features are **engineering-inspired metrics** created specifically for machine learning feature engineering.
>
> They are **not standard petroleum engineering equations** and are intended only to improve predictive performance on the synthetic dataset.

---

# 🤖 Machine Learning Models Evaluated

The following models were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- Tuned XGBoost Classifier
- Deep Neural Network (TensorFlow / Keras)

After extensive evaluation and hyperparameter tuning, the **Tuned XGBoost Classifier** achieved the best overall performance and was selected for deployment.

---

# 📈 Final Model Performance (Tuned XGBoost)

| Metric | Score |
|---------|-------|
| Accuracy | **91.10%** |
| Precision | **92.76%** |
| Recall | **73.74%** |
| F1 Score | **82.16%** |
| ROC-AUC | **87.81%** |

---

# 🧠 Deep Learning Experiment

A fully connected **Artificial Neural Network (ANN)** was developed using **TensorFlow/Keras** to compare its performance with traditional machine learning models.

The architecture includes:

- Dense Layers
- ReLU Activation
- Batch Normalization
- Dropout Regularization
- Early Stopping
- Adam Optimizer

Although the ANN produced competitive performance, the **Tuned XGBoost Classifier** achieved superior overall metrics and was selected for deployment.

---

# 🔍 Model Explainability

To improve model interpretability, **SHAP (SHapley Additive exPlanations)** was used.

Generated visualizations include:

- SHAP Summary Plot
- SHAP Feature Importance Plot

These explain how individual geological features contribute to the final prediction.

---

# 🌐 Streamlit Application

The deployed web application provides:

- Geological Parameter Input
- Oil Presence Prediction
- Prediction Probability
- Reservoir Engineering Summary
- Drilling Recommendation
- Prediction Confidence Indicator
- Engineered Feature Summary
- Input Summary
- Feature Information Sidebar
- Synthetic Dataset Disclaimer

---

# 🛠 Technology Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- XGBoost

### Deep Learning

- TensorFlow
- Keras

### Data Processing

- Pandas
- NumPy

### Model Explainability

- SHAP

### Visualization

- Matplotlib

### Deployment

- Streamlit

---

# 📂 Repository Structure

```text
Oil-Presence-Prediction/
│
├── app.py
├── oil_prob_xgb.json
├── scaler.pkl
├── feature_columns.pkl
├── requirements.txt
├── README.md
├── PROJECT_4.ipynb

```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/SAYANDAS2109/OIL_PRESENCE_PREDICTOR
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit

```bash
streamlit run app.py
```

---

# 🎯 Project Workflow

1. Data Collection (Synthetic Geological Dataset)
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Petroleum Engineering Feature Engineering
5. Feature Scaling & Encoding
6. Machine Learning Model Training
7. Hyperparameter Tuning
8. Deep Learning Model Development
9. Model Evaluation & Comparison
10. SHAP Explainability
11. Streamlit Deployment

---

# 📌 Future Improvements

- Integration with Real Geological Datasets
- Well Log Analysis
- Reservoir Simulation Integration
- Production Forecasting
- Multi-Class Reservoir Classification

---

