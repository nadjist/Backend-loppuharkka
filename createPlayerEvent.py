from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import events, players
from datetime import datetime

router = APIRouter()



class EventBase(BaseModel):
    type: str
    detail: str

class Event(EventBase):
    id: int
    timestamp: datetime
    player_id: int

@router.post('/players/{id}/events', status_code=201)
def createEvent(eventIn: EventBase, id: int):
    if not any(player['id'] == id for player in players):
        raise HTTPException(status_code=404, detail="Tuntematon pelaaja")
    if eventIn.type not in ["level_started", "level_solved"]:
        raise HTTPException(status_code=400, detail="Tuntematon eventtityyppi")
    ts = datetime.now()
    newEventId = len(events)
    event = Event(**eventIn.dict(), id = newEventId, timestamp = ts, player_id = id)
    events.append(event.dict())
    return event
