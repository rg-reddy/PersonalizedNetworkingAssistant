from transformers import pipeline, set_seed

set_seed(42)

generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_topics(event_themes, user_interests):
    prompt = (
        "Networking Event Topics: "
        + ", ".join(event_themes)
        + "\nUser Interests: "
        + ", ".join(user_interests)
        + "\nConversation Starters:\n1."
    )

    output = generator(
        prompt,
        max_new_tokens=50,
        do_sample=True,
        temperature=0.8,
        top_k=50,
        top_p=0.95,
        pad_token_id=50256,
        return_full_text=False
    )

    text = output[0]["generated_text"]

    suggestions = []

    for line in text.split("\n"):
        line = line.strip()
        if line:
            suggestions.append(line)

    return suggestions[:3]