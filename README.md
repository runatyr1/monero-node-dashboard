# 🛸 Alien-Themed Monero Node Dashboard

A futuristic alien-themed web dashboard for real-time monitoring of Monero node data with spectacular space visuals.

## 🚀 Features

- **Alien Theme**: Futuristic design with extraterrestrial visual effects
- **Real-time Updates**: Data refreshes automatically every 10 seconds
- **Comprehensive Metrics**: Displays detailed Monero node information:
  - Synchronization status
  - Current block height
  - Active connections
  - Latest block information
  - Transaction fee estimates
  - Network hash rate
  - Database size

## 🌟 Visual Features

- **Deep Space Background**: Twinkling stars and colorful nebula clouds
- **Alien Eyes**: Subtle floating orbs with sparkly effects
- **Smooth Animations**: Gentle text glow cycles and card scanning effects
- **Responsive Design**: Works perfectly on mobile devices
- **Neon Color Scheme**: Green alien-tech aesthetic

## 📋 Requirements

- Python 3.7+
- Monero node running on `192.168.122.185:18081` (Docker container)
- SSH tunnel to VM with Monero node
- Python dependencies: Flask, requests

## 🛠 Installation & Setup

### 1. **Establish SSH tunnel to Monero node:**
```bash
# Connect with port tunnel from your local machine
ssh -L 18081:172.18.0.4:18081 user1@192.168.122.185
# Keep this connection active in a separate terminal
```

### 2. **Install dependencies (in another terminal):**
```bash
cd /path/to/monero-node-dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. **Run the dashboard:**
```bash
# Option 1: Using the script
./run.sh

# Option 2: Directly with Python
source venv/bin/activate
python app.py
```

### 4. **Access the dashboard:**
- Open web browser at: `http://localhost:8282`
- Or from another machine on network: `http://[SERVER_IP]:8282`

## 🌐 API Endpoints

- `GET /` - Main dashboard interface
- `GET /api/data` - JSON data from Monero node
- `GET /api/health` - Application health status

## ⚙️ Configuration

The Monero node must be configured for:
- Host: `192.168.122.185`
- Port: `18081` (standard port)
- RPC enabled

## 🔄 Update Frequencies

- **Node information**: Every 30 seconds
- **Block information**: Every 10 seconds
- **Connections**: Every 60 seconds
- **Fee estimates**: Every 120 seconds
- **Web dashboard**: Every 10 seconds
- **Star twinkling**: 8-12 seconds
- **Text glow**: 7 seconds

## 🎨 Animation Details

- **Background nebulae**: Subtle colorful clouds
- **Twinkling starfield**: Hundreds of stars with varied colors and sizes  
- **Alien eyes**: Floating sparkly orbs
- **Card scanning**: Left-to-right glow effects
- **Text pulsing**: Gentle 7-second glow cycles

## 🐛 Troubleshooting

### 1. **Node connection error**:
- Verify Monero node is running
- Check IP and port configuration
- Verify firewall settings

### 2. **Dependencies**:
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

### 3. **Port occupied**:
- Change port in `app.py` final line: `app.run(host='0.0.0.0', port=NEW_PORT)`

### 4. **SSH tunnel issues**:
- Verify tunnel is active: `netstat -tulpn | grep 18081`
- Check Docker container IP: `docker inspect btcpayserver_monerod`

## 📱 Browser Compatibility

- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile responsive design

## 🚀 Development

Built with:
- **Backend**: Python Flask
- **Frontend**: Pure HTML/CSS/JavaScript
- **Styling**: CSS3 animations and gradients
- **Data**: Monero RPC API integration

## 📸 Screenshots

The dashboard features:
- Real-time Monero metrics in alien-themed cards
- Deep space background with hundreds of twinkling stars
- Floating alien eyes with sparkly effects
- Smooth animations and responsive layout

---

*An alien technology dashboard for monitoring your Monero node* 👽🛸