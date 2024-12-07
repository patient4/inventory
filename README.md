# Inventory Management gRPC Service

## **Overview**
This repository contains a Python-based gRPC service for managing an inventory system. The gRPC service allows CRUD operations on product data, including adding, retrieving, updating, and deleting products. This is implemented using Python, gRPC, and Protocol Buffers.

---

## **Features**
- **Add Product:** Add new products to the inventory.
- **Get Product:** Retrieve product details by ID.
- **Get All Products:** Fetch the list of all products in the inventory.
- **Update Product:** Modify existing product details.
- **Delete Product:** Remove a product from the inventory.

---

## **Technology Stack**
- **Programming Language:** Python
- **Framework:** gRPC
- **Serialization:** Protocol Buffers (proto3)

---

## **Setup and Installation**

### **Prerequisites**
- Python 3.9 or higher
- `grpcio` and `grpcio-tools` libraries

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/patient4/inventory.git
   cd inventory
   ```

2. Install the required dependencies:
   ```bash
   pip install grpcio grpcio-tools
   ```

3. Compile the Protocol Buffers:
   ```bash
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. inventory_service.proto
   ```
   This generates `inventory_service_pb2.py` and `inventory_service_pb2_grpc.py` files.

4. Start the gRPC server:
   ```bash
   python server.py
   ```

5. (Optional) Run the client to test the service:
   ```bash
   python client.py
   ```

---

## **gRPC API Endpoints**

### **Service Definition**
The `InventoryService` is defined in the `inventory.proto` file. Below are the supported RPC methods:

1. **AddProduct**
   - **Request:** `Product`
   - **Response:** `Empty`

2. **GetProduct**
   - **Request:** `ProductRequest`
   - **Response:** `Product`

3. **GetAllProducts**
   - **Request:** `Empty`
   - **Response:** `ProductList`

4. **UpdateProduct**
   - **Request:** `Product`
   - **Response:** `Empty`

5. **DeleteProduct**
   - **Request:** `ProductRequest`
   - **Response:** `Empty`

### **Sample Request and Response**
#### Add Product:
**Request:**
```json
{
  "id": 1,
  "name": "Laptop",
  "description": "High-performance laptop",
  "price": 1200.50,
  "stock": 10
}
```
**Response:**
```json
{}
```

---

## **Project Structure**
```
.
├── inventory.proto        # Protocol Buffers file
├── inventory_pb2.py       # Generated Python classes for messages
├── inventory_pb2_grpc.py  # Generated gRPC service classes
├── server.py              # gRPC server implementation
├── client.py              # gRPC client implementation
├── README.md              # Project documentation
```

---

## **Testing**
- Use `client.py` to test the gRPC server functionality.
- Alternatively, use gRPC client tools like [BloomRPC](https://github.com/bloomrpc/bloomrpc) or [Postman](https://www.postman.com/) (with gRPC support).

---

## **Future Enhancements**
- Integrate with a persistent database (e.g., PostgreSQL or MongoDB).
- Add authentication and SSL/TLS for secure communication.
- Containerize the service using Docker.
- Implement advanced monitoring with Prometheus and Grafana.

---


