from flask import Flask, render_template, jsonify
import requests
import json
import threading
import time
from datetime import datetime

app = Flask(__name__)

MONERO_NODE_HOST = "localhost"
MONERO_NODE_PORT = 18081

class MoneroNodeClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.base_url = f"http://{host}:{port}"
        self.cached_data = {}
        self.last_update = {}
    
    def make_rpc_call(self, method, params=None):
        try:
            payload = {
                "jsonrpc": "2.0",
                "id": "0",
                "method": method
            }
            if params:
                payload["params"] = params
            
            response = requests.post(
                f"{self.base_url}/json_rpc",
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                if "result" in result:
                    return result["result"]
            return None
        except Exception as e:
            print(f"Error calling {method}: {e}")
            return None
    
    def get_info(self):
        return self.make_rpc_call("get_info")
    
    def get_block_count(self):
        return self.make_rpc_call("get_block_count")
    
    def get_connections(self):
        return self.make_rpc_call("get_connections")
    
    def get_block_header(self, height=None):
        params = {}
        if height is not None:
            params["height"] = height
        return self.make_rpc_call("get_block_header_by_height", params)
    
    def get_last_block_header(self):
        return self.make_rpc_call("get_last_block_header")
    
    def get_fee_estimate(self):
        return self.make_rpc_call("get_fee_estimate")

monero_client = MoneroNodeClient(MONERO_NODE_HOST, MONERO_NODE_PORT)

def update_data_background():
    while True:
        try:
            # Update node info every 30 seconds
            if time.time() - monero_client.last_update.get('info', 0) > 30:
                info = monero_client.get_info()
                if info:
                    monero_client.cached_data['info'] = info
                    monero_client.last_update['info'] = time.time()
            
            # Update block info every 10 seconds
            if time.time() - monero_client.last_update.get('block', 0) > 10:
                last_block = monero_client.get_last_block_header()
                if last_block:
                    monero_client.cached_data['last_block'] = last_block
                    monero_client.last_update['block'] = time.time()
            
            # Update connections every 60 seconds
            if time.time() - monero_client.last_update.get('connections', 0) > 60:
                connections = monero_client.get_connections()
                if connections:
                    monero_client.cached_data['connections'] = connections
                    monero_client.last_update['connections'] = time.time()
            
            # Update fee estimate every 120 seconds
            if time.time() - monero_client.last_update.get('fees', 0) > 120:
                fees = monero_client.get_fee_estimate()
                if fees:
                    monero_client.cached_data['fees'] = fees
                    monero_client.last_update['fees'] = time.time()
            
        except Exception as e:
            print(f"Background update error: {e}")
        
        time.sleep(5)

# Start background data updates
update_thread = threading.Thread(target=update_data_background, daemon=True)
update_thread.start()

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/data')
def get_data():
    data = {
        'timestamp': datetime.now().isoformat(),
        'node_info': monero_client.cached_data.get('info', {}),
        'last_block': monero_client.cached_data.get('last_block', {}),
        'connections': monero_client.cached_data.get('connections', {}),
        'fees': monero_client.cached_data.get('fees', {}),
        'node_status': 'online' if monero_client.cached_data.get('info') else 'offline'
    }
    return jsonify(data)

@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'node_connected': bool(monero_client.cached_data.get('info')),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/block/<int:height>')
def get_block_by_height(height):
    try:
        block_data = monero_client.get_block_header(height)
        if block_data:
            return jsonify(block_data)
        else:
            return jsonify({'error': 'Block not found or node unavailable'}), 404
    except Exception as e:
        return jsonify({'error': f'Failed to fetch block: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8282, debug=True)