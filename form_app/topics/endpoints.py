import streamlit as st

def render():
    answers = {}
    answers["How happy are you with end-points?"] = st.radio(
        "How happy are you with end-points?",
        ["Very happy", "Happy", "Not happy", "Desappointed"]
    )
    
    answers["What are the best brands and models, and why?"] = st.text_area(
        "What are the best brands and models, and why?"
    )
    
    answers["What are the worst brands and models, and why?"] = st.text_area(
        "What are the worst brands and models, and why?"
    )
    
    answers["Any brands or models missing in the portfolio?"] = st.text_area(
        "Any brands or models missing in the portfolio?"
    )
    
    answers["Easy to install?"] = st.text_area(
        "Easy to install?"
    )

    answers["Easy to maintain?"] = st.text_area(
        "Easy to maintain?"
    )

    answers["What do think could be improved about/in the endpoints?"] = st.text_area(
        "What do think could be improved about/in the endpoints?"
    )
    return answers
