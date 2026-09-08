import socket
import platform
import time
import psutil
import requests

API_URL = "http://127.0.0.1:8000/api/telemetry"

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def collect_system_metrics():
    return {
        "hostname": socket.gethostname(),
        "ip_address": get_ip(),
        "os_name": f"{platform.system()} {platform.release()}",
        "cpu_usage": psutil.cpu_percent(interval=1),
        "ram_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("/").percent
    }

def run_agent(interval_seconds=30):
    print(f"[*] AssetPulse Agent iniciado. Enviando dados para {API_URL} a cada {interval_seconds}s...")
    while True:
        try:
            payload = collect_system_metrics()
            response = requests.post(API_URL, json=payload, timeout=5)
            if response.status_code == 201:
                print(f"[+] [{time.strftime('%H:%M:%S')}] Telemetria enviada: CPU {payload['cpu_usage']}% | RAM {payload['ram_usage']}%")
            else:
                print(f"[-] Erro do servidor: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[!] Erro ao conectar a API: {e}")
        time.sleep(interval_seconds)

if __name__ == "__main__":
    run_agent(interval_seconds=30)