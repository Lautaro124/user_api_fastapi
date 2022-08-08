from pydantic import BaseModel, Field

class SchemaUser(BaseModel):
    name: str = Field(
        ..., 
        min_length = 1,
        max_length = 50,
    )
    age: int = Field(..., gt=0, le= 150)
    status_id: int = Field(...)

    class Config:
        orm_mode= True

class SchemaStatusUser(BaseModel):
    name: str = Field(...)
    is_dangerous: bool = Field(...)

    class Config:
        orm_mode= True