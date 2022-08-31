from fastapi import FastAPI
from routes.route import api
from fastapi.middleware.cors import CORSMiddleware

from fastapi_mqtt import FastMQTT, MQTTConfig



from fastapi_mail import FastMail, MessageSchema,ConnectionConfig


app=FastAPI()


app.include_router(api)


origins = ["https://a865-197-1-81-117.eu.ngrok.io","http://localhost","http://localhost:4200","http://localhost:4201","http://127.0.0.1:8080","http://192.168.1.7:8080","http://172.20.240.1:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)












