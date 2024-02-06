import os
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
   return "<h1>Annuaire Internet</h1><p>Ce site est le prototype d’une API.</p>"

port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)