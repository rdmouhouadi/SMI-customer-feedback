import streamlit as st

def render():
    answers = {}
    answers["How happy are you with the NFC dongle?"] = st.radio(
        "How happy are you with the NFC dongle?",
        ["Very happy", "happy", "Not happy", "Desappointed"], index=None
    )

    answers["Is it easy to use?"] = st.radio(
        "Is it easy to use?",
        ["Yes", "No"], index=None
    )
    
    answers["How happy are you with the battery and its autonomy?"] = st.text_area(
        "How happy are you with the battery and its autonomy?"
    )

    answers["Is the battery easy to recharge?"] = st.radio(
        "Is the battery easy to recharge?",
        ["Yes", "No"], index=None
    )

    answers["Do you have any issue with the NFC dongles?"] = st.text_area(
        "Do you have any issue with the NFC dongles?"
    )
    
    answers["What do you think could be improved in the NFC dongles?"] = st.text_area(
        "What do you think could be improved in the NFC dongles?"
    )
    return answers
