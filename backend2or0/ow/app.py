from flask import Flask, request, jsonify, json, render_template, Response
from werkzeug.exceptions import HTTPException

from database import database
from datetime import datetime
from xml.dom import minidom
import xml
import xml.parsers
import yaml
from misc import *

import json

app = Flask(__name__)

@app.route('/sendJson', methods=['GET', 'POST'])
def add_message():

    print("initial string", request)
    try:
        abba = request.get_data(as_text=True)
        if(abba.lenght()>0):
            json_object = json.loads(abba)
            print("Is valid json? true")
            content = json_object  # request.json
            print(content['ships'])
            return jsonify({"uuid": "OK"})
        else:
            return jsonify({"JSON": "EMPTY"})
    except ValueError as e:
        print("Is valid json? false")
        return jsonify({"error": e})

@app.route('/list', methods=['GET','POST'])
def home():
    con = database("172.28.0.19", "root", "EinZweiDrei", "OW")

    now = datetime.now()
    dt_string = now.strftime("%Y.%m.%d")
    hm_string = now.strftime("%H:%M")
    print("date and time =", dt_string)

    data = (dt_string, hm_string, request.remote_addr)
    con.execute("INSERT INTO `odwiedziny`(`data`, `godzina`, `adres`) VALUES (%s,%s, %s);", data)

    con.queryAll("SELECT * FROM `odwiedziny`;", None)

    listOfIps = con.getResults()

    render = []
    for x in listOfIps[0]:
        render.append(TupleToArray(x))
        print(x)

    con.clearResult()
    con.clearMessages()
    return render_template("list.html", ip_list=render)
@app.route('/', methods=['GET', 'POST'])
def handle_request():
    headers = dict(request.headers)
    content = request.data.decode('utf-8')

    saveNewIP = database("172.28.0.19", "root", "EinZweiDrei", "OW")

    now = datetime.now()
    dt_string = now.strftime("%Y.%m.%d")
    hm_string = now.strftime("%H:%M")
    print("date and time =", dt_string)

    data = (dt_string, hm_string, request.remote_addr)
    saveNewIP.execute("INSERT INTO `odwiedziny`(`data`, `godzina`, `adres`) VALUES (%s,%s, %s);", data)

    if 'text/xml' in headers['Content-Type']:

    #TODO
#        try:
#            dom = xml.dom.minidom.parse(content)
#        except xml.parsers.expat.ExpatError as e:
#            handle_parse_error_xml()

        response_data = process_xml(content)
        return Response(response_data, mimetype='text/xml')

    elif 'text/yaml' in headers['Content-Type']:
    #TODO
#        try:
#            data = yaml.safe_load(content)
#        except yaml.YAMLError:
#            return handle_yaml_error()

        response_data = process_yaml(content)
        return Response(response_data, mimetype='application/x-yaml')

    elif 'text/html' in headers['Content-Type']:

        render = request.remote_addr
        return render_template("ip.html", your_ip=render)

    elif 'text/plain' in headers['Content-Type']:

        response_data = process_text(content)
        return Response(response_data, mimetype='text/plain')

    else:
        return Response('Unsupported format', status=415)


def handle_parse_error_xml(error=None):
    message = '<html><body><h1>Parse Error</h1><p>Failed to parse XML.</p></body></html>'
    return Response(message, status=400, mimetype='text/html')

@app.errorhandler(yaml.YAMLError)
def handle_yaml_error(error=None):
    message = '<html><body><h1>YAML Error</h1><p>Failed to parse YAML.</p></body></html>'
    return Response(message, status=400, mimetype='text/html')

# @app.errorhandler(Exception)
# def handle_generic_error(e):
#     # pass through HTTP errors
#     if isinstance(e, HTTPException):
#         return e
#     message = '<html><body><h1>Error</h1><p>An error occurred.</p></body></html>'
#     return Response(message, status=500, mimetype='text/html')

def process_xml(xml_data):
    root = minidom.Document()

    xml = root.createElement('root')
    root.appendChild(xml)

    clientChild = root.createElement('Client')
    clientChild.setAttribute('ip', request.remote_addr)

    xml.appendChild(clientChild)

    xml_str = root.toprettyxml(indent="\t")

    return xml_str

def process_yaml(yaml_data):
    yamlFile = {
        'IP Adress': request.remote_addr
    }

    # Zapisz dane do pliku YAML
    with open('ipyaml.yaml', 'w') as f:
        yaml.dump(yamlFile, f)

    file = open('ipyaml.yaml', 'r')
    content = file.read()
    file.close()

    return content

def process_text(text_data):
    txt_str = "IP of client: " + request.remote_addr
    return txt_str

if __name__ == '__main__':
    app.run(debug=True)
