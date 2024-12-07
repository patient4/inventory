from concurrent import futures
import inventory_service_pb2
import inventory_service_pb2_grpc
import grpc

from Model.model_manager import grpc_to_dataclass


class InventoryService(inventory_service_pb2_grpc.InventoryServiceServicer):

    def __init__(self):
        self.products = []

    def GetProduct(self, request, context):
        pass


    def AddProduct(self, request, context):
        print(request)
        product = grpc_to_dataclass(request)
        self.products.append(product)
        return inventory_service_pb2.ProductResponse(msg="added products", success=True)


    def RemoveFromInventory(self, request, context):
        pass

    def GetAllProducts(self, request, context):
        pass

    def UpdateAllProducts(self, request, context):
        pass

    def DeleteProduct(self, request, context):
        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_service_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:5001')
    print("server is up at PORT 5001.")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()