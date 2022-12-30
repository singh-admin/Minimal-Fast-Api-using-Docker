from fastapi import APIRouter, Response, Depends
from pydantic import BaseModel, Field
from .control import dummy_control
from fastapi.security.api_key import APIKeyHeader


api_key_header = APIKeyHeader(name='X-API-Key')

#create the instance of Api Router.
router = APIRouter(
                prefix="/api/dummy",
                tags=["Token API"]
                )


#create the pydentic model for validation.
class dummy_payload(BaseModel):
    str1: str = Field(title="dummy", description="Provide the valid dummy data")
    str2: str = Field(title="dummy", description="Provide the valid dummy data")
    str3: str = Field(title="dummy", description="Provide the valid dummy data")
    str4: str = Field(title="dummy", description="Provide the valid dummy data")

    class Config:
        schema_extra = {
            "example": {
                "str1": "Dummy_data",
                "str2": "Dummy_data",
                "str3": "Dummy_data",
                "str4": "Dummy_data",
            }
        }


responses = {
    403: {"description": " Forbidden Error"},
    404: {"description": "Not Found"},
    500: {"description": "Server is not responding"},

}

@router.post("/postData", responses={**responses})
async def post_data(model: dummy_payload, response: Response, key: str = Depends(api_key_header)):
    try:
        if model:
            return dummy_control(model.dict(), key, response)
        else:
            response.status_code = 403
    except Exception:
        return {"Unsuccessful": "Server is not responding"}
