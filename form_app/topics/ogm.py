import streamlit as st

def render():
    answers = {}
    answers["How happy are you with OGM?"] = st.radio(
        "How happy are you with OGM?",
        ["Very happy", "happy", "Not happy", "Desappointed"]
    )
    answers["Do you find it easy to create/manage new sites, concentrators and components?"] = st.text_area(
        "Do you find it easy to create/manage new sites, concentrators and components?"
    )
    answers["Do you find it easy to monitor the gateway fleet?"] = st.text_area(
        "Do you find it easy to monitor the gateway fleet (diagnostics, traffic trends, alarms, etc.?"
    )
    answers["Do you find it easy to visualize and understand alarms?"] = st.radio(
        "Do you find it easy to visualize and understand alarms?",
        ["Yes", "No"]
    )
    answers["Any issues or feedback on the different screens and data presented?"] = st.text_area(
        "Any issues or feedback on the differenr screens and data presented?"
    )
    answers["How happy are you with the system availability time?"] = st.radio(
        "How happy are you with the system availability time?",
        ["Very happy", "happy", "Not happy", "Desappointed"]
    )
    answers["How happy are you with the system performance?"] = st.radio(
        "How happy are you with the system performance?",
        ["Ver happy", "happy", "Not happy", "Desappointed"]
    )
    answers["How happy are you with the application release management?"] = st.radio(
        "How happy are you with the application release management (planning and execution)?",
        ["Very happy", "happy", "Not happy", "Desappointed"]
    )
    answers["What do you think that could be improved in OGM?"] = st.text_area(
        "What do you think that could be improved in OGM?
    )
    return answers
