from pydantic import BaseModel

class PageBase(BaseModel):
    page_id: str
    name: str
    url: str
    profile_picture_url: str
    description: str
    website: str
    industry: str
    total_followers: int
    head_count: int
    specialities: str

class PostBase(BaseModel):
    page_id: str
    content: str
    likes: int
    comments_count: int

class SocialMediaUserBase(BaseModel):
    page_id: str
    name: str
    role: str

class CommentBase(BaseModel):
    post_id: int
    user_id: int
    content: str

    