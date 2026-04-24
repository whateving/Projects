from http.server import BaseHTTPRequestHandler, HTTPServer


host = "localhost"
port = 8000


#########
# Handle the response here 
def block_request(self):
    self.send_response(403)  # Send a 403 Forbidden response
    self.send_header("content-type", "application/json")
    self.end_headers()
    self.wfile.write(b'{"message": "Request blocked"}')
    print("Blocking request")


def handle_request(self):
    self.send_response(200)
    self.send_header("content-type", "application/json")
    self.end_headers()
    self.wfile.write(b'{"message": "Request allowed"}')
    print("Handling request")


#########


class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        handle_request(self)


    def do_POST(self):
        # Check if the request path is '/tomcatwar.jsp'
        if self.path == "/tomcatwar.jsp":
            # Check if the required headers are present and match the specified values
            if (
                self.headers.get('suffix') == "%>//" and
                self.headers.get('c1') == "Runtime" and
                self.headers.get('c2') == "<%" and
                self.headers.get('DNT') == "1" and
                self.headers.get('Content-Type') == "application/x-www-form-urlencoded"
            ):
                block_request(self)
                return
        
        # If the request doesn't match the blocking criteria, handle it normally
        handle_request(self)


if __name__ == "__main__":        
    server = HTTPServer((host, port), ServerHandler)
    print("[+] Firewall Server")
    print("[+] HTTP Web Server running on: %s:%s" % (host, port))


    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


    server.server_close()
    print("[+] Server terminated. Exiting...")
    exit(0)
