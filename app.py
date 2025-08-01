from flask import Flask, render_template, jsonify, request
import subprocess
from datetime import datetime
import requests
import json
from cachetools import TTLCache
import os
import logging

app = Flask(__name__)

# إعدادات المشروع
BLACKLIST_IPS = ["192.168.1.100", "10.0.0.1"]
IPINFO_TOKEN = os.getenv("IPINFO_TOKEN", "default_token")  # مفتاح API لـ ipinfo.io
LOG_FILE = "traffic_log.json"  # اسم الملف لحفظ السجلات
geo_cache = TTLCache(maxsize=100, ttl=3600)  # تخزين بيانات IP لمدة ساعة واحدة

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Application started")

# تحميل السجلات من الملف عند بدء التشغيل
def load_traffic_log():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as file:
            json.dump([], file)  # إنشاء ملف فارغ إذا لم يكن موجودًا
    try:
        with open(LOG_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logging.error("Error loading traffic log. Starting with an empty log.")
        return []  # إذا لم يكن الملف موجودًا أو حدث خطأ في التحميل، يعيد قائمة فارغة

# حفظ السجلات في الملف
def save_traffic_log(log_data):
    try:
        with open(LOG_FILE, "w") as file:
            json.dump(log_data, file, indent=4)
        logging.info("Log saved successfully.")
    except Exception as e:
        logging.error(f"Error saving log to file: {e}")

# تحميل السجلات عند بدء التشغيل
traffic_log = load_traffic_log()

# وظيفة لجلب الموقع الجغرافي لعناوين IP
def get_geo_info(ip):
    if ip in geo_cache:  # تحقق إذا كان IP موجودًا في الكاش
        return geo_cache[ip]

    try:
        response = requests.get(f"https://ipinfo.io/{ip}?token={IPINFO_TOKEN}")
        if response.status_code == 200:
            geo_data = response.json()
            geo_cache[ip] = {
                "city": geo_data.get("city", "Unknown"),
                "region": geo_data.get("region", "Unknown"),
                "country": geo_data.get("country", "Unknown"),
            }
            return geo_cache[ip]
        else:
            logging.error(f"Failed to fetch geo info for {ip}: {response.status_code}")
            return {"city": "Unknown", "region": "Unknown", "country": "Unknown"}
    except Exception as e:
        logging.error(f"Error fetching geo info for {ip}: {e}")
        return {"city": "Unknown", "region": "Unknown", "country": "Unknown"}

# وظيفة لالتقاط حزم الشبكة باستخدام tcpdump
def capture_traffic():
    try:
        process = subprocess.Popen(
            ["sudo", "tcpdump", "-n", "-c", "10"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        if stderr:
            logging.error(f"Error: {stderr.decode()}")
        return stdout.decode().splitlines()
    except Exception as e:
        logging.error(f"Error in capture_traffic: {str(e)}")
        return []

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html', traffic=traffic_log)

# API لرصد الطلبات
@app.route('/monitor', methods=['POST'])
def monitor_traffic():
    ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # التحقق إذا كان IP ضمن القائمة السوداء
    status = "Blocked" if ip_address in BLACKLIST_IPS else "Allowed"
    
    # جلب بيانات الموقع الجغرافي
    geo_info = get_geo_info(ip_address)
    
    # تسجيل الطلب
    log = {
        "ip": ip_address,
        "timestamp": timestamp,
        "status": status,
        "geo_info": geo_info
    }
    traffic_log.append(log)  # إضافة السجل إلى القائمة
    save_traffic_log(traffic_log)  # تحديث الملف
    
    return jsonify(log)

# API للتقاط الحزم
@app.route('/capture')
def capture():
    captured_data = capture_traffic()
    return jsonify({"captured_traffic": captured_data})

# API لعرض السجل بالكامل
@app.route('/traffic')
def get_traffic_log():
    return jsonify({"traffic_log": traffic_log})

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

