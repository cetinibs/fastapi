from pydantic import Schema

from starlette.requests import Request

from .base import SecurityBase, Types


class HTTPBase(SecurityBase):
    type_ = Schema(Types.http, alias="type")
    scheme: str

    async def __call__(self, request: Request):
        return request.headers.get("Authorization")


class HTTPBasic(HTTPBase):
    scheme = "basic"


class HTTPBearer(HTTPBase):
    scheme = "bearer"
    bearerFormat: str = None


class HTTPDigest(HTTPBase):
    scheme = "digest"