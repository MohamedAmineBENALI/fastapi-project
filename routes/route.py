from fastapi import APIRouter
from config.db import conn
from models.models import demo
from schemas.schemas import sh_demo


api =APIRouter()

    

@api.get("/param/select")
async def paramSelect():
    return conn.execute(demo.select()).first()

@api.put("/param/param_update")
async def param_update(d:sh_demo):
    conn.execute(demo.update().values(
        time=d.time,
        speed=d.speed,
        mode_fonctionnement=d.mode
    ))






