from fastapi import APIRouter
from database import players

router = APIRouter()


@router.get('/players/{id}')
def getPlayerById(id: int):

    return players[id]