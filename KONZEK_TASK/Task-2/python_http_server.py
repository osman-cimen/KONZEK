from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 8080  # Default port for the server

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple Python HTTP server!")

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), CustomHandler)
    print(f"Server started on {HOST}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        server.server_close()

