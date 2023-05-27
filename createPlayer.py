from fastapi import APIRouter
from pydantic import BaseModel
from database import players

router = APIRouter()

class PlayerBase(BaseModel):
    name: str

class Player(PlayerBase):
    id: int

@router.post('/player', status_code=201)
def createPlayer(playerIn: PlayerBase):
    newPlayerId = len(players)
    player = Player(**playerIn.dict(), id = newPlayerId)
    players.append(player.dict())
    return player