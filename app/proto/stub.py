import grpc
from croydon import ctx
from .camden_pb2_grpc import CamdenStub


def get_new_stub() -> CamdenStub:
    chan = grpc.aio.insecure_channel(ctx.cfg.grpc.socket)
    return CamdenStub(chan)

