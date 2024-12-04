import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import joblib
import pandas as pd

# Load the SVM model
model = joblib.load('svm_model.joblib')

# Mapping dictionaries
ethnicity_map = {
    'White-European': 0, 
    'Black': 1, 
    'Asian': 2, 
    'Hispanic': 3, 
    'Other': 4
}
contry_of_res_map = {
    'United States': 0, 'Brazil': 1, 'Spain': 2, 'Egypt': 3, 'New Zealand': 4,
    'Bahamas': 5, 'Burundi': 6, 'Austria': 7, 'Argentina': 8, 'Jordan': 9,
    'Ireland': 10, 'United Arab Emirates': 11, 'Afghanistan': 12, 'Lebanon': 13,
    'United Kingdom': 14, 'South Africa': 15, 'Italy': 16, 'Pakistan': 17,
    'Bangladesh': 18, 'Chile': 19, 'France': 20, 'China': 21, 'Australia': 22,
    'Canada': 23, 'Saudi Arabia': 24, 'Netherlands': 25, 'Romania': 26,
    'Sweden': 27, 'Tonga': 28, 'Oman': 29, 'India': 30, 'Philippines': 31,
    'Sri Lanka': 32, 'Sierra Leone': 33, 'Ethiopia': 34, 'Viet Nam': 35,
    'Iran': 36, 'Costa Rica': 37, 'Germany': 38, 'Mexico': 39, 'Russia': 40,
    'Armenia': 41, 'Iceland': 42, 'Nicaragua': 43, 'Hong Kong': 44, 'Japan': 45,
    'Ukraine': 46, 'Kazakhstan': 47, 'American Samoa': 48, 'Uruguay': 49,
    'Serbia': 50, 'Portugal': 51, 'Malaysia': 52, 'Ecuador': 53, 'Niger': 54,
    'Belgium': 55, 'Bolivia': 56, 'Aruba': 57, 'Finland': 58, 'Turkey': 59,
    'Nepal': 60, 'Indonesia': 61, 'Angola': 62, 'Azerbaijan': 63, 'Iraq': 64,
    'Czech Republic': 65, 'Cyprus': 66
}
relation_map = {
    'Self': 0, 'Parent': 1, 'Sibling': 2, 'Friend': 3, 'Other': 4, 'Guardian': 5
}

age_desc_map = {
    '0-3 years': 0, '4-11 years': 1, '12-17 years': 2, '18+ years': 3
}

gender_map = {'f': 0, 'm': 1}  # Female = 0, Male = 1

# Streamlit page settings
st.set_page_config(page_title="Autism Screening App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Predict Autism"])

# Home page
# Home page
if page == "Home":
    st.title("Welcome to AutiScreen")
    st.markdown("""
        Autism, or Autism Spectrum Disorder (ASD), is a developmental disorder characterized by challenges 
        with social interaction, communication, and repetitive behaviors. It affects individuals differently, 
        hence the term 'spectrum.'

        ### Why is Autism Screening Important?
        Early screening and diagnosis can help families access interventions and support systems tailored to 
        the individual's needs. Detecting autism early enables strategies that significantly improve quality 
        of life, education, and social integration.

        ### How Our App Helps
        This application provides a simple and accessible way to analyze tendencies towards autism using 
        responses to a series of questions and demographic data. Powered by an advanced **SVM Machine Learning 
        model**, it predicts the likelihood of autism traits, helping individuals seek further professional 
        evaluation if needed.
    """)

    st.markdown("### Explore the Carousel Below to Learn More:")

    # Carousel with st.image()
    carousel_images = [
        {"url": "https://plus.unsplash.com/premium_photo-1663089388518-cd602f17efb5?q=80&w=2070&auto=format&fit=crop", "caption": "Understanding Autism"},
        {"url": "https://dreambigchildren.com/wp-content/uploads/2021/08/Strategies-for-autism-1536x1024.jpeg", "caption": "Strategies for Autism Support"},
    ]

    for item in carousel_images:
        st.image(item["url"], use_column_width=True, caption=item["caption"])

    st.markdown("""
        ### Our Mission
        By using this tool, we aim to empower individuals, families, and caregivers with a quick, accessible, 
        and scientifically-backed initial screening process for autism.
    """)

# Predict Autism page
elif page == "Predict Autism":
    st.title("Autism Screening Prediction")

    # User input fields for features
    A1_Score = st.number_input('A1 Score', min_value=0, max_value=1, value=0)
    A2_Score = st.number_input('A2 Score', min_value=0, max_value=1, value=0)
    A3_Score = st.number_input('A3 Score', min_value=0, max_value=1, value=0)
    A4_Score = st.number_input('A4 Score', min_value=0, max_value=1, value=0)
    A5_Score = st.number_input('A5 Score', min_value=0, max_value=1, value=0)
    A6_Score = st.number_input('A6 Score', min_value=0, max_value=1, value=0)
    A7_Score = st.number_input('A7 Score', min_value=0, max_value=1, value=0)
    A8_Score = st.number_input('A8 Score', min_value=0, max_value=1, value=0)
    A9_Score = st.number_input('A9 Score', min_value=0, max_value=1, value=0)
    A10_Score = st.number_input('A10 Score', min_value=0, max_value=1, value=0)
    age = st.number_input('Age', min_value=0, value=0)
    gender = st.selectbox('Gender', options=['f', 'm'])
    ethnicity = st.selectbox('Ethnicity', options=list(ethnicity_map.keys()))
    jundice = st.selectbox('Jundice', options=['no', 'yes'])
    contry_of_res = st.selectbox('Country of Residence', options=list(contry_of_res_map.keys()))
    used_app_before = st.selectbox('Used App Before', options=['no', 'yes'])
    relation = st.selectbox('Relation', options=list(relation_map.keys()))
    age_desc = st.selectbox('Age Description', options=list(age_desc_map.keys()))

    # Calculate the `result` score as the sum of A1–A10 scores
    result = sum([A1_Score, A2_Score, A3_Score, A4_Score, A5_Score, A6_Score, A7_Score, A8_Score, A9_Score, A10_Score])

    # Prepare input data for the model
    input_data = pd.DataFrame({
        'A1_Score': [A1_Score], 'A2_Score': [A2_Score], 'A3_Score': [A3_Score], 
        'A4_Score': [A4_Score], 'A5_Score': [A5_Score], 'A6_Score': [A6_Score], 
        'A7_Score': [A7_Score], 'A8_Score': [A8_Score], 'A9_Score': [A9_Score], 
        'A10_Score': [A10_Score], 'age': [age], 'gender': [gender_map[gender]], 
        'ethnicity': [ethnicity_map[ethnicity]], 'jundice': [1 if jundice == 'yes' else 0], 
        'contry_of_res': [contry_of_res_map[contry_of_res]], 
        'used_app_before': [1 if used_app_before == 'yes' else 0], 
        'relation': [relation_map[relation]], 'age_desc': [age_desc_map[age_desc]], 
        'result': [result]
    })

    # Prediction button
    if st.button('Predict'):
        prediction = model.predict(input_data)
        st.write('Prediction: **Autism Likely**' if prediction[0] == 1 else '**Autism Unlikely**')