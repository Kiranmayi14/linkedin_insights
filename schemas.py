from pydantic import BaseModel

# Schemas for API requests/responses
class PageCreate(BaseModel):
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

class PageResponse(BaseModel):
    id: int
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

class PostResponse(BaseModel):
    id: int
    page_id: str
    content: str
    likes: int
    comments_count: int
    posted_at: str

class SocialMediaUserResponse(BaseModel):
    id: int
    page_id: str
    name: str
    role: str

class CommentResponse(BaseModel):
    id: int
    post_id: int
    user_id: int
    content: str
    commented_at: str

    
    