import grpc
from fastapi import APIRouter
from google.protobuf.json_format import MessageToDict
from croydon.errors import ApiError, NotFound
from app.types import Airport
from app.proto.stub import get_new_stub
from app.proto.camden_pb2 import AirportRequest

airports_ctrl = APIRouter(prefix="/api/v1/airports")


@airports_ctrl.get("/{code}")
async def get_airport(code: str) -> Airport:
    stub = get_new_stub()
    try:
        resp = await stub.GetAirport(AirportRequest(code=code))
    except grpc.aio.AioRpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            raise NotFound(e.details())
        raise ApiError(e.details())
    dct = MessageToDict(resp.airport, preserving_proto_field_name=True)
    return Airport(**dct)
