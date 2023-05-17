import uvicorn
from script.config import Service

if __name__ == "__main__":
    uvicorn.run("course:app",host=Service.host, port=Service.port)