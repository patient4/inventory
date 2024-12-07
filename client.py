from http.client import responses

import grpc

import inventory_service_pb2
import inventory_service_pb2_grpc
from Model.Product import Product
from Model.model_manager import dataclass_to_grpc_obj

channel = grpc.insecure_channel('localhost:5001')
stub = inventory_service_pb2_grpc.InventoryServiceStub(channel)
product_data = [
    {
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
     },
    {
        "id": 3,
        "name":"Vasmol",
        "description":"Surakshit kale mere baal vasmol ne kiya kamaal",
        "stock": 10,
        "price": 110
    }
]

product = Product(**product_data[3])
print(product)
#add product logic

# request = dataclass_to_grpc_obj(product)
# response = stub.AddProduct(request)
# print(response)

## delete product logic
# id = 1
# request = inventory_service_pb2.ProductRequest(id=id)
# response = stub.DeleteProduct(request)
# print(response)

# update product logic
# id = 1
# product_update = {
#     "id": "2",
#     "name": "Tata Tea",
#     "description": "waah TAJ!",
#     "stock": 10,
#     "price": 100
# }
#
# product = Product(**product_update)
# request = dataclass_to_grpc_obj(product)
# response = stub.UpdateProduct(request)
# print(response)

# # get product with id=3
# id = 3
# request = inventory_service_pb2.ProductRequest(id=id)
# response = stub.GetProduct(request)
# print(response)

# # get all product from the entity products
# request = inventory_service_pb2.Empty()
# response = stub.GetAllProducts(request)
# print(response)

