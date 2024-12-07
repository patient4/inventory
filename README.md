# E-commerce Inventory Microservice

## **Overview**
This repository contains the code for a microservice that manages the inventory of an e-commerce application. The Inventory Microservice provides RESTful APIs to perform CRUD operations on product data, including adding new products, fetching product details, updating product information, and deleting products.

---

## **Features**
- Add new products to the inventory.
- Fetch all products or a specific product by ID.
- Update product details.
- Delete products from the inventory.

---

## **Technology Stack**
- **Programming Language:** Python (Flask/FastAPI) or Node.js (Express.js)
- **Database:** PostgreSQL or MongoDB
- **Containerization:** Docker
- **Hosting:** AWS / GCP / Azure / DigitalOcean

---

## **Setup and Installation**

### Prerequisites
- Docker installed on your system
- Python 3.9+ or Node.js 16+ installed
- PostgreSQL or MongoDB database setup
- Git installed

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   - **Python**
     ```bash
     pip install -r requirements.txt
     ```
   - **Node.js**
     ```bash
     npm install
     ```

3. Configure the environment variables:
   - Copy the `.env.example` file and rename it to `.env`.
   - Update the database connection string and other configuration variables.

4. Run the application locally:
   - **Python**
     ```bash
     python app.py
     ```
   - **Node.js**
     ```bash
     npm start
     ```

5. Access the application at `http://localhost:5000`.

---

## **API Endpoints**

### **Product Management**
- **POST /products** - Add a new product
- **GET /products** - Fetch all products
- **GET /products/{id}** - Fetch product by ID
- **PUT /products/{id}** - Update product by ID
- **DELETE /products/{id}** - Delete product by ID

### **Sample Request/Response**
#### POST /products
**Request:**
```json
{
  "name": "Laptop",
  "description": "High-performance laptop",
  "price": 1200.50,
  "stock": 10
}
```
**Response:**
```json
{
  "id": 1,
  "name": "Laptop",
  "description": "High-performance laptop",
  "price": 1200.50,
  "stock": 10
}
```

---

## **Containerization**

### Build Docker Image
```bash
docker build -t inventory-microservice .
```

### Run Docker Container
```bash
docker run -d -p 5000:5000 --env-file .env inventory-microservice
```

### Using Docker Compose
1. Ensure `docker-compose.yml` is properly configured.
2. Run the following command:
   ```bash
   docker-compose up
   ```

---

## **Deployment**

1. Push the Docker image to a registry:
   ```bash
   docker tag inventory-microservice <registry-url>/inventory-microservice
   docker push <registry-url>/inventory-microservice
   ```

2. Deploy to your cloud provider (AWS/GCP/Azure):
   - Set up a virtual machine or container orchestration platform (e.g., Kubernetes).
   - Pull and run the Docker image.

---

## **Testing**
- Use Postman or Curl to test the API endpoints.
- Run unit tests:
  ```bash
  pytest  # For Python
  npm test  # For Node.js
  ```

---

## **Documentation**
- Swagger UI is available at `/docs` if enabled.
- Alternatively, API documentation is available in the `docs` folder of this repository.

---

## **Contributing**
- Fork the repository.
- Create a new branch (`feature-branch`).
- Commit your changes.
- Submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---

## **Contact**
For any issues or feature requests, please raise an issue in this repository.
