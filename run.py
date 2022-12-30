# This file is responsible for running the application.
import uvicorn
from MinimalOpenAPIs.main import create_app

app = create_app()


if __name__ == "__main__":
    uvicorn.run("run:app", port=5000, reload=True)


