from fastapi import FastAPI
from routes import gfg_routes, github_routes, leetcode_routes

app = FastAPI()

# Register routes
app.include_router(gfg_routes.router)
app.include_router(github_routes.router)
app.include_router(leetcode_routes.router)

@app.get("/")
def root():
    return {"message": "Mystara Backend is running 🚀"}
