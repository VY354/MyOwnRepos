from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int = Field(default=-1)
    date: str = Field(default='1970-01-01 00:00:00')
    title: str = Field(default='empty title')
    text: str = Field(default='empty text')


if __name__ == '__main__':
    t = Task()
    print(t.dict())
