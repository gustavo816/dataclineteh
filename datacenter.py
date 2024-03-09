from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

financial_data = {
    'net_profit': '5.000',
    'balance': '30.000'
}

client_notifications = []


@app.route('/financial-data', methods=['GET'])
def get_financial_data():
    print(f'Executado em: {datetime.datetime.now()}')
    return jsonify(financial_data)


@app.route('/update-financial-data/<net_profit>/<balance>', methods=['GET'])
def update_financial_data(net_profit, balance):
    print(f'Executado em: {datetime.datetime.now()}')
    financial_data['net_profit'] = net_profit
    financial_data['balance'] = balance
    return jsonify(financial_data)


@app.route('/notify-execution', methods=['GET'])
def notify_execution():
    print(f'Executado em: {datetime.datetime.now()}')
    client_id = request.args.get('client_id', 'Unknown client')
    timestamp = datetime.datetime.now()
    client_notifications.append((client_id, timestamp))
    return jsonify({'message': f'Received notification from {client_id} at {timestamp}'})


@app.route('/client-notifications', methods=['GET'])
def get_client_notifications():
    print(f'Executado em: {datetime.datetime.now()}')
    return jsonify(client_notifications)


if __name__ == '__main__':
    app.run(port=5000)
