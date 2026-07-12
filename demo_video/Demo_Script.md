# Personalized Networking Assistant Demo Script

## 1. Introduction

Hello everyone.

I am Raja Gopala Reddy Bora,
Fourth Year B.Tech student,
Computer Science and Engineering with Artificial Intelligence and Machine Learning,
MVGR College of Engineering.

My roll number is 23331A4208.

Today I am presenting my SmartBridge Capstone Project:

Personalized Networking Assistant.

---

## 2. Problem Statement

Networking events such as conferences, workshops, seminars, and hackathons often make it difficult for participants to identify meaningful conversation topics quickly.

Many students and professionals struggle to initiate discussions with strangers despite sharing common interests.

This project addresses this problem using Artificial Intelligence and Natural Language Processing.

---

## 3. Project Objective

The objective of this project is to generate intelligent and personalized conversation starters based on:

- Event description
- User interests
- Event themes

The system also provides factual information to help users participate confidently in discussions.

---

## 4. Technology Stack

This project uses the following technologies:

- FastAPI for backend APIs
- Streamlit for frontend interface
- HuggingFace Transformers
- DistilBERT Zero-Shot Classification
- GPT-2 Text Generation
- PyTorch
- Wikipedia API
- HTTPX
- Pydantic
- Pytest
- Uvicorn

---

## 5. Project Structure

The project follows SmartBridge recommended structure.

```
app/
frontend/
tests/
data/
logs/
screenshots/
demo_video/
README.md
requirements.txt
```

---

## 6. Backend Demonstration

First, I start the FastAPI backend server.

Command:

```cmd
uvicorn app.main:app --reload
```

The backend starts successfully and loads the AI models.

Next, I open Swagger documentation.

URL:

```
http://127.0.0.1:8000/docs
```

Available APIs include:

- Analyze Event
- Generate Conversation
- Fact Check

---

## 7. Event Theme Extraction

Now I demonstrate event theme extraction.

Input:

```
AI in healthcare and robotics conference focusing on patient care and automation
```

The DistilBERT model extracts the following themes:

- Robotics
- Healthcare
- Artificial Intelligence

This helps identify the major topics of the event.

---

## 8. Conversation Starter Generation

Next, GPT-2 generates conversation starters.

User interests:

- Machine Learning
- Patient Safety

Generated topics include:

- Robotic Surgery
- Machine Learning
- Human Intelligence

These suggestions help participants start meaningful conversations during networking events.

---

## 9. Fact Checking

The system also provides factual information using Wikipedia API.

Example:

Artificial Intelligence is the capability of computational systems to perform tasks typically associated with human intelligence.

This feature improves user confidence and discussion quality.

---

## 10. Frontend Demonstration

Now I open the Streamlit frontend.

Command:

```cmd
streamlit run frontend\streamlit_app.py
```

The application opens successfully.

The user enters:

### Event Description

```
AI in healthcare and robotics conference focusing on patient care and automation
```

### User Interests

```
machine learning, patient safety
```

The user clicks:

```
Generate Conversation Starters
```

The system then displays:

### Extracted Topics

- Robotics
- Healthcare
- Artificial Intelligence

### Conversation Starters

- Robotic Surgery
- Machine Learning
- Human Intelligence

### Fact Check Output

The system provides factual information related to the generated topics.

---

## 11. GitHub Repository

The project repository contains:

- Source Code
- README Documentation
- Screenshots
- Requirements File
- Demo Video

Repository:

https://github.com/rg-reddy/PersonalizedNetworkingAssistant

---

## 12. Future Enhancements

Future improvements include:

- Larger language models
- Better personalization
- User profile support
- Cloud deployment
- Recommendation systems

---

## 13. Conclusion

This project demonstrates practical application of:

- Natural Language Processing
- Transformer Models
- REST APIs
- AI-powered Recommendation Systems

Thank you for your time and attention.

Thank you.