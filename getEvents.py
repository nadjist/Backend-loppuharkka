from fastapi import APIRouter, HTTPException
from database import events

router = APIRouter()


@router.get('/events')
def getEvents(type: str = ""):
    if type not in ["level_started", "level_solved", ""]:
        raise HTTPException(status_code=400, detail="Tuntematon eventtityyppi")
    if type in ["level_started", "level_solved"]:
        listOfEvents = list(filter(lambda event: event['type'] == type, events))
        return listOfEvents
    return events