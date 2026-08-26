from pydantic import BaseModel, Field


class GameModel(BaseModel):
    app_id: int = Field(alias="appid")
    name: str = Field(alias="name", default="unknown")
    playtime_forever: int = Field(alias="playtime_forever", default=0)


class PlayerStats(BaseModel):
    steam_id: str
    games: list[GameModel] = []
