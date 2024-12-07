from Model.Product import Product
import inventory_service_pb2

def grpc_to_dataclass(grpc_obj):
    return Product(id=int(grpc_obj.id), name=grpc_obj.name, price=grpc_obj.price,
                   description=grpc_obj.description, stock=grpc_obj.stock)

def dataclass_to_grpc_obj(data):
    return inventory_service_pb2.Product(id=int(data.id), name=data.name, price=data.price,
                                         description=data.description,stock=data.stock)

def convert_products_to_grpc_products(records):
    products = inventory_service_pb2.ProductList()
    for record in records:
        print(f"Converting record with id: {record.id} and price: {record.price} (type: {type(record.price)})")
        grpc_product = dataclass_to_grpc_obj(record)
        products.products.append(grpc_product)
        print(products)
    return products