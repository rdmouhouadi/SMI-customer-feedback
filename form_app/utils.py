import os
import pandas as pd
from datetime import datetime

from config import RESPONSES_FILE

def init_responses_file():
    if not os.path.exists(RESPONSES_FILE):
        pd.DataFrame(columns=[
            "Customer ID", "Name", "Email", "Company",
            "Topic", "Question", "Answer", "Timestamp"
        ]).to_csv(RESPONSES_FILE, index=False)

def load_responses():
    if os.path.exists(RESPONSES_FILE):
        return pd.read_csv(RESPONSES_FILE)
    return pd.DataFrame()

def save_responses(new_df, customer_id, topic):
    df_existing = load_responses()
    df_existing = df_existing[
        ~((df_existing["Customer ID"] == customer_id) &
          (df_existing["Topic"] == topic))
    ]
    df_updated = pd.concat([df_existing, new_df], ignore_index=True)
    df_updated.to_csv(RESPONSES_FILE, index=False)

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
