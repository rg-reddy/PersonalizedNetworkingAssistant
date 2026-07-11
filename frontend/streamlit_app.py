import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝",
    layout="wide"
)

st.title("🤝 Personalized Networking Assistant")
st.write(
    "Generate conversation starters for networking events based on your interests."
)

event_description = st.text_area(
    "📝 Enter Event Description",
    placeholder="AI in Public Health"
)

interests = st.text_input(
    "🎯 Your Interests (comma-separated)",
    placeholder="data ethics, patient safety, machine learning"
)

if st.button("Generate Conversation Starters"):

    if not event_description.strip():
        st.error("Please enter an event description.")
    else:
        user_interests = [
            x.strip() for x in interests.split(",") if x.strip()
        ]

        payload = {
            "description": event_description,
            "interests": user_interests
        }

        try:
            response = requests.post(
                f"{API_URL}/generate-conversation",
                json=payload,
                timeout=120
            )

            if response.status_code == 200:
                data = response.json()

                st.subheader("🧠 Extracted Topics")
                st.json(data.get("topics", []))

                st.subheader("💬 Conversation Starters")

                for idx, suggestion in enumerate(
                        data.get("suggestions", []), start=1):
                    st.markdown(
                        f"**{idx}. {suggestion}**"
                    )

                if data.get("topics"):
                    topic = data["topics"][0]

                    fact_response = requests.post(
                        f"{API_URL}/fact-check",
                        json={"query": topic},
                        timeout=120
                    )

                    if fact_response.status_code == 200:
                        st.subheader("📚 Fact Check")
                        st.write(
                            fact_response.json().get(
                                "summary",
                                "No information found."
                            )
                        )

            else:
                st.error(
                    f"API Error: {response.status_code}"
                )

        except Exception as e:
            st.error(str(e))