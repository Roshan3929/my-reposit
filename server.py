import http.server
import socketserver
import mimetypes

PORT = 8000

class BrotliHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
     def end_headers(self):
         if self.path.endswith('.br'):
            self.send_header('Content-Encoding', 'br')
         super().end_headers()
 
 # Add MIME types for WebGL build files
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('application/octet-stream', '.data')
mimetypes.add_type('application/wasm', '.wasm')
 
with socketserver.TCPServer(("", PORT), BrotliHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
