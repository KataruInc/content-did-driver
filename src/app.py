from flask import Flask, jsonify
from error import UnsupportedDID, InvalidDID, Internal
from resolver import resolve
app = Flask(__name__)

@app.route('/1.0/identifiers/<did>')
def handleResolve(did):
  try:
    didDocument = resolve(did)    
    return jsonify(didDocument), 200
  except UnsupportedDID:
    return jsonify({"message": "unsupported did method", "did": did}), 400
  except InvalidDID:
    return jsonify({"message": "invalid did format", "did": did}), 400
  except Internal:
    return jsonify({"message": "internal error", "did": did}), 503

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8888)