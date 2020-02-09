# The MIT License
#
# Copyright (c) 2019 - Present Firebolt, Inc. & Firebolt Space Agency(FSA).
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
import json
import urllib.error
import urllib.parse
import urllib.request

from src import config
from src import utils
if config.DEBUG:
    from pudb import set_trace
    
telemetry = {}
commands = {}


class TelemetryNotAvailable(Exception):
    """This exception should be raised when we do not have a list of available telemetry"""
    pass


class KSPNotConnected(Exception):
    """ This exception should be raised when there is no connection to KSP """
    pass


def check_connection():


    try:
        urllib.request.urlopen(config.URL + "paused=p.paused")
    except urllib.error.URLError:
        return False
    else:
        return True


def get_api_listing():

    global telemetry
    global commands
    try:
        response = urllib.request.urlopen(config.URL + "api=a.api")
    except urllib.error.URLError:
        raise KSPNotConnected
    response_string = response.read().decode('utf-8')
    data = json.loads(response_string)

    for a in data.values():
        for b in a:
            if b["apistring"].startswith("b."):
                name = "body_" + b["apistring"].rsplit(".", 1)[1]
            elif b["apistring"].startswith("tar."):
                name = "target_" + b["apistring"].rsplit(".", 1)[1]
            elif b["apistring"].startswith("f.") or b["apistring"].startswith("mj.") or \
                    b["apistring"].startswith("v.set"):
                command = b["apistring"].rsplit(".", 1)[1]
                commands[command] = b["apistring"]
                continue
            else:
                name = b["apistring"].rsplit(".", 1)[1]
            telemetry[name] = b["apistring"]


def get_telemetry(data, body_number=None):

    try:
        query_string = data + "=" + telemetry[data]
    except KeyError:
        raise KSPNotConnected
        return
    if body_number:
        query_string += "[{}]".format(body_number)

    try:
        raw_response = urllib.request.urlopen(config.URL + query_string)
    except urllib.error.URLError:
        utils.log("Query string: {}".format(query_string), log_level="ERROR")
        utils.log("Caught exception urllib2.URLERROR", log_level="ERROR")
        raise KSPNotConnected
    response_string = raw_response.read().decode("utf-8)")
    json_response = json.loads(response_string)
    return json_response[data]

def set_mechjeb_smartass(direction):

    command_string = "command=" + commands[direction]
    send_command_to_ksp(command_string)

def disable_smartass():
    command_string = "command=" + commands["smartassoff"]
    send_command_to_ksp(command_string)

def set_throttle(throttle_percent):
    if throttle_percent == 0:
        throttle_magnitude = 0
    else:
        throttle_magnitude = throttle_percent / 100.0
    command_string = "command=" + commands["setThrottle"] + "[" + str(throttle_magnitude) + "]"
    send_command_to_ksp(command_string)

def cut_throttle():
    command_string = "command=" + commands["throttleZero"]
    send_command_to_ksp(command_string)

def send_command_to_ksp(command_string):
    
    try:
        urllib.request.urlopen(config.URL + command_string)
    except urllib.error.URLError:
        utils.log("Query string: {}".format(command_string), log_level="ERROR")
        utils.log("Caught exception urllib2.URLERROR", log_level="ERROR")
        raise KSPNotConnected

def print_all_telemetry():
    print("Telemetry available:")
    for item in sorted(telemetry):
        print("- " + item)
    print()
    print("Commands available:")
    for item in sorted(commands):
        print("- " + item)

def add_maneuver_node(ut, delta_v):

    ut = str(round(ut, 2))
    delta_v_x = str(round(delta_v[0], 2))
    delta_v_y = str(round(delta_v[1], 2))
    delta_v_z = str(round(delta_v[2], 2))
    command_string = "command=" + telemetry["addManeuverNode"] + "[" + str(ut) + "," + delta_v_x  + "," + delta_v_y  + "," + delta_v_z + "]"
    send_command_to_ksp(command_string)

def update_maneuver_node(ut, delta_v):
    ut = str(round(ut, 2))
    delta_v_x = str(round(delta_v[0], 2))
    delta_v_y = str(round(delta_v[1], 2))
    delta_v_z = str(round(delta_v[2], 2))
    command_string = "command=" + telemetry["updateManeuverNode"] + "[0," + str(ut) + "," + delta_v_x  + "," + delta_v_y  + "," + delta_v_z + "]"
    send_command_to_ksp(command_string)