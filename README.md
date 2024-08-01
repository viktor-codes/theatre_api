# Theater API

The Theater API is a comprehensive platform designed to streamline the management and operation of a Theater or performing arts venue. It provides a wide range of functionalities to facilitate the administration of performances, ticket sales, audience engagement, and more.

---

## Running the API Locally

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/rurakite/Theater-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Theater-api
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running with Django's Built-in Development Server

1. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

2. (Optional) Load initial data (if provided):

   ```bash
   python manage.py loaddata Theater_api_data.json
   ```

3. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The API will be accessible at `http://127.0.0.1:8000/`.

### Running with Docker

1. Build the Docker image:

   ```bash
   docker-compose build -t Theater-api .
   ```

2. Run the Docker container:

   ```bash
   docker-compose up run
   ```

   The API will be accessible at `http://0.0.0.0:8000/`.

### Testing the API

You can now test the API by sending requests to the endpoints using tools like cURL, Postman, or your preferred HTTP client.

### Shutting Down

To stop the development server or Docker container, press `Ctrl + C` in the terminal where it's running.

If using Docker, you can stop and remove the container:

```bash
docker stop <container_id>
docker rm <container_id>
```

### Key Features:

1. **Performance Management**: Effortlessly create, update, and schedule performances, complete with showtimes, venue details, cast, and crew information.

2. **Ticketing System**: Seamlessly manage ticket sales, reservations, and seat assignments, with support for various ticket types and pricing options tailored to your audience's needs.

3. **User Authentication with JWT**: Secure user authentication using JSON Web Tokens (JWT), ensuring seamless access control and authentication for API endpoints. Users can obtain JWT tokens by providing valid credentials, which are then used to authenticate subsequent API requests.

4. **API Documentation**: Provide detailed documentation for developers, including information on endpoints, authentication methods, request and response formats. Available at  `/api/doc/swagger/`

### Using JWT for User Authentication:

To authenticate users and obtain JWT tokens for accessing protected API endpoints, follow these steps:

1. **Register a User**: If you haven't already, register a user account using the API endpoint `/api/user/register/`. Provide the required user details, such as username, email, and password.

2. **Obtain JWT Token**: Authenticate the user by sending a POST request to the `/api/user/token/` endpoint with their credentials (username and password). Upon successful authentication, the API will respond with a JWT token in the JSON format.

3. **Include JWT Token**: Include the obtained JWT token in the `Authorization` header of subsequent API requests to access protected endpoints. Set the header value as `Bearer <JWT_token>`.

4. **Access Protected Endpoints**: With the JWT token included in the request headers, you can now access protected API endpoints requiring authentication.

