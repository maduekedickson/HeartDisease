import streamlit as st
import pandas as pd
import pickle

st.image("image.jpg")


# Load the saved model
with open("random_forest_model_1.pkl", "rb") as f:
    loaded_pickle_model = pickle.load(f)

# Define the function to make predictions
def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    })
    prediction = loaded_pickle_model.predict(input_data)
    return prediction[0]

# Create the Streamlit app
def main():
    st.title("Heart Disease Prediction")
    
    # Add input fields for various features
    age = st.slider("Age", min_value=0, max_value=100, value=50)
    sex = st.radio("Sex", options=["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", options=[0, 1, 2, 3])
    trestbps = st.slider("Resting Blood Pressure (mm Hg)", min_value=90, max_value=200, value=120)
    chol = st.slider("Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", options=["False", "True"])
    restecg = st.selectbox("Resting Electrocardiographic Results", options=[0, 1, 2])
    thalach = st.slider("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
    exang = st.radio("Exercise Induced Angina", options=["No", "Yes"])
    oldpeak = st.slider("ST Depression Induced by Exercise", min_value=0.0, max_value=6.2, value=2.0)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", options=[0, 1, 2])
    ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", options=[0, 1, 2, 3])
    thal = st.selectbox("Thal", options=[0, 1, 2, 3])
    
    # Convert categorical inputs to numerical
    sex = 1 if sex == "Male" else 0
    fbs = 1 if fbs == "True" else 0
    exang = 1 if exang == "Yes" else 0
    
    # When the predict button is pressed
    if st.button("Predict"):
        prediction = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
        if prediction == 1:
            st.write("The patient is predicted to have heart disease.")
        else:
            st.write("The patient is predicted to not have heart disease.")

if __name__ == "__main__":
    main()
