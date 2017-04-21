from threading import Thread
from rpi_cs import app


if __name__ == "__main__":
    app.run(host='0.0.0.0')

def flask_app():
    app.run(host='0.0.0.0')


if __name__ == '__main__':

    t1 = Thread(target=flask_app)

    t1.start()
