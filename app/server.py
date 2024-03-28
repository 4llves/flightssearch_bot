from flask import Flask, json

test_server = [{"server": "To On Uhulll 🤪"}]

api = Flask(__name__)

@api.route('/', methods=['GET'])
def get_test_server():
  return json.dumps(test_server)

def start_server():
  api.run(host='0.0.0.0', port=3000)

if __name__ == '__main__':
  start_server()