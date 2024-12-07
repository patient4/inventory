from concurrent import futures
import inventory_service_pb2
import inventory_service_pb2_grpc
import grpc

from Model.model_manager import grpc_to_dataclass, convert_products_to_grpc_products, dataclass_to_grpc_obj
from db.curd_operation import Database
from Model.Product import Product


class InventoryService(inventory_service_pb2_grpc.InventoryServiceServicer):

    def __init__(self):
        self.db = Database()

    def GetProduct(self, request, context):
        success, message = self.db.get(model=Product, id=request.id)
        response = dataclass_to_grpc_obj(message)
        return response

    def AddProduct(self, request, context):
        product = grpc_to_dataclass(request)
        success, message = self.db.add(product)
        return inventory_service_pb2.ProductResponse(msg=message, success=success)


    def DeleteProduct(self, request, context):
        success, message = self.db.delete(Product, request.id)
        return inventory_service_pb2.ProductResponse(msg=message, success=success)

    def GetAllProducts(self, request, context):
        success, records = self.db.get_all(Product)
        if success:
            product_list = convert_products_to_grpc_products(records)
            return product_list
        else:
            return inventory_service_pb2.ProductList()

    def UpdateProduct(self, request, context):
        product = grpc_to_dataclass(request)
        updated_object = {"name": product.name, "description": product.description,"stock":product.stock,
                          "price":product.price}
        try:
            success, message = self.db.update(model=Product, id=request.id, **updated_object)
            return inventory_service_pb2.ProductResponse(msg=message, success=success)
        except Exception as e:
            print(e)




def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_service_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:5001')
    print("server is up at PORT 5001.")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()