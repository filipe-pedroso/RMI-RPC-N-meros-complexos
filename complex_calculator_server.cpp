#include <iostream>
#include <memory>
#include <string>
#include <grpcpp/grpcpp.h>
#include "complex_calculator.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using complexcalculator::ComplexNumber;
using complexcalculator::ComplexResponse;
using complexcalculator::ComplexOperationRequest;
using complexcalculator::ComplexCalculator;

// Implementa a lógica do serviço
class ComplexCalculatorServiceImpl final : public ComplexCalculator::Service {
public:
    Status Calculate(ServerContext* context, const ComplexOperationRequest* request, ComplexResponse* response) override {
        ComplexNumber num1 = request->num1();
        ComplexNumber num2 = request->num2();
        std::string operation = request->operation();

        double real, imaginaria;

        if (operation == "add") {
            real = num1.real() + num2.real();
            imaginaria = num1.imaginaria() + num2.imaginaria();
        } else if (operation == "subtract") {
            real = num1.real() - num2.real();
            imaginaria = num1.imaginaria() - num2.imaginaria();
        } else if (operation == "multiply") {
            real = num1.real() * num2.real() - num1.imaginaria() * num2.imaginaria();
            imaginaria = num1.real() * num2.imaginaria() + num1.imaginaria() * num2.real();
        } else if (operation == "divide") {
            double denom = num2.real() * num2.real() + num2.imaginaria() * num2.imaginaria();
            real = (num1.real() * num2.real() + num1.imaginaria() * num2.imaginaria()) / denom;
            imaginaria = (num1.imaginaria() * num2.real() - num1.real() * num2.imaginaria()) / denom;
        } else {
            return Status(grpc::INVALID_ARGUMENT, "Operação inválida.");
        }

        ComplexNumber* result = response->mutable_result();
        result->set_real(real);
        result->set_imaginaria(imaginaria);

        return Status::OK;
    }
};

void RunServer() {
    std::string server_address("0.0.0.0:50051");
    ComplexCalculatorServiceImpl service;

    ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);

    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "Servidor ouvindo em " << server_address << std::endl;
    server->Wait();
}

int main(int argc, char** argv) {
    RunServer();
    return 0;
}
