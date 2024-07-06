from pydantic import BaseModel


class SignUp(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username": "Ahmed",
                "password": "@hm3d"
            }
        }
