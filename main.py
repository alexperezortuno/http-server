import argparse
import getopt
import os
import ssl
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

current_path: str = os.path.dirname(os.path.realpath(__file__))
secure: bool = False

try:
    for arg in sys.argv:
        if "-s" in arg or "--secure" in arg:
            option = arg.replace('-s=', '').replace('--secure=', '').lower()

            if option == 'yes' or option == 'y':
                secure = True
except Exception as e:
    print(e)

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--port', '-p', default=8000, type=int)
        parser.add_argument('--secure', '-s', default=False, type=str)
        parser.add_argument('--dir', '-d', default=os.path.dirname(os.path.realpath(__file__)), type=str)
        args = parser.parse_args()

        os.chdir(args.dir)

        server_address = ('', args.port)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        sa = httpd.socket.getsockname()

        if secure:
            httpd.socket = ssl.wrap_socket(httpd.socket,
                                           certfile=f'{current_path}/cert.pem',
                                           keyfile=f'{current_path}/key.pem',
                                           server_side=True)
            print("Serving HTTPS on %s port %s ..." % (sa[0], sa[1]))
        else:
            print("Serving HTTP on %s port %s ..." % (sa[0], sa[1]))
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print(f"HTTP close connection")
    except Exception as e:
        print(e)
