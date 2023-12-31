# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import app.proto.camden_pb2 as camden__pb2


class CamdenStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MapUpdates = channel.stream_stream(
                '/camden.Camden/MapUpdates',
                request_serializer=camden__pb2.MapUpdatesRequest.SerializeToString,
                response_deserializer=camden__pb2.Update.FromString,
                )
        self.GetAirport = channel.unary_unary(
                '/camden.Camden/GetAirport',
                request_serializer=camden__pb2.AirportRequest.SerializeToString,
                response_deserializer=camden__pb2.AirportResponse.FromString,
                )
        self.GetPilot = channel.unary_unary(
                '/camden.Camden/GetPilot',
                request_serializer=camden__pb2.PilotRequest.SerializeToString,
                response_deserializer=camden__pb2.PilotResponse.FromString,
                )
        self.ListPilots = channel.unary_unary(
                '/camden.Camden/ListPilots',
                request_serializer=camden__pb2.QueryRequest.SerializeToString,
                response_deserializer=camden__pb2.PilotListResponse.FromString,
                )
        self.CheckQuery = channel.unary_unary(
                '/camden.Camden/CheckQuery',
                request_serializer=camden__pb2.QueryRequest.SerializeToString,
                response_deserializer=camden__pb2.QueryResponse.FromString,
                )
        self.BuildInfo = channel.unary_unary(
                '/camden.Camden/BuildInfo',
                request_serializer=camden__pb2.NoParams.SerializeToString,
                response_deserializer=camden__pb2.BuildInfoResponse.FromString,
                )
        self.GetMetrics = channel.unary_unary(
                '/camden.Camden/GetMetrics',
                request_serializer=camden__pb2.NoParams.SerializeToString,
                response_deserializer=camden__pb2.MetricSet.FromString,
                )
        self.GetMetricsText = channel.unary_unary(
                '/camden.Camden/GetMetricsText',
                request_serializer=camden__pb2.NoParams.SerializeToString,
                response_deserializer=camden__pb2.MetricSetTextResponse.FromString,
                )
        self.SubscribeQuery = channel.stream_stream(
                '/camden.Camden/SubscribeQuery',
                request_serializer=camden__pb2.QuerySubscriptionRequest.SerializeToString,
                response_deserializer=camden__pb2.QuerySubscriptionUpdate.FromString,
                )


class CamdenServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MapUpdates(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAirport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPilot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPilots(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BuildInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMetrics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMetricsText(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeQuery(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CamdenServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MapUpdates': grpc.stream_stream_rpc_method_handler(
                    servicer.MapUpdates,
                    request_deserializer=camden__pb2.MapUpdatesRequest.FromString,
                    response_serializer=camden__pb2.Update.SerializeToString,
            ),
            'GetAirport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAirport,
                    request_deserializer=camden__pb2.AirportRequest.FromString,
                    response_serializer=camden__pb2.AirportResponse.SerializeToString,
            ),
            'GetPilot': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPilot,
                    request_deserializer=camden__pb2.PilotRequest.FromString,
                    response_serializer=camden__pb2.PilotResponse.SerializeToString,
            ),
            'ListPilots': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPilots,
                    request_deserializer=camden__pb2.QueryRequest.FromString,
                    response_serializer=camden__pb2.PilotListResponse.SerializeToString,
            ),
            'CheckQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckQuery,
                    request_deserializer=camden__pb2.QueryRequest.FromString,
                    response_serializer=camden__pb2.QueryResponse.SerializeToString,
            ),
            'BuildInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.BuildInfo,
                    request_deserializer=camden__pb2.NoParams.FromString,
                    response_serializer=camden__pb2.BuildInfoResponse.SerializeToString,
            ),
            'GetMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetrics,
                    request_deserializer=camden__pb2.NoParams.FromString,
                    response_serializer=camden__pb2.MetricSet.SerializeToString,
            ),
            'GetMetricsText': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetricsText,
                    request_deserializer=camden__pb2.NoParams.FromString,
                    response_serializer=camden__pb2.MetricSetTextResponse.SerializeToString,
            ),
            'SubscribeQuery': grpc.stream_stream_rpc_method_handler(
                    servicer.SubscribeQuery,
                    request_deserializer=camden__pb2.QuerySubscriptionRequest.FromString,
                    response_serializer=camden__pb2.QuerySubscriptionUpdate.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'camden.Camden', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Camden(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MapUpdates(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/camden.Camden/MapUpdates',
            camden__pb2.MapUpdatesRequest.SerializeToString,
            camden__pb2.Update.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAirport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/camden.Camden/GetAirport',
            camden__pb2.AirportRequest.SerializeToString,
            camden__pb2.AirportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPilot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/camden.Camden/GetPilot',
            camden__pb2.PilotRequest.SerializeToString,
            camden__pb2.PilotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPilots(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/camden.Camden/ListPilots',
            camden__pb2.QueryRequest.SerializeToString,
            camden__pb2.PilotListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/camden.Camden/CheckQuery',
            camden__pb2.QueryRequest.SerializeToString,
            camden__pb2.QueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BuildInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/camden.Camden/BuildInfo',
            camden__pb2.NoParams.SerializeToString,
            camden__pb2.BuildInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/camden.Camden/GetMetrics',
            camden__pb2.NoParams.SerializeToString,
            camden__pb2.MetricSet.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMetricsText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/camden.Camden/GetMetricsText',
            camden__pb2.NoParams.SerializeToString,
            camden__pb2.MetricSetTextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeQuery(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/camden.Camden/SubscribeQuery',
            camden__pb2.QuerySubscriptionRequest.SerializeToString,
            camden__pb2.QuerySubscriptionUpdate.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
