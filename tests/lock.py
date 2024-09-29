import asyncio

from contextlib import asynccontextmanager
from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache


@asynccontextmanager
async def lifespan(_):
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/cached-route")
@cache(expire=10)
async def cached_route():
    print('Function invoked')
    await asyncio.sleep(5)
    return dict(hello="world")

