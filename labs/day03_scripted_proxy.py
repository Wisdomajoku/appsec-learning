#!/usr/bin/env python3
"""
Day 3 Lab: Programmatic HTTP Automation via Burp Proxy
Demonstrating session management, query parameter encoding,
JSON body transmission, and upstream proxy routing.
"""
import requests
import urllib3

# Suppress InsecureRequestWarning when using verify=False in local labs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Upstream proxy configuration (Burp Suite default listener)
BURP_PROXY = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

BASE_URL = "http://127.0.0.1:3000"

def create_appsec_session() -> requests.Session:
    """
    Constructs a persistent HTTP session configured for security testing.
    """
    session = requests.Session()
    # Route all session traffic through Burp Suite
    session.proxies.update(BURP_PROXY)
    
    # Disable SSL verification for lab proxying (prevents self-signed cert crashes)
    session.verify = False
    
    # Establish realistic baseline headers
    session.headers.update({
        "User-Agent": "AppSecAutomationEngine/1.0",
        "Accept": "application/json, text/plain, */*"
    })
    return session


def run_automated_assessment(session: requests.Session):
    print("=" * 65)
    print("DAY 3 LAB: SCRIPTED HTTP AUTOMATION THROUGH BURP SUITE")
    print("=" * 65)

    # 1. GET Request with Query Parameters
    # Target: Product Search endpoint
    search_term = "apple"
    search_url = f"{BASE_URL}/rest/products/search"
    params = {"q": search_term}
    
    print(f"\n[Test 1] Dispatching GET Request to {search_url}?q={search_term}...")
    resp1 = session.get(search_url, params=params)
    print(f"--> Status Code: {resp1.status_code}")
    print(f"--> Response Headers (Server): {resp1.headers.get('Server', 'Unknown')}")
    print(f"--> Items Found: {len(resp1.json().get('data', []))}")

    # 2. GET Request fetching system configuration
    config_url = f"{BASE_URL}/rest/admin/application-configuration"
    print(f"\n[Test 2] Dispatching GET Request to {config_url}...")
    resp2 = session.get(config_url)
    print(f"--> Status Code: {resp2.status_code}")
    if resp2.status_code == 200:
        app_name = resp2.json().get("config", {}).get("application", {}).get("name")
        print(f"--> Discovered Application Name: {app_name}")

    # 3. POST Request transmitting JSON Payload
    # Target: User feedback submission
    feedback_url = f"{BASE_URL}/api/Feedbacks/"
    payload = {
        "UserId": 1,
        "comment": "Automated security test payload from Python.",
        "rating": 5
    }
    
    print(f"\n[Test 3] Dispatching POST Request with JSON Body to {feedback_url}...")
    resp3 = session.post(feedback_url, json=payload)
    print(f"--> Status Code: {resp3.status_code}")
    print(f"--> Response Body: {resp3.text[:120]}...")

    print("\n" + "=" * 65)
    print("AUTOMATION COMPLETE: CHECK BURP SUITE PROXY HTTP HISTORY")
    print("=" * 65)


if __name__ == "__main__":
    try:
        session = create_appsec_session()
        run_automated_assessment(session)
    except requests.exceptions.ProxyError:
        print("\n[!] FATAL ERROR: Could not connect to Burp Suite proxy on 127.0.0.1:8080.")
        print("[!] Ensure Burp Suite is running with its default proxy listener enabled.")
    except requests.exceptions.ConnectionError:
        print("\n[!] FATAL ERROR: Could not connect to Juice Shop on http://127.0.0.1:3000.")
        print("[!] Ensure Juice Shop container is running: 'docker start juiceshop'.")
