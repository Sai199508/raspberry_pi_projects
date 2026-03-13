from fastapi import FastAPI
from .device_service import DeviceService

app = FastAPI()
device = DeviceService()


@app.get("/")
def root():
    return {"message": "Home Automation API Running"}


@app.post("/light/on")
def light_on():
    return {"status": device.light_on()}


@app.post("/light/off")
def light_off():
    return {"status": device.light_off()}
