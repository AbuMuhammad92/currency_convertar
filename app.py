from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
API_KEY = "1nYFGotMD2gDGjxrSkIInonCpdnwPCWU"


@app.route('/api/rates', methods=['GET'])
def get_exchange_rates():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = request.args.get('value')

    response = requests.get(
        API_URL.format(to_currency=to_currency, from_currency=from_currency, amount=amount),
        headers={"apikey": API_KEY}
    )

    if response.status_code == 200:
        data = response.json()
        return jsonify({"result": data['result']})
    else:
        return jsonify({"error": "Unable to fetch rates"}), 500


if __name__ == '__main__':
    app.run(debug=True)
