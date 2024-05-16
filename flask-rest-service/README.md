# Flask REST Service

This is a simple RESTful web service built with Flask, inspired by the Spring Boot guide.

## Getting Started

These instructions will help you set up and run the Flask REST service on your local machine.

### Prerequisites

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### Installing

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/flask-rest-service.git
    cd flask-rest-service
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Flask application:**

    ```sh
    python run.py
    ```

2. **Access the service:**

    Open your web browser and go to [http://localhost:8080/greeting](http://localhost:8080/greeting).

### API Endpoints

- **GET /greeting**

  Returns a greeting message. You can customize the greeting with a `name` query parameter.

  **Example Requests:**

  - `GET /greeting` returns `{"id": 1, "content": "Hello, World!"}`
  - `GET 
