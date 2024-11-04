from fastapi import FastAPI
from routes import account_holder_router, wallet_router
from models import Base
from mysqldb import db_connection



app = FastAPI()

app.include_router(account_holder_router)
app.include_router(wallet_router)

if __name__ == "__main__":
    import uvicorn
    Base.metadata.create_all(bind=db_connection.engine)
    uvicorn.run(app, host='0.0.0.0', port=8080)




