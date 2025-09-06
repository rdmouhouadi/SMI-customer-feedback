import streamlit as st

def render():
    answers = {}
    answers["How happy are you with the SUEZ Smart Metering contract?"] = st.radio(
        "How happy are you with the SUEZ Smart Metering contract?",
        ["Very happy", "happy", "Not happy", "Desappointed"], index=None
    )

    answers["How would you rate the overall smart metering solution?"] = st.radio(
        "How would you rate the overall smart metering solution?",
        ["Very happy", "happy", "Not happy", "Desappointed"], index=None
    )
    
    answers["What aspects of the solution do you value the most?"] = st.text_area(
        "What aspects of the solution do you value the most?"
    )

    answers["How strongly would you recommend SUEZ as a Smart Metering Partner?"] = st.radio(
        "How strongly would you recommend SUEZ as a Smart Metering Partner?",
        ["Strongly", "Neutral", "Poorly", "Not recommend"], index=None
    )
    
    answers["Any suggestions for improvement in general?"] = st.text_area(
        "Any suggestions for improvement in general?"
    )
    return answers
