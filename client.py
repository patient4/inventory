import grpc

import inventory_service_pb2
import inventory_service_pb2_grpc
from Model.Product import Product
from Model.model_manager import dataclass_to_grpc_obj

channel = grpc.insecure_channel('localhost:5001')
stub = inventory_service_pb2_grpc.InventoryServiceStub(channel)

product = Product(id=1, name="Fair and lovely", description='good cream', stock=10, price=100)
response = stub.AddProduct(dataclass_to_grpc_obj(product))
print(product, response)