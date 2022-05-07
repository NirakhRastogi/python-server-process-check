from http.server import BaseHTTPRequestHandler, HTTPServer
import processCheck
import json
import sys

#To start the server run - python -u "f:\Learning\Python\server\local_server.py" localhost 8080 System 40 passtest.txt F:\Learning\Python\server False

hostName:str = sys.argv[1]
serverPort:int = int(sys.argv[2])
processName:str = sys.argv[3]
processPID:int = int(sys.argv[4])
fileName:str = sys.argv[5]
filePath:str = sys.argv[6]
skipCheckPID:bool = bool(sys.argv[7])


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        is_process_running = processCheck.check_running_process(processPID, processName, skipCheckPID)
        does_file_exists = processCheck.check_file_exists_at_location(fileName, filePath)
        status:int = 404
        if is_process_running and does_file_exists:
            status = 200
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response= {"process_name":processName,"process_pid":processPID,"process_running":is_process_running,"check_file_exists":does_file_exists, "status": status, "pid_skip_check": skipCheckPID}
        response_str:str = json.dumps(response)
        print(response_str)
        self.wfile.write(bytes(response_str, "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")