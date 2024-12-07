from Model.Product import Product
import inventory_service_pb2

def grpc_to_dataclass(grpc_obj):
    return Product(id=grpc_obj.id, name=grpc_obj.name, price=grpc_obj.price,
                   description=grpc_obj.description, stock=grpc_obj.stock)

def dataclass_to_grpc_obj(data):
    return inventory_service_pb2.Product(id=data.id, name=data.name, price=data.price,
                                         description=data.description,stock=data.stock)