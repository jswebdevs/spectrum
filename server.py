#!/usr/bin/env python3
import http.server
import socketserver
import gzip
import io
import os
import sys

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PORT = 5000

class ProductionLikeHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            return super().send_head()
        
        ctype = self.guess_type(path)
        ext = os.path.splitext(path)[1].lower()
        ae = self.headers.get('Accept-Encoding', '')
        
        # Enable gzip text compression for web assets
        if 'gzip' in ae and ext in ['.css', '.js', '.html', '.json', '.xml', '.txt', '.svg']:
            try:
                with open(path, 'rb') as f:
                    content = f.read()
                compressed = gzip.compress(content, 6)
                self.send_response(200)
                self.send_header('Content-Type', ctype)
                self.send_header('Content-Encoding', 'gzip')
                self.send_header('Content-Length', str(len(compressed)))
                self.send_header('Vary', 'Accept-Encoding')
                # Never cache HTML, CSS, JS during development so mobile devices always see live edits
                if ext in ['.css', '.js', '.html']:
                    self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
                    self.send_header('Pragma', 'no-cache')
                    self.send_header('Expires', '0')
                else:
                    self.send_header('Cache-Control', 'public, max-age=3600')
                self.end_headers()
                return io.BytesIO(compressed)
            except OSError:
                return super().send_head()
        
        # Add cache headers for images and other static assets
        if ext in ['.webp', '.png', '.jpg', '.jpeg', '.svg', '.ico', '.woff', '.woff2']:
            try:
                f = open(path, 'rb')
            except OSError:
                self.send_error(404, "File not found")
                return None
            try:
                fs = os.fstat(f.fileno())
                self.send_response(200)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(fs[6]))
                self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
                self.send_header("Cache-Control", "public, max-age=3600")
                self.end_headers()
                return f
            except Exception:
                f.close()
                raise

        return super().send_head()

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == '__main__':
    with ThreadingHTTPServer(('0.0.0.0', PORT), ProductionLikeHTTPHandler) as httpd:
        print(f"Serving Spectrum site at http://0.0.0.0:{PORT}/ from {DIRECTORY} with gzip compression enabled...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

