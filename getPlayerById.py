from fastapi import APIRouter, HTTPException
from database import players

router = APIRouter()


@router.get('/players/{id}')
def getPlayerById(id: int):
    if not any(player['id'] == id for player in players):
        raise HTTPException(status_code=404, detail="Tuntematon pelaaja")
    return players[id]