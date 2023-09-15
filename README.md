Currency Converter API

Base URL: http://127.0.0.1:5001

How to Run using Docker:
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
docker run -p 5001:5000 currency-converter:latest
After this, the application should be accessible at http://127.0.0.1:5001.

Exchange Rate Endpoint:
Endpoint: /api/rates
Method: GET
Parameters:

from: Source currency (e.g., "USD").
to: Target currency (e.g., "RUB").
value: Amount of currency to convert (e.g., "1").
Example Request:

vbnet
Copy code
GET /api/rates?from=USD&to=RUB&value=1
Example Response:

json
Copy code
{
    "result": 96.530036
}
