from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


tags_metadata = [

    {
        "name": "Dummy API",
        "description": "",
        "externalDocs": {
            "description": "",
            "url": "",
        },
    }
]

app = FastAPI(
        
        title = "Open Apis",
        description="""""",
        swagger_ui_parameters={"syntaxHighlight.theme": "obsidian",
                                "operationsSorter": "method",
                              },
        version="3.0.2",
        contact={
        },
        openapi_tags=tags_metadata
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Open Apis",
        version="",
        description="""""",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": ""
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema
app.openapi = custom_openapi


def create_app():
    from .public_apis.dummy import view
    app.include_router(view.router)
    return app
