import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="TE B group 3 project",
                   layout="wide",
                   page_icon="🩺")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Innovative Strategies for Multiple Disease Prognosis',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.caption("MCT RGIT Computer Engineering Department's")
    st.title('Multiple Disease Prognosis using Machine Learning')
    st.header("✅ verified by top medical consultants")
    st.text('Guide: Dr. Sharmila Rathod')
    st.text('Aryan Panchal B609')
    st.text('Jash Panchal B610')
    st.text('Ashlesha Padvi B606')
    





    # getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')   
    if len(Pregnancies) >  1:
     st.write("Please enter a valid number of pregnancies")
    else:
     st.write("")
    
with col2:
    Glucose = st.text_input('Glucose Level (mg/dl)')
    if len(Glucose) >  4:
     st.error("Please enter a valid Glucose level")
    else:
     st.write("")
    # code for Prediction    
with col3:
    BloodPressure = st.text_input('Blood Pressure value (mm Hg)')
    if len(BloodPressure) >  4:
     st.error("Please enter a valid bood pressure level")
    else:
     st.write("")
with col1:
    SkinThickness = st.text_input('Skin Thickness value')
    if len(SkinThickness) >  2:
     st.error("Please enter a valid skin thickness value")
    else:
     st.write("")
with col2:
    Insulin = st.text_input('Insulin Level (mu U/ml)')
    if len(Insulin) >  2:
     st.error("Please enter a valid Insulin level")
    else:
     st.write("")
with col3:
    BMI = st.text_input('BMI value (kg/m^2)')
    if len(BMI) >  3:
     st.error("Please enter a valid BMI")
    else:
     st.write("")
with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
with col2:
    Age = st.text_input('Age of the Person (years)')
    if len(Age) >  3:
     st.error("Please enter a valid age")
    else:
     st.write("")

    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic (ML Model Accuracy: 78.33%)'
            st.subheader('_⚕️Suggestions and inputs from our associated doctors:_')
            st.caption("personalised prognosis (refer your blood reports)")
            st.markdown("➡ If fasting blood sugar is numerically between 100-126 then patient is :blue[100% PRE-DIABETIC]")
            st.markdown("➡ If fasting blood sugar is numerically >126 then patient is :red[100% DIABETIC]")
            st.markdown("➡ If fasting blood sugar is numerically between 70-100 then patient is :green[100% NON-DIABETIC]")
            st.text("")
            st.markdown("➡ If post lunch blood sugar is numerically 140-200 then patient is :blue[100% PRE-DIABETIC]")
            st.markdown("➡ If post lunch blood sugar is numerically >200 then patient is :red[100% DIABETIC]")
            st.markdown("➡ If post lunch blood sugar is numerically <140 then patient is :green[100% NON-DIABETIC]") 


        else:
            diab_diagnosis = 'The person is not diabetic (ML Model Accuracy: 78.33%)'
            st.subheader('_⚕️Suggestions and inputs from our associated doctors:_')
            st.caption("personalised prognosis (refer your blood reports)")
            st.markdown("➡ If fasting blood sugar is numerically between 100-126 then patient is :blue[100% PRE-DIABETIC]")
            st.markdown("➡ If fasting blood sugar is numerically >126 then patient is :red[100% DIABETIC]")
            st.markdown("➡ If fasting blood sugar is numerically between 70-100 then patient is :green[0% NON-DIABETIC]")
            st.text("")
            st.markdown("➡ If post lunch blood sugar is numerically 140-200 then patient is :blue[100% PRE-DIABETIC]")
            st.markdown("➡ If post lunch blood sugar is numerically >200 then patient is :red[100% DIABETIC]")
            st.markdown("➡ If post lunch blood sugar is numerically <140 then patient is :green[100% NON-DIABETIC]") 

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.caption("MCT RGIT Computer Engineering Department's")
    st.title('Multiple Disease Prognosis using Machine Learning')
    st.header("✅ verified by top medical consultants")
    st.text('Guide: Dr. Sharmila Rathod')
    st.text('Aryan Panchal B609')
    st.text('Jash Panchal B610')
    st.text('Ashlesha Padvi B606')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease (ML Model accuracy: 85.12%).'

        else:
            heart_diagnosis = 'The person does not have any heart disease (ML Model accuracy: 85.12%).'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.caption("MCT RGIT Computer Engineering Department's")
    st.title('Multiple Disease Prognosis using Machine Learning')
    st.header("✅ verified by top medical consultants")
    st.text('Guide: Dr. Sharmila Rathod')
    st.text('Aryan Panchal B609')
    st.text('Jash Panchal B610')
    st.text('Ashlesha Padvi B606')
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease (ML Model accuracy: 87.17%)."
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease (ML Model accuracy: 87.17%)."

    st.success(parkinsons_diagnosis)
    
