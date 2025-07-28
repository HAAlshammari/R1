import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Define scope for Sheets API
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Load credentials from Streamlit Secrets
service_account_info = {
    "type": st.secrets["gcp_service_account"]["type"],
    "project_id": st.secrets["gcp_service_account"]["project_id"],
    "private_key_id": st.secrets["gcp_service_account"]["private_key_id"],
    "private_key": st.secrets["gcp_service_account"]["private_key"],
    "client_email": st.secrets["gcp_service_account"]["client_email"],
    "client_id": st.secrets["gcp_service_account"]["client_id"],
    "auth_uri": st.secrets["gcp_service_account"]["auth_uri"],
    "token_uri": st.secrets["gcp_service_account"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["gcp_service_account"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["gcp_service_account"]["client_x509_cert_url"],
}

credentials = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
client = gspread.authorize(credentials)

# You can change "RentalData" to your actual Google Sheet name
sheet = client.open("RentalData").sheet1

def submit_to_sheet(date, flats_a, flats_b, flats_c, total_cost, total_income, investor1, investor2, investor3):
    data = [str(date), flats_a, flats_b, flats_c, total_cost, total_income, investor1, investor2, investor3]
    sheet.append_row(data)
