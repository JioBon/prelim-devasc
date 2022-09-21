from flask import Flask, jsonify, request

app = Flask(__name__)
hearts = [

    {
        "heart_id": "Heart1",
        "date": "01/22/2020",
        "heart_rate":  "70bpm"
    },
    {
        "heart_id": "Heart2",
        "date": "02/15/2020",
        "heart_rate":  "78bpm"
    },
    {
        "heart_id": "Heart3",
        "date": "10/05/2021",
        "heart_rate":  "81bpm"
    },


]

@app.route('/heart', methods=['GET'])
def getHeart():
    return jsonify(hearts)

@app.route('/heartid/<string:id>', methods=['GET'])
def getHeartID(id):
    heartid = [ heartid for heartid in hearts if heartid['heart_id'] == id ]
    #heartid = hearts.query.get(id)
    return ({"heart": heartid})

@app.route('/heart', methods=['POST'])
def addHeart():
    heart = request.get_json()
    hearts.append(heart)
    return {'id': len(hearts)}, 200

@app.route('/updateheart/<string:id>', methods=['PUT'])
def updateHeart(id):
    heartid = [ heartid for heartid in hearts if heartid['heart_id'] == id ]
    heartid[0]['heart_rate'] = request.json['heart_rate']
    return jsonify(hearts)

@app.route('/delheart/<string:id>', methods=['DELETE'])
def delHeart(id):
    heartid = [ heartid for heartid in hearts if heartid['heart_id'] == id ]
    hearts.remove(heartid[0])
    return jsonify(hearts)

if __name__ == '__main__':
    app.run()
