from typing import Tuple
from http.client import HTTPSConnection, HTTPConnection
from urllib.parse import urlparse
import ssl

def get(url: str, verify: bool = True, timeout: int = 0):
    parse_result = urlparse(url)
    scheme = parse_result.scheme
    host = parse_result.netloc
    tls_ctx = ssl.create_default_context()
    if not verify:
        tls_ctx.check_hostname = False
        tls_ctx.verify_mode = ssl.CERT_NONE

    if ':' in host:
        hostname, port = host.split(':')
    else:
        hostname = host
        port = 80 if scheme == "http" else 443

    if scheme == "https":
        conn = HTTPSConnection(hostname, port, context=tls_ctx)
    elif scheme == "http":
        conn = HTTPConnection(hostname, port)
    else:
        raise ValueError("URL is not supported")

    conn.request("GET", parse_result.path)
    return conn.getresponse()
