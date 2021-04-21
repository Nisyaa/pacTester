from flask import Flask, render_template, request, redirect, url_for
import pacparser
from urlparse import urlparse


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/parse_result/", methods=["POST"])
def parse_result():
    if request.method == 'POST':
        client_ip = request.form["cip"]
        target_url = request.form["turl"]
        pac_string = request.form["pac"]
        if client_ip == '' or target_url == '' or pac_string == '':
            return render_template("index.html")
        else:
            parsed_url = urlparse(target_url).netloc
            pacparser.init()
            pacparser.parse_pac_string(pac_string)
            pacparser.setmyip(client_ip)
            proxy = pacparser.find_proxy(target_url, parsed_url)
            pacparser.cleanup()
            return render_template("index.html", pacresult=proxy)


if __name__ == '__main__':
    app.run()
