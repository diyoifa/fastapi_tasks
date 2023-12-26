from fastapi import FastAPI, status
from .middlewares.cors import setup_cors
from .middlewares.exception_handler import ExceptionHandlerMiddleware
from .routers import user
from .routers import auth
from .routers import task

app = FastAPI(
  title="FastAPI & MongoDb Rest_API with JWT Authentication",
  description="This repository contains a simple REST API developed using FastAPI, MongoDB, and JWT for authentication.",
  version="0.0.1",
)

#MIDDLEWARES
setup_cors(app)
app.add_middleware(ExceptionHandlerMiddleware)

#ROUTERS
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(task.router)

@app.get("/", tags=["Root"], status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Hello World"}

