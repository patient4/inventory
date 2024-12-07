from http.client import responses

import grpc

import inventory_service_pb2
import inventory_service_pb2_grpc
from Model.Product import Product
from Model.model_manager import dataclass_to_grpc_obj

channel = grpc.insecure_channel('localhost:5001')
stub = inventory_service_pb2_grpc.InventoryServiceStub(channel)
product_data = [{
    "id": 1,
    "name": "Fair and lovely",
    "description": "Good cream",
    "stock": 10,
    "price": 100
},
    {"id":2,
     "name":"Fair and Handsome",
     "description":"mard ko banae gora",
     "stock": 10,
     "price": 100
     },
{"id":2,
     "name":"Fena",
     "description":"mard ko banae kala",
     "stock": 10,
     "price": 100
     }
]

# product = Product(**product_data[2])
# print(product)
# productRequest = dataclass_to_grpc_obj(product)
# print(productRequest)
# response = stub.UpdateProduct(productRequest)
# response = stub.AddProduct(dataclass_to_grpc_obj(product))
# id = 1
# request = inventory_service_pb2.ProductRequest(id=id)
# response = stub.DeleteProduct(request)
# request = inventory_service_pb2.Empty()
# response = stub.GetAllProducts(request)
id = 2
request = inventory_service_pb2.ProductRequest(id=id)
response = stub.GetProduct(request)
print(response)
