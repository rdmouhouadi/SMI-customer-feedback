import streamlit as st

def render():
    answers = {}
    answers["How happy are with the K2G?"] = st.radio(
        "How happy are you with teh K2G?",
        ["Very happy", "happy", "Not happy", "Desappointed"]
    )
    answers["Any recurrent issue with the deliveries (delays, shipping, etc.)"] = st.text_area(
        "Any recurrent issue with the deliveries (delays, shipping, etc.)?"
    )
    answers["How easy are they to install and commission (validation, optimization and tuning)?"] = st.radio(
        "How easy are they to install and commission (validation, optimization and tuning)?",
        ["Very easy", "Easy", "Difficult", "Very difficult"]
    )
    answers["Any issues with the filters or accessories (such as external antenas, ...)?"] = st.text_area(
        "Any issues with the filters or accessories (such as external antenas, ...)?"
    )
    answers["Are they easy to maintain in the field?"] = st.text_area(
        "Are they easy to maintain in the field (make diagnosis, replace parts, correct config, update versions, change SIM card, add external GSM or GPS, antenas, etc.)?"
    )
    answers["Are you happy with local tools working with K2Gs?"] = st.text_area(
        "Are you happy with local tools working with K2Gs (auto-test, noise analysis, etc.)?"
    )
    answers["Any issues with the concentrators?"] = st.text_area(
        "Any issues with the concentrators?"
    )
    answers["Any issues with the SIM cards from Suez Digital Solutions or related to the telecom operators?"] = st.text_area(
        "Any issues with the SIM cards from Suez Digital Solutions or related to the telecom operators?"
    )
    answers["How happy are you with the K2G fleet performance?"] = st.radio(
        "How happy are you with the K2G fleet performance?",
        ["Very happy", "Happy", "Not happy", "Desappointed"]
    )
    answers["What do you think could be improved in the concentrators?"] = st.text_area(
        "What do you think could be improved in the concentrators?"
    )
    return answers
