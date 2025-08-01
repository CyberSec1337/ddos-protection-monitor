# ddos-protection-monitor
🛡️ DDoS Protection & Traffic Monitor Dashboard

A comprehensive real-time network traffic monitoring and DDoS protection system built with Flask. This application provides advanced traffic analysis, IP geolocation tracking, and automated threat detection capabilities.

https://github.com/user-attachments/assets/cc619dc7-9171-47fe-9e66-50733c54e6db

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v3.1.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 🌟 Features

### 🔍 Real-time Traffic Monitoring
- **Live Traffic Analysis**: Monitor incoming network requests in real-time
- **Interactive Dashboard**: Beautiful web-based interface with charts and statistics
- **Traffic Logging**: Persistent storage of all traffic data in JSON format

### 🌍 IP Geolocation & Analysis
- **Geographic Tracking**: Automatic IP geolocation using IPInfo.io API
- **Location Mapping**: Display visitor locations with city, region, and country data
- **Caching System**: Efficient TTL-based caching for improved performance

### 🚫 DDoS Protection
- **IP Blacklisting**: Configurable blacklist for blocking malicious IPs
- **Automated Blocking**: Real-time threat detection and blocking
- **Status Tracking**: Monitor allowed vs blocked requests

### 📊 Network Packet Capture
- **Deep Packet Inspection**: Integration with tcpdump for network analysis
- **Raw Traffic Data**: Capture and analyze network packets
- **Security Monitoring**: Advanced network security features

### 🎨 Modern Web Interface
- **Responsive Design**: Bootstrap-powered responsive UI
- **Interactive Charts**: Real-time data visualization with Chart.js
- **Alert System**: SweetAlert2 integration for user notifications
- **Dark/Light Theme**: Modern and professional interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Linux/Unix system (for tcpdump functionality)
- sudo privileges (for packet capture features)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ddos-protection-monitor.git
   cd ddos-protection-monitor
   ```

2. **Install dependencies**
   ```bash
   pip install flask requests cachetools
   ```

3. **Set up environment variables** (Optional)
   ```bash
   export IPINFO_TOKEN="your_ipinfo_token_here"
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the dashboard**
   Open your browser and navigate to `http://localhost:5000`

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `IPINFO_TOKEN` | IPInfo.io API token for geolocation | `default_token` |

### Application Settings

Edit the configuration variables in `app.py`:

```python
# Blacklist Configuration
BLACKLIST_IPS = ["192.168.1.100", "10.0.0.1"]

# Logging Configuration
LOG_FILE = "traffic_log.json"

# Cache Configuration
geo_cache = TTLCache(maxsize=100, ttl=3600)  # 1 hour TTL
```

## 📡 API Endpoints

### Traffic Monitoring
- **POST** `/monitor` - Log and analyze incoming traffic
- **GET** `/traffic` - Retrieve complete traffic log
- **GET** `/capture` - Capture network packets

### Dashboard
- **GET** `/` - Main dashboard interface

## 🏗️ Project Structure

```
ddos-protection-monitor/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Dashboard HTML template
├── static/
│   ├── styles.css        # Custom CSS styles
│   ├── charts.js         # Chart visualization logic
│   └── logs.js           # Log management functions
├── traffic_log.json      # Traffic data storage
├── app.log              # Application logs
└── README.md            # Project documentation
```

## 🛠️ Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5.3
- **Charts**: Chart.js
- **Alerts**: SweetAlert2
- **Network Analysis**: tcpdump
- **Caching**: cachetools
- **HTTP Requests**: requests library

## 📈 Usage Examples

### Monitor Traffic
```bash
curl -X POST http://localhost:5000/monitor
```

### Get Traffic Logs
```bash
curl http://localhost:5000/traffic
```

### Capture Network Packets
```bash
curl http://localhost:5000/capture
```

## 🔒 Security Features

- **IP Blacklisting**: Automatic blocking of malicious IPs
- **Request Logging**: Comprehensive logging of all requests
- **Geolocation Tracking**: Monitor request origins
- **Real-time Monitoring**: Live threat detection
- **Packet Analysis**: Deep network inspection capabilities

## 🎯 Use Cases

- **Network Security Monitoring**: Monitor and analyze network traffic
- **DDoS Attack Prevention**: Detect and block malicious traffic
- **Web Application Protection**: Protect web services from attacks
- **Traffic Analysis**: Analyze visitor patterns and behavior
- **Security Research**: Study network security patterns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **IPInfo.io** for geolocation services
- **Bootstrap** for responsive UI components
- **Chart.js** for data visualization
- **Flask** community for the excellent framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/ddos-protection-monitor/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

## 🔮 Future Enhancements

- [ ] Machine Learning-based threat detection
- [ ] Advanced analytics and reporting
- [ ] Multi-language support
- [ ] Docker containerization
- [ ] Database integration (PostgreSQL/MySQL)
- [ ] Real-time notifications (Email/SMS)
- [ ] API rate limiting
- [ ] Advanced filtering and search

---

⭐ **Star this repository if you find it helpful!**

Made with ❤️ for network security and monitoring
