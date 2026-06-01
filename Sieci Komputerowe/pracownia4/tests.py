import requests
import socket
import subprocess


def print_result(ok, msg):
    if ok:
        print(f"{msg} \033[92mOK\033[0m")
    else:
        print(f"{msg} \033[91mFAILED\033[0m")


def test_redirect():
    try:
        r = requests.get("http://virbian:8888/", allow_redirects=False, timeout=3)
        if r.status_code == 301 and r.headers.get("Location") == "/index.html":
            r2 = requests.get("http://virbian:8888/index.html", timeout=3)
            return print_result("3" in r2.text, "Redirect to /index.html and content check")
    except:
        pass
    return print_result(False, "Redirect to /index.html")


def test_subpage():
    try:
        r = requests.get("http://virbian:8888/page.html", timeout=3)
        return print_result("html" in r.text.lower(), "Subpage page.html loads")
    except:
        return print_result(False, "Subpage page.html")


def test_files():
    try:
        files = {
            "plik.txt": "text/plain",
            "kupony.pdf": "application/pdf",
            "file.bin": "application/octet-stream"
        }
        for name, mime in files.items():
            r = requests.get(f"http://virbian:8888/{name}", timeout=3)
            if mime not in r.headers.get("Content-Type", ""):
                return print_result(False, f"{name} wrong content type")
        return print_result(True, "All files served correctly")
    except:
        return print_result(False, "File serving")


def test_virtual_page():
    try:
        r = requests.get("http://virtual-domain.example.com:8888/page.html", headers={"Host": "virtual-domain.example.com"}, timeout=3)
        return print_result("html" in r.text.lower(), "Virtual domain page.html")
    except:
        return print_result(False, "Virtual domain page.html")


def test_virtual_redirect():
    try:
        r = requests.get("http://virtual-domain.example.com:8888/", allow_redirects=False, timeout=3)
        if r.status_code == 301 and "index.html" in r.headers.get("Location", ""):
            r2 = requests.get("http://virtual-domain.example.com:8888/index.html", timeout=3)
            return print_result(r2.status_code == 404, "Virtual domain 301 -> 404")
    except:
        pass
    return print_result(False, "Virtual domain redirect to 404")


def test_path_traversal():
    try:
        result = subprocess.run([
            "curl", "-v", "--path-as-is",
            "http://virtual-domain.example.com:8888/../virbian/index.html"
        ], capture_output=True, text=True)
        blocked = "403" in result.stdout or "400" in result.stdout or "not allowed" in result.stdout.lower()
        return print_result(blocked, "Path traversal blocked")
    except:
        return print_result(False, "Path traversal")


def test_telnet_501():
    try:
        s = socket.create_connection(("virbian", 8888), timeout=3)
        s.sendall(b"abcdef\nqwerty\n\n")
        data = s.recv(1024).decode()
        s.close()
        if "501" in data:
            r = requests.get("http://virbian:8888/", timeout=3)
            return print_result(True, "501 error handled, server still responds")
    except:
        pass
    return print_result(False, "Telnet 501 test")


if __name__ == "__main__":
    # test_redirect()
    # test_subpage()
    # test_files()
    # test_virtual_page()
    # test_virtual_redirect()
    # test_path_traversal()
    test_telnet_501()
