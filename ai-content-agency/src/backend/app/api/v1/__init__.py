from fastapi import APIRouter

from . import auth, brands, generate, contents

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(brands.router, prefix="/brands", tags=["Brands"])
api_router.include_router(generate.router, prefix="/generate", tags=["Content Generation"])
api_router.include_router(contents.router, prefix="/contents", tags=["Contents"])
