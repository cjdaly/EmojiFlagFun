#   Copyright [2022] Chris J Daly (github user cjdaly)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from flask import Flask, request, Response
from cc_scraper.cc_to_name import CC_to_Name

app = Flask(__name__)

int_A = 65 ; int_A_block = 127462
_letter_to_block = {chr(i+int_A):chr(i+int_A_block) for i in range(26)}
def L2B(letter):
    return _letter_to_block[letter]

HTML_template = "<html><head></head><body>{}</body></html>"
def CC_item(cc):
    return "{} : {}{} - {}".format(cc, L2B(cc[0]), L2B(cc[1]) , CC_to_Name[cc])

@app.route("/", methods=["GET"])
def root():
    output = HTML_template.format("Hello World!")
    return Response(output, mimetype="text/html")

@app.route("/<CC>", methods=["GET"])
def cc(CC):
    CC = CC.upper()
    txt = ""
    if len(CC) == 1 and CC.isalpha():
        for k in CC_to_Name.keys():
            if k[0] == CC:
                txt += CC_item(k) + "<br/>\n"
        output = HTML_template.format(txt)
        return Response(output, mimetype="text/html")
    elif CC in CC_to_Name:
        txt = CC_item(CC)
        output = HTML_template.format(txt)
        return Response(output, mimetype="text/html")
    else:
        txt = "Country code '{}' not found!".format(CC)
        output = HTML_template.format(txt)
        return Response(output, 404)
