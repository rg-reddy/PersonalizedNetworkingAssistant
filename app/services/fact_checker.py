import wikipedia

def fact_check(query):
    try:
        results = wikipedia.search(query)

        if not results:
            return "No information found."

        page_title = results[0]

        return wikipedia.summary(
            page_title,
            sentences=2,
            auto_suggest=False
        )

    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(
            e.options[0],
            sentences=2,
            auto_suggest=False
        )

    except Exception as e:
        return f"Fact check failed: {e}"