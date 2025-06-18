import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("salary_model.pkl", "rb"))

# Set page config
st.set_page_config(page_title="Salary Estimator", page_icon="💰")
st.title("💰 Salary Estimator")
st.markdown("Enter your details below to estimate your expected salary based on experience.")

# Dropdown options
job_titles = ['Data Analyst', 'ML Engineer', 'Data Scientist', 'Business Analyst', 'Software Developer']
locations = ['Mumbai', 'Bangalore', 'Hyderabad', 'Pune', 'Chennai', 'Delhi', 'Kolkata', 'Remote']
companies = ['TCS', 'Infosys', 'Accenture', 'Wipro', 'IBM', 'Capgemini', 'Deloitte', 'ZS Associates', 'EY', 'Cognizant']

# Form
with st.form("user_input_form"):
    st.subheader("📝 Your Profile")
    name = st.text_input("Your Name")
    role = st.selectbox("Job Role", job_titles)
    company = st.selectbox("Preferred Company", companies)
    location = st.selectbox("Preferred Location", locations)
    experience = st.slider("Years of Experience", 0, 20, 2)
    submitted = st.form_submit_button("💡 Estimate Salary")

if submitted:
    predicted_salary = model.predict([[experience]])[0]

    st.success(f"Hi {name}, your estimated salary is:")
    st.markdown(f"### 💰 ₹{predicted_salary:.2f} LPA")

    # Display user inputs
    st.subheader("📋 Your Provided Details")
    st.markdown(f"- 👤 **Name**: {name}")
    st.markdown(f"- 💼 **Role**: {role}")
    st.markdown(f"- 🏢 **Company**: {company}")
    st.markdown(f"- 📍 **Location**: {location}")
    st.markdown(f"- 📈 **Experience**: {experience} years")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Salary prediction based on simple linear regression model")
