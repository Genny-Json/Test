import ssl
import socketserver

import http.server

PORT = 8443
CERTFILE = "cert.pem"
KEYFILE = "key.pem"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello from HTTPS server!")

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(CERTFILE, KEYFILE)

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"HTTPS Server running on port {PORT}")
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()