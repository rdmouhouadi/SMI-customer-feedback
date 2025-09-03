# config.py
RESPONSES_FILE = "../responses.csv"
TOPIC_MODULES = {
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
TOPICS = list(TOPIC_MODULES.keys())
