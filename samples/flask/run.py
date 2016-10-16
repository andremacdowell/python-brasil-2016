# encoding: utf-8
from resources import app

PORT = 5000


def execute(debug):
    app.run(host="0.0.0.0", port=PORT, debug=debug)


if __name__ == "__main__":  # pragma: no cover
    execute(debug=True)
