import http.server
import socketserver
from load_env import PORT

Handler = http.server.SimpleHTTPRequestHandler


if __name__ == '__main__':
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving at port: {PORT}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"HTTP close connection")
    except Exception as e:
        print(e)
