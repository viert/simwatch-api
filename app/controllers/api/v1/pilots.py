import grpc
from fastapi import APIRouter
from google.protobuf.json_format import MessageToDict
from croydon.errors import ApiError, NotFound
from app.types import Pilot
from app.proto.stub import get_new_stub
from app.proto.camden_pb2 import PilotRequest

pilots_ctrl = APIRouter(prefix="/api/v1/pilots")


@pilots_ctrl.get("/{callsign}")
async def get_pilot(callsign: str) -> Pilot:
    stub = get_new_stub()
    try:
        resp = await stub.GetPilot(PilotRequest(callsign=callsign))
    except grpc.aio.AioRpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            raise NotFound(e.details())
        raise ApiError(e.details())
    dct = MessageToDict(resp.pilot, preserving_proto_field_name=True)
    return Pilot(**dct)
