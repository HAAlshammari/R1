import gspread
from google.oauth2 import service_account
import streamlit as st

def submit_to_sheet(date, flats_a, flats_b, flats_c, total_cost, total_income, investor1_income, investor2_income, investor3_income):
    creds_dict = st.secrets["gcp_service_account"]
    creds = service_account.Credentials.from_service_account_info(dict(creds_dict))
    client = gspread.authorize(creds)

    sheet = client.open("RentalData").sheet1  
    sheet.append_row([
    date,
    flats_a,
    flats_b,
    flats_c,
    total_cost,
    total_income,
    investor1_income,
    investor2_income,
    investor3_income
    ])
