import streamlit as st

def render():
    answers = {}
    answers["How happy are you with ONconnect?"] = st.radio(
        "How happy are you with ONconnect?",
        ["Very happy", "happy", "Not happy", "Desappointed"], index=None
    )
    answers["How often do you use the Map Screen?"] = st.radio(
        "How often do you use the Map Screen?",
        ["Every day", "Usually", "Reraly", "Never"], index=None
    )
    answers["How easy do you find it to manage the assets?"] = st.radio(
        "How easy do you find it to manage the assests (including manufacturer files, assets files)?",
        ["Very easy", "Easy", "Difficult", "Very difficult"], index=None
    )
    answers["How easy to find it to supervise and monitor the radio performane?"] = st.radio(
        "How easy do you find it to supervise and monitor the radio performance (maps, diagnostics, etc.)?",
        ["Very easy", "Easy", "Difficult", "Very difficult"], index=None
    )
    answers["How easy do you find it to visualize and understand alarms?"] = st.radio(
        "How easy do you find it to visualize and understand alarms?",
        ["Very easy", "Easy", "Difficult", "Very difficult"], index=None
    )
    answers["How easy do you find it to visualize consumption in graphs, including exports?"] = st.radio(
        "How easy do you find it to visualize consumption in graphs, including exports?",
        ["Very easy", "Easy", "Difficult", "Very difficult"], index=None
    )
    answers["Any issues or feedback on the the screens?"] = st.text_area(
        "Any issues or feedback on the screens (in general or on some screens in particular)?"
    )
    answers["Any issues or feedback on the exports?"] = st.text_area(
        "Any issues or feedback on the exports (MDD, BPS, API)?"
    )
    answers["How happy are you with the system availability time?"] = st.radio(
        "How happy are you with the system availability time?",
        ["Very happy", "Happy", "Not happy", "Desappointed"], index=None
    )
    answers["How happy are you with the system performance?"] = st.radio(
        "How happy are you with the system performance?",
        ["Very happy", "Happy", "Not happy", "Desappointed"], index=None
    )
    answers["How happy are you with the application release management?"] = st.radio(
        "How happy are you with the application release management (planning and execution)?",
        ["Very happy", "Happy", "Not happy", "Desappointed"], index=None
    )
    answers["What do you think that could be improved in the MDM?"] = st.text_area(
        "What do you think that could be improved in the MDM?"
    )
    return answers
