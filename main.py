from fastapi import FastAPI
from routes.user import user

app = FastAPI(

    title='test FastAPI',
    description='Prueba de FastAPI con SQLAlchemy',
    version='1.0',
    openapi_tags=[{"name": "users",
                   "description": "user routes"}]
)


app.include_router(user)
