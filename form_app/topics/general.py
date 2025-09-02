import streamlit as st

def render():
    answers = {}
    answers["How would you rate the overall smart metering solution?"] = st.radio(
        "How would you rate the overall smart metering solution?",
        ["Excellent", "Good", "Average", "Poor"]
    )
    answers["What aspects of the solution do you value the most?"] = st.text_area(
        "What aspects of the solution do you value the most?"
    )
    answers["Any suggestions for improvement in general?"] = st.text_area(
        "Any suggestions for improvement in general?"
    )
    return answers
