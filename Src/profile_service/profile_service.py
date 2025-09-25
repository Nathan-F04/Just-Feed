"""Module for the profile setting service"""
from fastapi import FastAPI, HTTPException, status
from .schemas import User

ProfileService = FastAPI()
profiles: list[Profile] = []

@app.put("/api/profile/", status_code=status.HTTP_201_CREATED)
def update_profile(profile: Profile):
    """Edits a profile in the profile list"""
    for p in profiles:
        if(p.profile_id == profile.profile_id):
            profiles[profiles.index(p)] = profile 
            return profile
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")