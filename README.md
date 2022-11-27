# Fee Calculator

Fee Calculator is a microservice that calculates the fee that must be charged to the user for transporting a package with dPost.

This project contains several implementations of this service. Each implementation is written in Python, but uses different libraries. The used protocol is RCP and the chosen implementations are gRPC and JSON-RPC.

Every subproject contains documentation on how to setup and use the service.

## Implementations

- JSON-RPC
    - json-rpc
    - Flask-JSONRPC
- gRPC
    - grpcio
    - mask
    - python-grpc
