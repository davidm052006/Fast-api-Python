from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/echo", tags=["echo"])


class EchoRequest(BaseModel):
    message: str


@router.post("/", response_model=EchoRequest)
def echo_message(req: EchoRequest) -> EchoRequest:
    return req
