from fastapi import APIRouter, HTTPException
from database import players, events
from createPlayer import Player
from createPlayerEvent import Event

router = APIRouter()


class PlayerEvents(Player):
    events: list[Event]

@router.get('/players/{id}')
def getPlayerById(id: int):
    if not any(player['id'] == id for player in players):
        raise HTTPException(status_code=404, detail="Tuntematon pelaaja")
    playerById = next(player for player in players if player["id"] == id)
    eventsById = list(filter(lambda event: event["player_id"] == id, events))
    playerEvents = PlayerEvents(**playerById, events = eventsById)
    return playerEvents