import streamlit as st

def render():
    answers = {}
    answers["How happy are you with PeauseNG"] = st.radio(
        "How happy are you with PeauseNG?",
        ["Very happy", "Happy", "Not happy", "Desappointed"]
    )

    answers["How easy is it to use?] = st.radio(
        "How easy is it to use?,
        ["Very easy", "Easy", "Difficult", "Very difficult"]
    )

    answers["How easy it to manage the fleet and users base?"] = st.radio(
        "How easy is it to manage the fleet and users base?",
        ["Very easy", "Easy", "Difficult", "Very difficult"]
    )

    answers["Do you have issues with the devices/smart phones?"] = st.radio(
        "Do you have issues with the devices/smart phones?",
        ["Yes", "No"]
    )
    
    answers["What do you think could be improved in PeauseNG and smart phones?"] = st.text_area(
        "What do you think could be improved in PeauseNG and smart phones?",
    )
    return answers
