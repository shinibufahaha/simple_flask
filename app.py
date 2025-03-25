from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
    return render_template("index.html")

@app.route("/get_index", methods=['GET', 'POST', 'PUT', 'DELETE'])
def about():
    return render_template("index.html")

@app.route("/get_js", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_js():
    # js = request.args.get("js")
    # print(js)
    return "jet_js"

@app.route("/intent_data", methods=['GET', 'POST', 'PUT', 'DELETE'])
def intent_data():
    return render_template("intent_data.html")


@app.route("/simple", methods=['GET', 'POST', 'PUT', 'DELETE'])
def log_activity():
    print(request.args.get("activity_name"))
    return "ok"

@app.route("/file_picker", methods=['GET', 'POST', 'PUT', 'DELETE'])
def file_picker():
    return render_template("file_picker.html")

@app.route("/native", methods=['GET', 'POST', 'PUT', 'DELETE'])
def native():
    return render_template("native_method.html")

@app.route("/download", methods=['GET', 'POST', 'PUT', 'DELETE'])
def download():
    # return a file
    return send_file("./templates/index.html")

@app.route("/upload", methods=['GET', 'POST', 'PUT', 'DELETE'])
def upload():
    print(request.args.get("filePath"))
    return "ok"

@app.route("/fetch", methods=['GET', 'POST', 'PUT', 'DELETE'])
def fetch():
    return render_template("fetch.html")

@app.route("/run", methods=['GET', 'POST', 'PUT', 'DELETE'])
def run_js():
    return render_template("run_js.html")

@app.route("/ali", methods=['GET', 'POST', 'PUT', 'DELETE'])
def ali():
    return render_template("ali/youku.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
