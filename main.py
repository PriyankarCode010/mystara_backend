import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import leetcode_routes, gfg_routes, github_routes

app = FastAPI()

# Routers
app.include_router(leetcode_routes.router, prefix="/leetcode")
app.include_router(gfg_routes.router, prefix="/gfg")
app.include_router(github_routes.router, prefix="/github")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Run uvicorn only if local
if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 8080))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
