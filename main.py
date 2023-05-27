from fastapi import FastAPI
import createPlayer, getPlayers, getPlayerById

app = FastAPI()

app.include_router(createPlayer.router)
app.include_router(getPlayers.router)
app.include_router(getPlayerById.router)