from fastapi import APIRouter, HTTPException
from database import players

router = APIRouter()


@router.get('/players/{id}')
def getPlayerById(id: int):
    if id not in players:
        raise HTTPException(status_code=404, message="Tuntematon pelaaja")
    return players[id]