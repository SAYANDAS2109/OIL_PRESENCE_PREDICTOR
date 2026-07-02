🛢 Oil Presence Prediction using Machine Learning

A complete end-to-end Machine Learning project that predicts the probability of oil occurrence using geological, seismic, and petroleum engineering parameters.

The project combines Petroleum Engineering concepts, Feature Engineering, Machine Learning, Deep Learning, Model Explainability, and Streamlit Deployment to simulate an intelligent reservoir screening system.

Note

This project has been developed for educational and portfolio purposes.
The model has been trained using a synthetic geological dataset, therefore predictions and engineering indicators should not be interpreted as real exploration recommendations.

🚀 Project Highlights
End-to-End Machine Learning Pipeline
Geological Data Preprocessing
Petroleum Engineering Feature Engineering
Hyperparameter Tuning
Deep Learning Model Comparison
SHAP Explainability
Interactive Streamlit Dashboard
Reservoir Engineering Summary
Drilling Recommendation System
Responsive User Interface
📊 Dataset

The model was trained on a synthetic geological dataset containing reservoir properties such as:

Rock Type
Trap Type
Porosity
Permeability
Seismic Score
Reservoir Depth
Distance to Existing Oil Field

The synthetic dataset was designed to simulate realistic petroleum exploration scenarios for machine learning experimentation.

⚙ Petroleum Engineering Feature Engineering

Several engineered features were created to improve model performance.

Reservoir Quality

Rule-based classification using Porosity and Permeability.

Categories:

Excellent
Good
Average
Poor
Pore Connectivity Index

Measures the combined influence of storage capacity and fluid flow.

Formula

Pore Connectivity Index = Porosity × Permeability
Reservoir Flow Capacity

Represents simplified reservoir productivity.

Formula

Reservoir Flow Capacity =
(Permeability × Porosity)
/ Reservoir Depth
Hydrocarbon Prospect Score

Composite exploration score.

Formula

Hydrocarbon Prospect Score

=
0.35 × Normalized Porosity
+
0.35 × Normalized Permeability
+
0.30 × Seismic Score

These engineered features are engineering-inspired metrics created specifically for machine learning feature engineering.

They are not standard petroleum engineering equations and are intended only for educational demonstration.

🤖 Machine Learning Models Evaluated

The following models were trained and compared:

Logistic Regression
Decision Tree
Random Forest
Tuned XGBoost
Deep Neural Network (TensorFlow/Keras)

After extensive evaluation and hyperparameter tuning, the Tuned XGBoost Classifier was selected for deployment because it achieved the best overall performance.

📈 Final Model Performance (Tuned XGBoost)
Metric	Score
Accuracy	91.10%
Precision	92.76%
Recall	73.74%
F1 Score	82.16%
ROC-AUC	87.81%
🧠 Deep Learning Experiment

A fully connected Deep Neural Network (ANN) was also developed using TensorFlow/Keras.

The network included:

Dense Layers
Batch Normalization
Dropout Regularization
Early Stopping
Adam Optimizer

Although the ANN produced competitive results, the Tuned XGBoost model achieved superior overall performance and was therefore selected for deployment.

🔍 Model Explainability

SHAP (SHapley Additive exPlanations) was used to interpret model predictions.

Visualizations include:

SHAP Summary Plot
SHAP Feature Importance Plot

These explain how each geological feature contributes to the final prediction.

🌐 Streamlit Application

The deployed application provides:

Geological parameter input
Prediction probability
Reservoir Engineering Summary
Drilling Recommendation
Prediction Confidence
Input Summary
Engineered Feature Summary
Feature Information Sidebar
🛠 Tech Stack
Programming
Python
Libraries
Pandas
NumPy
Scikit-learn
XGBoost
TensorFlow / Keras
SHAP
Matplotlib
Deployment
Streamlit
📂 Project Structure
Oil-Presence-Prediction/

│── app.py
│── oil_prob_xgb.json
│── scaler.pkl
│── feature_columns.pkl
│── requirements.txt
│── README.md
│── Oil_Presence_Prediction.ipynb

├── screenshots/
│
├── models/
│
└── dataset/
🚀 Installation

Clone the repository

git clone https://github.com/yourusername/Oil-Presence-Prediction.git

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app.py
📌 Future Improvements
Integration with real geological datasets
Well Log Analysis
Reservoir Simulation Integration
GIS-Based Visualization
Cloud Deployment
Multi-Class Reservoir Classification
Time-Series Production Forecasting
⚠ Disclaimer

This application is intended solely for educational purposes.

The model has been trained using a synthetic dataset and should not be used for real-world petroleum exploration or drilling decisions.

Actual hydrocarbon exploration requires extensive geological, geophysical, geochemical, and reservoir engineering analysis beyond the scope of this project.

👨‍💻 Author

Elite Devill

Petroleum Engineering Student | Machine Learning Enthusiast | AI & Data Science
