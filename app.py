from codecs import getencoder
import streamlit as st
import pickle


def main():
    background = """<div style='background-color:black; padding:13px'>
                    <h1 style='color:white'>Model Deployment Load Eligibility Prediction Apps</h1>
                </div>"""

    st.markdown(background, unsafe_allow_html=True)
    left, right =  st.columns ((2,2))
    gender = left.selectbox ('Gender', ('Male', 'Female'))
    married = right.selectbox ('Maried', ('Yes', 'No'))
    dependent = left.selectbox ('Dependents', ('None','One','Two', 'Theree'))
    education = right.selectbox ('Education', ('Graduate','Not Graduate'))
    self_employed = left.selectbox ('Self-Employed', ('Yes', 'No'))
    applicant_income = left.number_input('Applicant Income')
    Coapplicat_income = left.number_input('Coapplicat_income')
    loan_amount = right.number_input('Loan Amount')
    loan_amount_term = left.number_input('Loan Amount Term')
    creditHistory = right.number_input('Credit History', 0.0, 1.0)
    propertyArea =  left.selectbox('Property Area', ('Semiurban','Urban','Rural'))
    button = st.button('Predict')
    #Kalau button di klik
    if button:
        #buat prediksi
        result = predict(gender, married, dependent, education, self_employed, applicant_income, Coapplicat_income, loan_amount, loan_amount_term, creditHistory,propertyArea,button )
        st.success(f'You are {result} for loan')


with open('Random_Forest_model.pkl','rb') as file:
    RF_Model = pickle.load(file)

def predict  (gender, married, dependent, education, self_employed, applicant_income, Coapplicat_income, loan_amount, loan_amount_term, creditHistory,propertyArea,button ):
    #Proses hasil input
    gen = 0 if gender == 'Male' else 1
    mar = 0 if married == 'Yes' else 1
    dep = float (0 if dependent == 'None' else 1 if dependent == 'One' else 2 if dependent == 'Two' else 3)  
    edu = 0 if education == 'Graduate' else 1
    sem = 0 if self_employed == 'Yes' else 1
    pro = 0 if propertyArea == 'Semiurban' else 1
    lam = loan_amount / 1000
    cap =     Coapplicat_income / 1000


    #Membuat Prediksi
    prediction = RF_Model.predict([[gen, mar, dep, edu, sem, applicant_income, cap, lam, loan_amount_term, creditHistory, pro]])
    verdict = 'Not Eligible' if prediction == 0 else 'Eligible'
    return verdict

if __name__ == "__main__":
    main()
