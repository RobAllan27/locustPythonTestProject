from flask import Flask, json

players = [{"id": 1, "name": "Speedy Rob","position": "Winger"}, 
        {"id": 2, "name": "Solid Richard","position": "Defender"},
        {"id": 3, "name": "Elusive Michael","position": "Attacker"}]

footballAPI = Flask(__name__)

@footballAPI.route('/players', methods=['GET'])
def get_players():
  return json.dumps(players)

# Simple API to create a player - returns constant value for test
@footballAPI.route('/player', methods=['POST'])
def post_player():
  return json.dumps({"success": True,"regoNumber": 12345}), 201

# Simple API to delete a player - returns constant value for test
@footballAPI.route('/player', methods=['DELETE'])
def delete_player():
  return json.dumps({"success": True, "regoNumber": 22}), 200

if __name__ == '__main__':
    footballAPI.run(host='localhost', port='5010')