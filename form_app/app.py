import streamlit as st
import importlib
import pandas as pd
import uuid

from config import TOPICS, TOPIC_MODULES
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
# Init
# ---------------------
init_responses_file()


# ---------------------
# Step 1: Customer Info
# ---------------------
if not all([st.session_state.get("name"), st.session_state.get("email"), st.session_state.get("company")]):
    name, email, company, submit_info = show_customer_info_form()
    if submit_info and name and email and company:
        st.session_state["name"] = name
        st.session_state["email"] = email
        st.session_state["company"] = company
        st.session_state["customer_id"] = str(uuid.uuid4())
        st.rerun()


# ---------------------
# Step 2: Load Responses and Check Completion
# ---------------------
if all([st.session_state.get("name"), st.session_state.get("company"), st.session_state.get("email")]):
    df_responses = load_responses()
    completed_topics = set(
        df_responses[df_responses["Customer ID"] == st.session_state.customer_id]["Topic"].unique()
    )

    if len(completed_topics) == len(TOPICS):
        show_thank_you_page()


    # ---------------------
    # Sidebar Navigation
    # ---------------------
    sidebar_labels = []
    for topic in TOPICS:
        label = f"{topic} ✅" if topic in completed_topics else topic
        sidebar_labels.append(label)

    label_to_topic = {label: topic for label, topic in zip(sidebar_labels, TOPICS)}

    if "selected_label" not in st.session_state:
        st.session_state.selected_label = sidebar_labels[0]

    if st.session_state.selected_label not in sidebar_labels:
        original_topic = label_to_topic.get(st.session_state.selected_label, None)
        st.session_state.selected_label = (
            f"{original_topic} ✅" if original_topic in completed_topics else original_topic
        ) if original_topic else sidebar_labels[0]

    selected_label = st.sidebar.radio(
        "Select a section:",
        sidebar_labels,
        index=sidebar_labels.index(st.session_state.selected_label)
    )

    st.session_state.selected_label = selected_label
    selected_topic = label_to_topic[selected_label]


    # ---------------------
    # Welcome Message
    # ---------------------
    st.success(
        f"Hello **{st.session_state.name}** from **{st.session_state.company}**! "
        "Use the sidebar to navigate and fill out each topic's questions."
    )


    # ---------------------
    # Topic Form
    # ---------------------
    topic_key = TOPIC_MODULES[selected_topic]
    topic_module = importlib.import_module(f"topics.{topic_key}")

    with st.form(f"{selected_topic}_form"):
        st.markdown(f"### 📝 {selected_topic} Feedback")
        answers = topic_module.render()
        submitted = st.form_submit_button("Submit This Section")

        if submitted:
            rows = []
            for question, answer in answers.items():
                rows.append({
                    "Customer ID": st.session_state.customer_id,
                    "Name": st.session_state.name,
                    "Email": st.session_state.email,
                    "Company": st.session_state.company,
                    "Topic": selected_topic,
                    "Question": question,
                    "Answer": answer,
                    "Timestamp": timestamp()
                })
            new_df = pd.DataFrame(rows)
            save_responses(new_df, st.session_state.customer_id, selected_topic)
            st.success(f"Your answers for **{selected_topic}** have been saved. Thank you!")
            st.rerun()
