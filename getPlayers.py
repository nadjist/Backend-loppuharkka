from fastapi import APIRouter
from database import players

router = APIRouter()


@router.get('/players')
def getPlayers():
    return players