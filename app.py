from flask import Flask, jsonify, request
from datetime import datetime
import logging

app = Flask(__name__)
with open('logging.txt', 'w') as file:
    file.write("----- THIS IS A LOGFILE ------" + "\n")

@app.route('/')
def hello():
    timestamp = datetime.now().strftime("%Y-%m-%d: %H:%M:%S")
    log_dict = {'ip':request.remote_addr, 'path':request.path, 'host':request.host, 'time':timestamp}
    with open('logging.txt', 'a') as file:
        for k in log_dict.keys():
            line = k + ' : ' + str(log_dict[k]) + '\n'
            file.write(line)
        file.write('--------------------' + '\n')
    return jsonify(log_dict)

if __name__ == "__main__":
    
    app.run()
