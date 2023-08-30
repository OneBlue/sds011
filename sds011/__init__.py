import sys
import serial
from flask import Flask, Response


app = Flask(__name__)

tty_path = None

def read_device():
    with serial.Serial(tty_path, 9600) as tty:
        if not tty.isOpen():
            tty.open()

        content = tty.read(10)

    if len(content) != 10:
        raise RuntimeError(f'Unexpected content length: {len(content)}')

    if [content[0], content[1], content[9]] != [0xaa, 0xc0, 0xab]:
        raise RuntimeError(f'Unexpected magic: {content}')

    pm25 = (content[3] * 256 + content[2]) / 10
    pm10 = (content[5] * 256 + content[4]) / 10

    return pm25, pm10


@app.route('/', methods=['GET'])
def get():
    content = 'sds011_pm25 {}\nsds011_p10 {}\n'.format(*read_device())

    return content, 200

def main():
    if len (sys.argv) != 4:
        print('Usage: {} <listen_address> <port> <serial device>'.format(sys.argv[0]))
        sys.exit(1)

    global tty_path
    tty_path = sys.argv[3]

    app.run(host=sys.argv[1], port=int(sys.argv[2]))

