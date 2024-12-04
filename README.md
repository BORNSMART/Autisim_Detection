 AutiScreen: Autism Screening Application
AutiScreen is a user-friendly web application designed to assist in the early screening of Autism Spectrum Disorder (ASD). Powered by a Support Vector Machine (SVM) model, it uses a combination of questionnaire responses and demographic data to predict the likelihood of autism traits. The app serves as an initial screening tool, empowering individuals, caregivers, and healthcare professionals to seek professional evaluation and support when needed.

Features
User-Friendly Interface: Simple and accessible interface built using Streamlit.
Accurate Predictions: Leverages an advanced SVM model for autism screening.
Demographic and Behavioral Inputs: Includes factors like age, gender, ethnicity, and key behavioral scores (A1–A10).
Insights on Autism: Provides informative content about autism and its significance.
How It Works
Input Data: Users provide information, including A1–A10 behavioral scores, age, gender, ethnicity, country of residence, and other factors.
Prediction: The SVM model processes the inputs and predicts whether the user is likely to exhibit autism traits.
Results: The app displays whether autism is likely or unlikely based on the inputs.
Setup and Installation
Follow these steps to set up and run the application locally:

Prerequisites
Python 3.8 or above
Libraries: Streamlit, scikit-learn, pandas, joblib, and PIL
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/AutiScreen.git  
cd AutiScreen  
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt  
Run the app:
bash
Copy code
streamlit run app.py  
Model Details
The application is powered by a Support Vector Machine (SVM) classifier. The model was trained using a dataset of autism screening data, which includes behavioral scores, demographic information, and screening results. Key features used for training include:

Behavioral scores (A1–A10)
Age and age description
Gender
Ethnicity
Country of residence
Relation to the person being screened
