# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import complex_calculator_pb2 as complex__calculator__pb2

GRPC_GENERATED_VERSION = '1.67.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in complex_calculator_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ComplexCalculatorStub(object):
    """Define o serviço da calculadora de números complexos
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Calculate = channel.unary_unary(
                '/complexcalculator.ComplexCalculator/Calculate',
                request_serializer=complex__calculator__pb2.ComplexOperationRequest.SerializeToString,
                response_deserializer=complex__calculator__pb2.ComplexResponse.FromString,
                _registered_method=True)


class ComplexCalculatorServicer(object):
    """Define o serviço da calculadora de números complexos
    """

    def Calculate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ComplexCalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Calculate': grpc.unary_unary_rpc_method_handler(
                    servicer.Calculate,
                    request_deserializer=complex__calculator__pb2.ComplexOperationRequest.FromString,
                    response_serializer=complex__calculator__pb2.ComplexResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'complexcalculator.ComplexCalculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('complexcalculator.ComplexCalculator', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ComplexCalculator(object):
    """Define o serviço da calculadora de números complexos
    """

    @staticmethod
    def Calculate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/complexcalculator.ComplexCalculator/Calculate',
            complex__calculator__pb2.ComplexOperationRequest.SerializeToString,
            complex__calculator__pb2.ComplexResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
