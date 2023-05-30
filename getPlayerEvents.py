from fastapi import APIRouter, HTTPException
from database import events, players

router = APIRouter()

@router.get('/players/{id}/events')
def getPlayerEvents(id: int, type: str = ""):
    if not any(player['id'] == id for player in players):
        raise HTTPException(status_code=404, detail="Tuntematon pelaaja")
    if type not in ["level_started", "level_solved", ""]:
        raise HTTPException(status_code=400, detail="Tuntematon eventtityyppi")
    if type in ["level_started", "level_solved"]:
        playerEvents = list(filter(lambda event: event["type"] == type and event["player_id"] == id, events))
        return playerEvents
    playerEvents = list(filter(lambda event: event["player_id"] == id, events))
    return playerEvents