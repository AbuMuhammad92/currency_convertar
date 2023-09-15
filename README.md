Currency Converter API Documentation

Base URL: http://127.0.0.1:5000

Setting Up using Docker
Clone the repository:
bash
Copy code
git clone [URL of your GitHub repository]
Navigate to the project directory:
bash
Copy code
cd currency_converter
Build the Docker image:
Copy code
docker build -t currency-converter:latest .
Run the Docker container:
arduino
Copy code
docker run -p 5000:5000 currency-converter:latest
Once the Docker container is up and running, the application should be accessible at http://127.0.0.1:5000.

Exchange Rate Endpoint
Path: /api/rates
Method: GET
Parameters:

from: Source currency (e.g., "USD").
to: Target currency (e.g., "RUB").
value: Amount of currency to convert (e.g., "1").
Example:

Copy code
GET /api/rates?from=USD&to=RUB&value=1
Response:

json
Copy code
{
    "result": 62.16
}
Possible Errors:

If the external currency conversion service is unavailable, the response might look like:

json
Copy code
{
    "error": "Unable to fetch rates"
}