from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi import HTTPException

class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException as e:
            # FastAPI lanza excepciones HTTPException para errores de estado HTTP
            # Podemos devolver el detalle de la excepción directamente
            return JSONResponse(
                status_code=e.status_code,
                content={"message": e.detail}
            )
        except Exception as e:
            # Para todas las demás excepciones, devolvemos un error 500
            return JSONResponse(
                status_code=500,
                content={"message": str(e)}
            )