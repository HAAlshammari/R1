import gspread
from google.oauth2 import service_account
import streamlit as st

def submit_to_sheet(date, flat_a, flat_b, flat_c, total_cost, total_income, investor_shares):
    creds_dict = st.secrets["gcp_service_account"]
    creds = service_account.Credentials.from_service_account_info(dict(creds_dict))
    client = gspread.authorize(creds)

    sheet = client.open("RentalData").sheet1  
    sheet.append_row([
        date,
        flat_a,
        flat_b,
        flat_c,
        total_cost,
        total_income,
        investor_shares[0],
        investor_shares[1],
        investor_shares[2]
    ])
