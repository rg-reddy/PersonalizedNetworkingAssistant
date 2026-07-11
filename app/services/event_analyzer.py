from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli"
)

def extract_event_themes(description, candidate_labels=None):
    if candidate_labels is None:
        candidate_labels = [
            "Artificial Intelligence",
            "Healthcare",
            "Blockchain",
            "Education",
            "Sustainability",
            "Robotics",
            "Cybersecurity",
            "Finance",
            "Cloud Computing",
            "Machine Learning"
        ]

    result = classifier(description, candidate_labels)

    return result["labels"][:3]
