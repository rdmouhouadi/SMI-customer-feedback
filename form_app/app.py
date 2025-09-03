import streamlit as st
import pandas as pd
from datetime import datetime
import uuid
import importlib
import os

# ---------------------
# Page Config
# ---------------------
st.set_page_config(
    page_title="Digital Solutions - Smart Metering International Customer Feedback Form",
    layout="wide",
    page_icon="📋"
)


# ---------------------
# File Setup
# ---------------------
responses_file = "../responses.csv"

# Create responses file if it doesn't exist
if not os.path.exists(responses_file):
    pd.DataFrame(columns=[
        "Customer ID", "Name", "Email", "Company",
        "Topic", "Question", "Answer", "Timestamp"
    ]).to_csv(responses_file, index=False)

# ---------------------
# Logo and Header
# ---------------------

st.logo(image="images/Logo_Suez.png", icon_image="images/Logo_Suez.png",size="large")


st.markdown("""
    <div style='text-align: center; margin-top: -20px; margin-bottom: 20px;'>
        <h1 style='color: #003366; font-size: 28px;'>Digital Solutions - Smart Metering International Customer Feedback Form</h1>
        <p style='font-size: 16px; color: #555;'>We appreciate your feedback.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------
# Topics
# ---------------------
topic_modules = {
    "General": "general",
    "WIZE": "wize",
    "End-points (meters and transmitters)": "endpoints",
    "PeauseNG": "peauseng",
    "NFC dongle": "nfc_dongle",
    "Concentrators (K2G)": "k2g",
    "ONconnect Gateway Manager (OGM)": "ogm",
    "ONconnect MDM": "onconnect_mdm",
    "Support services and Project Management": "support_services"
}
topics = list(topic_modules.keys())

# ---------------------
# Session State Init
# ---------------------
for key in ["name", "company", "email", "customer_id"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# ---------------------
# Customer Info Form (First Step)
# ---------------------
if not all([st.session_state.name, st.session_state.company, st.session_state.email]):
    with st.form("customer_info_form"):
        st.subheader("👤 Client Details")
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        company = st.text_input("Your Company Name")
        submit_info = st.form_submit_button("Continue")

        if submit_info and name and email and company:
            st.session_state.name = name
            st.session_state.email = email
            st.session_state.company = company
    
            # Try to find existing customer_id from responses.csv
            responses_file = "../responses.csv"
            customer_id = None
            if os.path.exists(responses_file):
                df = pd.read_csv(responses_file)
                # Search for existing customer with same name/email/company
                match = df[
                    (df["Name"] == name) &
                    (df["Email"] == email) &
                    (df["Company"] == company)
                ]
                if not match.empty:
                    customer_id = match.iloc[0]["Customer ID"]
            
            # If no existing customer, generate new UUID
            if customer_id:
                st.session_state.customer_id = customer_id
            else:
                st.session_state.customer_id = str(uuid.uuid4())
                
            st.rerun()

else:
    # ---------------------
    # Load existing responses for this customer to show checkmarks
    # ---------------------
    responses_file = "../responses.csv"

    responses_file = "../responses.csv"

    completed_topics = set()

    if os.path.exists(responses_file):
        df_responses = pd.read_csv(responses_file)
        # Filter responses for current customer
        df_cust = df_responses[df_responses["Customer ID"] == st.session_state.customer_id]
        completed_topics = set(df_cust["Topic"].unique())

    # ---------------------
    # Sidebar with checkmarks
    # ---------------------
    sidebar_labels = []
    for topic in topics:
        label = f"{topic} ✅" if topic in completed_topics else topic
        sidebar_labels.append(label)

    # Map label to original topic for lookup after selection
    label_to_topic = {label: topic for label, topic in zip(sidebar_labels, topics)}

    st.sidebar.title("🧭 Navigate Form")
    selected_label = st.sidebar.radio("Select a section:", sidebar_labels)
    selected_topic = label_to_topic[selected_label]

    # ---------------------
    # Welcome Message
    # ---------------------
    st.success(f"Hello **{st.session_state.name}** from **{st.session_state.company}**, welcome to our smart metering feedback portal. Use the sidebar to navigate between sections and fill out each topic's questions.")

    # ---------------------
    # Load Selected Topic Module
    # ---------------------
    topic_key = topic_modules[selected_topic]
    topic_module = importlib.import_module(f"topics.{topic_key}")

    # ---------------------
    # Render Topic Form
    # ---------------------
    with st.form(f"{selected_topic}_form"):
        st.markdown(f"### 📝 {selected_topic} Feedback")
        answers = topic_module.render()  # Returns a dict {question: answer}
        submitted = st.form_submit_button("Submit This Section")

        if submitted:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            rows = []
            for question, answer in answers.items():
                row = {
                    "Customer ID": st.session_state.customer_id,
                    "Name": st.session_state.name,
                    "Email": st.session_state.email,
                    "Company": st.session_state.company,
                    "Topic": selected_topic,
                    "Question": question,
                    "Answer": answer,
                    "Timestamp": timestamp
                }
                rows.append(row)

            df = pd.DataFrame(rows)
            df.to_csv(responses_file, mode="a", header=not os.path.exists(responses_file), index=False)
            st.success(f"Your answers for **{selected_topic}** have been saved. Thank you!")
            st.rerun()
