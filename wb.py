import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks', layout='wide', page_icon="🧑‍⚕️")

# Add custom CSS for styling
st.markdown("""
   <style>
        .main {background-color: #F0F8FF; color: #2F4F4F;}  /* Light Mode Color Scheme */
        .css-1v3fvcr {background-color: #1E90FF;}  /* Primary Button Color */
        .css-1l7y0w8 {background-color: #E0FFFF;}  /* Sidebar Background Color */
        .stButton button {background-color: #1E90FF; color: white;}  /* Button text color */
        .stTextInput input {border-color: #1E90FF;}  /* Text input border color */
        .stTextInput input:focus {border-color: #1E90FF;}  /* Text input focus color */
        /* Button Styling */
        .stButton button {
            background-color: #4C6E91;  /* Blue button */
            color: white;
            border-radius: 30px;
            padding: 15px 35px;
            font-size: 18px;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .stButton button:hover {
            background-color: #35598F;  /* Darker blue hover */
            transform: scale(1.05);
        }

        .stButton button:active {
            transform: scale(1.02);
        }

        /* Floating Action Button (FAB) */
        .fab {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background-color: #4C6E91;
            color: white;
            font-size: 30px;
            padding: 20px;
            border-radius: 50%;
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .fab:hover {
            background-color: #35598F;
            transform: scale(1.1);
        }

        /* Dark Mode Styling */
        body.dark-mode {
            background: #2D3B4F;
            color: #E1E4E8;
        }
    </style>
""", unsafe_allow_html=True)

# Load pre-trained models
diabetes_model = pickle.load(open(r"C:\Users\Gautam Kumar\OneDrive\Documents\Prediction of Disease Outbreaks\training_models\diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"C:\Users\Gautam Kumar\OneDrive\Documents\Prediction of Disease Outbreaks\training1_models\heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\Gautam Kumar\OneDrive\Documents\Prediction of Disease Outbreaks\training 2_models\parkinsons_model.sav", 'rb'))
# Initialize session state for sidebar visibility
if 'sidebar_visible' not in st.session_state:
    st.session_state.sidebar_visible = True  # Default: Show sidebar

# Toggle the sidebar visibility based on button click
def toggle_sidebar():
    st.session_state.sidebar_visible = not st.session_state.sidebar_visible

# Sidebar toggle button
st.sidebar.button("Toggle Sidebar", on_click=toggle_sidebar)

  # Show or hide the sidebar menu based on the session state
if st.session_state.sidebar_visible:
    with st.sidebar:
        selected = option_menu('Prediction of Disease Outbreaks',
                               ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                               menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)
else:
    selected = None  # If sidebar is hidden, set selected to None          

# Toggle for Dark Mode
dark_mode = st.checkbox("Enable Dark Mode", value=False)

if dark_mode:
    st.markdown('<style>body { background-color: #2D3B4F; color: #E1E4E8; }</style>', unsafe_allow_html=True)
    st.markdown('<div class="footer">Dark Mode Enabled</div>', unsafe_allow_html=True)

# Floating Action Button (FAB)
st.markdown('<div class="fab">+</div>', unsafe_allow_html=True)

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    st.markdown('<h4>Enter the details for Diabetes Prediction</h4>', unsafe_allow_html=True)
    st.markdown('Please enter the following details about the person below to predict the likelihood of diabetes.', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        Bloodpressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    st.markdown('<h4>Enter the details for Heart Disease Prediction</h4>', unsafe_allow_html=True)
    st.markdown('Please enter the following details about the person to predict the likelihood of heart disease.', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')
    with col2:
        Sex = st.text_input('Sex')
    with col3:
        Chest_Pain_types = st.text_input('Chest Pain types')
    with col1:
        Resting_Blood_Pressure = st.text_input('Resting Blood Pressure')
    with col2:
        Serum_Cholestoral_in_mg_dl = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        Fasting_Blood_Sugar_120_mg_dl = st.text_input('Fasting Blood Sugar >120 mg/dl')
    with col1:
        Resting_Electrocardiographic_results = st.text_input('Resting Electrocardiographic results')
    with col2:
        Maximum_Heart_Rate_achieved = st.text_input('Maximum Heart Rate achieved')
    with col3:
        Exercise_Induced_Angina = st.text_input('Exercise Induced Angina')
    with col1:
        ST_depression_induced_by_exercise = st.text_input('ST depression induced by exercise')
    with col2:
        Slop_of_the_peak_exercise_ST_segment = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        Major_vessels_colored_by_flourosopy = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thaldefect = st.text_input('thal: 0=normal; 1=fixed defect; 2=reversable defect')
   
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [Age, Sex, Chest_Pain_types, Resting_Blood_Pressure, Serum_Cholestoral_in_mg_dl, Fasting_Blood_Sugar_120_mg_dl, Resting_Electrocardiographic_results, Maximum_Heart_Rate_achieved, Exercise_Induced_Angina, ST_depression_induced_by_exercise, Slop_of_the_peak_exercise_ST_segment, Major_vessels_colored_by_flourosopy, thaldefect]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'
    st.success(heart_diagnosis)

# Parkinson's Disease Prediction
if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")
    st.markdown('<h4>Enter the details for Parkinson\'s Disease Prediction</h4>', unsafe_allow_html=True)
    st.markdown('Please enter the following details to predict the likelihood of Parkinson\'s disease.', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    # Collect user inputs for relevant Parkinson's features
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
        parkinson_prediction = parkinsons_model.predict([user_input])
        if parkinson_prediction[0] == 1:
            parkinson_diagnosis = "The person has Parkinson's disease"
        else:
            parkinson_diagnosis = "The person does not have Parkinson's disease"
    st.success(parkinson_diagnosis)
