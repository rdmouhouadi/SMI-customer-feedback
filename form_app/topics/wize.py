import streamlit as st

def render():
    answers = {}
    answers["How happy are you with the technology in general?"] = st.radio(
        "How happy are you with the technology in general?",
        ["Very happy", "happy", "Neutral", "Unhappy", "Dessapointed"], index=None
    )
    answers["What are the strong points of the technology?"] = st.text_area(
        "What are the strong points of the technology?"
    )
    answers["What do you think could be improved in the technology?"] = st.text_area(
        "What do you think could be improved in the technology?"
    )
    return answers
