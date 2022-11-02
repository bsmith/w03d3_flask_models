from flask import Flask

app = Flask(__name__)

from controllers.controller import blueprint
app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(debug=True)