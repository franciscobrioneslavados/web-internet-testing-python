from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import speedtest
from hurry.filesize import size
st = speedtest.Speedtest()
d_st = st.download()
u_st = st.upload()
st.get_servers([])
ping = st.results.ping

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h1>Internet Testing.</h1>", "utf-8"))
        self.wfile.write(bytes("<h4>Tu velocidad de subida es: %s Bytes</p>" % size(round(u_st)), "utf-8"))
        self.wfile.write(bytes("<h4>Tu velocidad de descarga es: %s Bytes</p>" % size(round(d_st)), "utf-8"))
        self.wfile.write(bytes("<h4>Tu Ping es: %s</p>" % round(ping), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")