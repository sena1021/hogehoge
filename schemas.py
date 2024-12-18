from pydantic import BaseModel

# ユーザー作成用リクエストスキーマ
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

# ユーザーのレスポンススキーマ
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
