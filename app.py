from fastapi import FastAPI
from routes.route import api
from fastapi.middleware.cors import CORSMiddleware

from fastapi_mqtt import FastMQTT, MQTTConfig



from fastapi_mail import FastMail, MessageSchema,ConnectionConfig


app=FastAPI()


app.include_router(api)


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)












