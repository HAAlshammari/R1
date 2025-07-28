import streamlit as st
import json
from google.oauth2 import service_account

# Load credentials from Streamlit secrets
creds_dict = st.secrets["gcp_service_account"]
credentials = service_account.Credentials.from_service_account_info(dict(creds_dict))

    # 👇 Replace with your actual sheet name
    sheet = client.open("RentalData").Sheet1

    sheet.append_row([
        date,
        flats_a,
        flats_b,
        flats_c,
        total_cost,
        total_income,
        inv1,
        inv2,
        inv3
    ])
