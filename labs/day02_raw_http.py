#!/usr/bin/env python3
"""
Day 2 Lab: Raw Socket HTTP Engine
Direct byte-level interaction with HTTP/1.1 to analyze protocol structure,
CRLF delimiters, status codes, and header mechanisms.
"""
import socket

def send_raw_http(host: str, port: int, raw_payload: str) -> tuple[str, str, str]:
    """
    Opens a raw TCP socket, pushes bytes down the wire, and separates
    the HTTP response into (Status Line, Headers, Body).
    """
    # 1. Establish low-level TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5.0)
    
    try:
        client.connect((host, port))
        # 2. Transmit raw ASCII bytes
        client.sendall(raw_payload.encode("utf-8"))
        
        # 3. Read response until socket closes
        response_bytes = b""
        while True:
            chunk = client.recv(4096)
            if not chunk:
                break
            response_bytes += chunk
    finally:
        client.close()

    raw_response = response_bytes.decode("utf-8", errors="replace")

    # 4. Protocol parsing: Split headers and body using the double CRLF boundary
    if "\r\n\r\n" in raw_response:
        header_section, body = raw_response.split("\r\n\r\n", 1)
    elif "\n\n" in raw_response: # Fallback for non-compliant servers
        header_section, body = raw_response.split("\n\n", 1)
    else:
        header_section, body = raw_response, ""

    # Split status line from the rest of the headers
    header_lines = header_section.split("\r\n")
    status_line = header_lines[0]
    headers = "\r\n".join(header_lines[1:])

    return status_line, headers, body


def run_protocol_experiments():
    target_host = "127.0.0.1"
    target_port = 3000

    print("=" * 65)
    print("DAY 2 LAB: RAW SOCKET HTTP PROTOCOL EXPERIMENTS")
    print("=" * 65)

    # EXPERIMENT 1: Valid, well-formed HTTP/1.1 GET Request
    # Notice the explicit \r\n after every header and the final \r\n\r\n
    valid_request = (
        "GET /rest/admin/application-version HTTP/1.1\r\n"
        "Host: localhost:3000\r\n"
        "User-Agent: RawSocketClient/1.0\r\n"
        "Accept: application/json\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    print("\n[Experiment 1] Transmitting Well-Formed HTTP/1.1 Request...")
    status, headers, body = send_raw_http(target_host, target_port, valid_request)
    print(f"--> Status Line: {status}")
    print(f"--> Headers Sample:\n{headers[:250]}...\n")
    print(f"--> Body Output: {body.strip()}")

    # EXPERIMENT 2: Protocol Violation (HTTP/1.1 without mandatory Host header)
    # RFC 9112 Section 7.2 requires HTTP/1.1 requests to include a Host header.
    invalid_request = (
        "GET /rest/admin/application-version HTTP/1.1\r\n"
        "User-Agent: HostlessAttacker/1.0\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    print("\n" + "-" * 65)
    print("[Experiment 2] Transmitting Protocol Violation (Missing Host Header)...")
    status, headers, body = send_raw_http(target_host, target_port, invalid_request)
    print(f"--> Status Line: {status}")
    print(f"--> Body Output: {body.strip()}")

    # EXPERIMENT 3: Inspecting Cookie Security Flags
    # Requesting a resource that sets session state
    cookie_request = (
        "GET /rest/user/authentication-details HTTP/1.1\r\n"
        "Host: localhost:3000\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    print("\n" + "-" * 65)
    print("[Experiment 3] Inspecting Server Security Headers & Set-Cookie...")
    status, headers, body = send_raw_http(target_host, target_port, cookie_request)
    print(f"--> Status Line: {status}")
    
    # Filter for security-relevant headers
    print("--> Security Headers Observed:")
    for line in headers.split("\r\n"):
        header_lower = line.lower()
        if any(h in header_lower for h in ["cookie", "x-", "content-security-policy", "access-control"]):
            print(f"    {line}")

    print("\n" + "=" * 65)
    print("EXPERIMENTS COMPLETE: PROTOCOL MECHANICS VERIFIED OVER RAW TCP")
    print("=" * 65)


if __name__ == "__main__":
    run_protocol_experiments()
