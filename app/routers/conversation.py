from fastapi import APIRouter

from app.models.schemas import (
    EventInput,
    ConversationRequest,
    ConversationResponse,
    FactCheckRequest,
    FactCheckResponse
)

from app.services.event_analyzer import extract_event_themes
from app.services.topic_generator import generate_topics
from app.services.fact_checker import fact_check

router = APIRouter()

@router.post("/analyze-event")
def analyze_event(data: EventInput):
    topics = extract_event_themes(data.description)
    return {"topics": topics}


@router.post(
    "/generate-conversation",
    response_model=ConversationResponse
)
def generate_conversation(data: ConversationRequest):

    topics = extract_event_themes(data.description)

    suggestions = generate_topics(
        topics,
        data.interests
    )

    return ConversationResponse(
        topics=topics,
        suggestions=suggestions
    )


@router.post(
    "/fact-check",
    response_model=FactCheckResponse
)
def factcheck(data: FactCheckRequest):
    summary = fact_check(data.query)

    return FactCheckResponse(
        summary=summary
    )