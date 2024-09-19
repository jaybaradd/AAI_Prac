import streamlit as st
import csv
import pandas as pd
import os

# CSV file to store user data
CSV_FILE = 'user_data.csv'

# Check if the CSV file exists, if not, create it with the appropriate columns
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=['Username', 'Password', 'Mobile', 'City'])
    df.to_csv(CSV_FILE, index=False)

# Function to save user details to the CSV file
def save_user_csv(username, password, mobile, city, filename='user_data.csv'):
    new_data = [username,password,mobile,city]
    with open(filename, mode='a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_data)

# Sidebar for Login and Signup
st.sidebar.title("User Authentication")
auth_option = st.sidebar.button('Login')
auth_option2 = st.sidebar.button('Signup')
if auth_option2:
    st.title("Signup Form")

    # Signup fields
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    mobile = st.text_input("Mobile Number")
    city = st.text_input("City")
    
    if st.button("Submit"):
        if username and password and mobile and city:
            # Save user data to CSV
            
            save_user_csv(username, password, mobile, city, filename='user_data.csv')
            st.success(f"User {username} registered successfully!")
        else:
            st.error("Please fill in all fields!")

elif auth_option:
    st.title("Login Form")

    # Login fields
    login_username = st.text_input("Username", key='login_username')
    login_password = st.text_input("Password", type='password', key='login_password')

    if st.button("Log in"):
        df = pd.read_csv(CSV_FILE)
        # Check if the username and password match any entry in the CSV
        if not df[(df['Username'] == login_username) & (df['Password'] == login_password)].empty:
            st.success(f"Welcome {login_username}!")
        else:
            st.error("Invalid username or password!")





