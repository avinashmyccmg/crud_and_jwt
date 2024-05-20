from fastapi import FastAPI
from models import model
from database import engine
from routers import organization, user, authentication


app = FastAPI()

model.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(organization.router)
app.include_router(user.router)





