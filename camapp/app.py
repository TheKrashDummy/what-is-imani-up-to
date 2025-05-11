from flask import Flask, send_file, make_response
from flask_cors import CORS
from picamera2 import Picamera2
import time
import io
import sys
import json

app = Flask(__name__)
CORS(app)
picam2 = Picamera2()
camera_config = picam2.create_still_configuration()
picam2.configure(camera_config)
picam2.start()
time.sleep(2)  # Let camera warm up

@app.route('/snapshot')
def snapshot():
    image_stream = io.BytesIO()
    picam2.capture_file(image_stream, format='jpeg')
    image_stream.seek(0)
    resp = make_response(send_file(image_stream, mimetype='image/jpeg'))
    resp.headers['Access-Control-Allow-Origin'] = '*' 

    # Print headers to stderr for visibility
    print("Response headers:", file=sys.stderr)
    for header, value in resp.headers.items():
        print(f"{header}: {value}", file=sys.stderr)

    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)