from pydantic import BaseModel, Field


# memo 参照定義
class MemoSchema(BaseModel):
    memo_id: int = Field()
    content: str = Field(max_length=100)

    class Config:
        orm_mode = True


class MemoCreatingSchema(BaseModel):
    content: str = Field(max_length=100)

    class Config:
        orm_mode = True

