import grpc
import complex_calculator_pb2
import complex_calculator_pb2_grpc

def run():
    # Conectar ao servidor
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = complex_calculator_pb2_grpc.ComplexCalculatorStub(channel)

        # Criação dos números complexos
        num1 = complex_calculator_pb2.ComplexNumber(real=1.0, imaginaria=2.0)
        num2 = complex_calculator_pb2.ComplexNumber(real=3.0, imaginaria=4.0)

        # Solicitar soma ao servidor
        request = complex_calculator_pb2.ComplexOperationRequest(num1=num1, num2=num2, operation="add")
        response = stub.Calculate(request)

        # Exibir o resultado
        print(f'Resultado: {response.result.real} + {response.result.imaginaria}i')

if __name__ == '__main__':
    run()
