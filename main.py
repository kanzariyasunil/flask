from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    name = request.args.get('name')
    if name:
        return jsonify({"status":200,"message":f"hello {name} how are you"})
    return "<h1> write in url ? name=any one name </h1>"

if __name__ == "__main__":
    app.run(debug=True)

