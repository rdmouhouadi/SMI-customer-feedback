import streamlit as st
import importlib
import pandas as pd
import uuid
import os

from config import TOPICS, TOPIC_MODULES, RESPONSES_FILE
from utils import init_responses_file, load_responses, save_responses, timestamp
from components import show_customer_info_form, show_thank_you_page

# ---------------------
# Page Config
# ---------------------
st.set_page_config(
    page_title="Digital Solutions - Smart Metering International Customer Feedback Form",
    layout="wide",
    page_icon="📋"
)

# ---------------------
# Initialize responses file
# ---------------------
init_responses_file()

# ---------------------
# Logo and Header
# ---------------------
st.logo(image="images/Logo_Suez.png", icon_image="images/Logo_Suez.png", size="large")

st.markdown("""
    <div style='text-align: center; margin-top: -20px; margin-bottom: 20px;'>
        <h1 style='color: #003366; font-size: 28px;'>Digital Solutions - Smart Metering International </h1>
        <p style='font-size: 16px; color: #555;'>Customer Feedback Form</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------
# Session State Init
# ---------------------
for key in ["name", "company", "email", "customer_id", "selected_label", "finished"]:
    if key not in st.session_state:
        st.session_state[key] = "" if key != "finished" else False

# ---------------------
# Step 1: Customer Info Form
# ---------------------
if not all([st.session_state["name"], st.session_state["email"], st.session_state["company"]]):
    name, email, company, submit_info = show_customer_info_form()
    if submit_info and name and email and company:
        st.session_state["name"] = name
        st.session_state["email"] = email
        st.session_state["company"] = company

        # Try to reuse existing customer_id
        df_existing = load_responses()
        match = df_existing[
            (df_existing["Name"] == name) &
            (df_existing["Email"] == email) &
            (df_existing["Company"] == company)
        ]
        st.session_state["customer_id"] = match.iloc[0]["Customer ID"] if not match.empty else str(uuid.uuid4())
        st.session_state["selected_label"] = TOPICS[0]
        st.rerun()

# ---------------------
# Step 2: Load Responses and Check Completion
# ---------------------
if all([st.session_state["name"], st.session_state["company"], st.session_state["email"]]):
    df_responses = load_responses()
    df_customer = df_responses[df_responses["Customer ID"] == st.session_state.customer_id]
    completed_topics = set(df_customer["Topic"].unique())

    # Check if finished
    if len(completed_topics) == len(TOPICS):
        st.session_state["finished"] = True

    if st.session_state["finished"]:
        show_thank_you_page()

    # ---------------------
    # Sidebar Navigation
    # ---------------------
    sidebar_labels = [f"{t} ✅" if t in completed_topics else t for t in TOPICS]
    label_to_topic = {label: topic for label, topic in zip(sidebar_labels, TOPICS)}

    # Ensure selected_label exists
    if not st.session_state["selected_label"] or st.session_state["selected_label"] not in sidebar_labels:
        plain_topic = st.session_state["selected_label"].replace(" ✅", "")
        st.session_state["selected_label"] = f"{plain_topic} ✅" if plain_topic in completed_topics else plain_topic
        if st.session_state["selected_label"] not in sidebar_labels:
            st.session_state["selected_label"] = sidebar_labels[0]

    selected_label = st.sidebar.radio(
        "Topics:",
        sidebar_labels,
        index=sidebar_labels.index(st.session_state["selected_label"])
    )
    st.session_state["selected_label"] = selected_label
    selected_topic = label_to_topic[selected_label]

    # ---------------------
    # Welcome + Warning Messages (stacked)
    # ---------------------
    st.info(
        f" Hello **{st.session_state['name']}** from **{st.session_state['company']}**, "
        "welcome to our Smart Metering feedback portal. Use the navigation buttons to fill out each topic's questions.",
        icon="👋"
    )

    st.warning(
    "⚠️Important: Your answers are **automatically saved** after each section submission.\n\n"
    "Do **not refresh** the page while completing the form, as this will require you to re-enter the exact credentials (name, email, and company) you provided in order to resume where you left off."
)

    # ---------------------
    # Topic Form
    # ---------------------
    topic_key = TOPIC_MODULES[selected_topic]
    topic_module = importlib.import_module(f"topics.{topic_key}")

    with st.form(f"{selected_topic}_form"):
        st.markdown(f"### 📝 {selected_topic} Feedback")
        answers = topic_module.render()  # should return dict {question: answer}
        submitted = st.form_submit_button("Submit This Section")

        if submitted:
            rows = []
            for question, answer in answers.items():
                rows.append({
                    "Customer ID": st.session_state["customer_id"],
                    "Name": st.session_state["name"],
                    "Email": st.session_state["email"],
                    "Company": st.session_state["company"],
                    "Topic": selected_topic,
                    "Question": question,
                    "Answer": answer,
                    "Timestamp": timestamp()
                })
            new_df = pd.DataFrame(rows)
            save_responses(new_df, st.session_state["customer_id"], selected_topic)
            #st.success(f"Your answers for **{selected_topic}** have been saved. Thank you!")

            # Jump to next incomplete topic
            remaining = [t for t in TOPICS if t not in completed_topics or t == selected_topic]
            next_topic = remaining[0] if remaining[0] != selected_topic else (remaining[1] if len(remaining) > 1 else selected_topic)
            next_label = [lbl for lbl, t in label_to_topic.items() if t == next_topic][0]
            st.session_state["selected_label"] = next_label
            st.rerun()

    # ---------------------
    # Navigation Buttons
    # ---------------------
    topic_index = TOPICS.index(selected_topic)
    col1, col2, col3 = st.columns([1,2,1])

    if col1.button("⬅️ Previous", disabled=(topic_index == 0)):
        prev_topic = TOPICS[topic_index - 1]
        prev_label = [lbl for lbl, t in label_to_topic.items() if t == prev_topic][0]
        st.session_state["selected_label"] = prev_label
        st.rerun()

    if col3.button("Next ➡️", disabled=(topic_index == len(TOPICS) - 1)):
        next_topic = TOPICS[topic_index + 1]
        next_label = [lbl for lbl, t in label_to_topic.items() if t == next_topic][0]
        st.session_state["selected_label"] = next_label
        st.rerun()
