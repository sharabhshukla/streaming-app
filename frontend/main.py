from fastapi import FastAPI
from faststream.redis import RedisBroker


app = FastAPI()
broker = RedisBroker(host="redis-svc", port=6379)


@app.on_event("startup")
async def connect_to_redis():
    await broker.connect()

@app.on_event("shutdown")
def disconnect_from_redis():
    broker.close()

@app.get("/")
async def root():
    await broker.publish(message="Root accessed!!", channel="opt_app")
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    await broker.publish(message=f"Greetings accessed {name}", channel="opt_app")
    return {"message": f"Hello {name}"}
