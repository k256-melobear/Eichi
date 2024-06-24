import streamlit as st
import pandas as pd
import requests

st.title("📊 aira(仮)")



userid = st.text_input("your uuid:")
response = requests.get('https://api.aira.love/user/ranking?uidCode=' + userid)
if response.status_code == 200:
    st.write(response.json())