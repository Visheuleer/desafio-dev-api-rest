from fastapi import FastAPI
from routes import account_holder_router
from models import Base
from mysqldb import db_connection



app = FastAPI()

app.include_router(account_holder_router)

if __name__ == "__main__":
    import uvicorn
    Base.metadata.create_all(bind=db_connection.engine)
    uvicorn.run(app)




