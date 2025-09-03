import streamlit as st

def show_customer_info_form():
    with st.form("customer_info_form"):
        st.subheader("👤 Client Details")
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        company = st.text_input("Your Company Name")
        submit_info = st.form_submit_button("Continue")
    return name, email, company, submit_info

def show_thank_you_page():
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; margin-top: 50px;'>
            <h2 style='color: #003366;'>🎉 Thank You for Your Feedback!</h2>
            <p style='font-size: 18px; margin-top: 20px;'>
                Your feedback is important to us. We will take it into consideration 
                to improve our solutions for your needs.
            </p>
            <p style='font-size: 16px; margin-top: 40px; font-style: italic;'>
                From the Suez Smart Metering International team
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.stop()
