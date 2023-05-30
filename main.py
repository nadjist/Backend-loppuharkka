from fastapi import FastAPI
import createPlayer, getPlayers, getPlayerById, createPlayerEvent, getEvents, getPlayerEvents

app = FastAPI()

app.include_router(createPlayer.router)
app.include_router(getPlayers.router)
app.include_router(getPlayerById.router)
app.include_router(createPlayerEvent.router)
app.include_router(getEvents.router)
app.include_router(getPlayerEvents.router)