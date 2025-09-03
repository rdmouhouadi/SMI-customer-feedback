import streamlit as st

def render():
    answers = {}
    answers["How happy are you with our support services in general?"] = st.radio(
        "How happy are you with our support services in general?",
       ["Very happy", "Happy", "Not happy", "Desappointed"]
    )
    answers["How happy are you with IT4US as a ticket management tool?"] = st.radio(
        "how happy are you with IT4US as a ticket management tool?",
        ["Very happy", "Happy", "Not happy", "Desappointed"]
    )
    answers["How happy are you with our Project Management?"] = st.radio(
        "How happy are you with our Project Management?",
        ["Very happy", "Happy", "Not happy", "Desappointed"]
    )
    answers["Any suggestions for improvement?"] = st.text_area(
        "Any suggestions for improvement in general?"
    )
    return answers
