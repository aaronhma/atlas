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
import inspect
import sys
from collections import OrderedDict

from src import config
if config.DEBUG:
    from pudb import set_trace 
from src import utils
from src.telemachus import get_telemetry, TelemetryNotAvailable

computer = None

def octal(value):

    """ Converts a value to octal, but not written as Ooxxx
    :param value: the value to convert
    :return: the octal value
    :rtype: int
    """

    return int(oct(value))


class NounNotImplementedError(Exception):

    """ This exception should be raised when a selected noun is not implemented
        yet
    """

    pass


class Noun(object):

    def __init__(self, description, number):
        self.description = description
        self.number = number

    def return_data(self):
        raise NounNotImplementedError


class Noun09(Noun):

    def __init__(self):
        super().__init__(description="Alarm Codes", number="09")

    def return_data(self):

        utils.log("Noun 09 requested")
        alarm_codes = computer.alarm_codes
        data = {
            1: str(alarm_codes[0]),
            2: str(alarm_codes[1]),
            3: str(alarm_codes[2]),
            "is_octal": True,
            "tooltips": [
                "First alarm code",
                "Second alarm code",
                "Last alarm code",
            ],
        }
        return data


class Noun14(Noun):

    def __init__(self):
        super().__init__(description="Burn error display (Expected Δv at cutoff (xxxxx m/s), Actual Δv at"
                                                 "cutoff (xxxxx m/s), Difference (xxxx.x m/s)",
                                     number="14")

    def return_data(self):
        if not computer.next_burn:
            computer.program_alarm(115)
            return False
        burn = computer.next_burn
        expected_delta_v_at_cutoff = burn.velocity_at_cutoff
        actual_delta_v_at_cutoff = get_telemetry("orbitalVelocity")
        delta_v_error = actual_delta_v_at_cutoff - expected_delta_v_at_cutoff

        expected_delta_v_at_cutoff = str(int(expected_delta_v_at_cutoff)).replace(".", "")
        actual_delta_v_at_cutoff = str(int(actual_delta_v_at_cutoff)).replace(".", "")
        delta_v_error = str(round(delta_v_error, 1)).replace(".", "")

        data = {
            1: expected_delta_v_at_cutoff,
            2: actual_delta_v_at_cutoff,
            3: delta_v_error,
            "tooltips": [
                "Expected velocity at cutoff (xxxxx m/s)",
                "Actual velocity at cutoff (xxxxx m/s)",
                "Velocity error (xxxx.x m/s)"
            ],
            "is_octal": False,
        }
        return data

class Noun17(Noun):

    def __init__(self):
        super().__init__("Attitude (Roll, Pitch, Yaw)", number="17")

    def return_data(self):

        try:
            roll = str(round(get_telemetry("roll"), 1))
            pitch = str(round(get_telemetry("pitch"), 1))
            yaw = str(round(get_telemetry("heading"), 1))
        except TelemetryNotAvailable:
            raise

        roll = roll.replace(".", "")
        pitch = pitch.replace(".", "")
        yaw = yaw.replace(".", "")

        data = {
            1: roll,
            2: pitch,
            3: yaw,
            "is_octal": False,
            "tooltips": [
                "Roll (0xxx.x°)",
                "Pitch (0xxx.x°)",
                "Yaw (0xxx.x°)",
            ],
        }
        return data


class Noun25(Noun):
    
    def __init__(self):
        
        super().__init__("Spacecraft mass", number="25")
        self.mass_whole_part = computer.noun_data["25"][0]
        self.mass_fractional_part = computer.noun_data["25"][1]

    def return_data(self):

        data = {
            1: self.mass_whole_part,
            2: self.mass_fractional_part,
            3: "bbbbb",
            "tooltips": ["Spacecraft mass ", None, None],
            "is_octal": True,
        }
        return data



        
class Noun30(Noun):
    
    def __init__(self):
        
        super().__init__("Octal Target ID (000XX)", number="30")

    def return_data(self):

        target_id = computer.noun_data["30"][0]
        data = {
            1: target_id,
            2: "",
            3: "",
            "tooltips": ["Target Octal ID", None, None],
            "is_octal": True,
        }
        return data

    def receive_data(self, data):
        computer.noun_data["30"] = data

class Noun31(Noun):
    
    def __init__(self):
        
        super().__init__("Stage Max Thrust", number="31")

    def return_data(self):

        
        data = {
            1: computer.noun_data["31"][0],
            2: computer.noun_data["31"][1],
            3: "bbbbb",
            "tooltips": ["Stage Max Thrust (s) ", None, None],
            "is_octal": False,
        }
        return data

class Noun33(Noun):

    def __init__(self):
        super().__init__("Time to Ignition (00xxx hours, 000xx minutes, 0xx.xx seconds)", number="33")

    def return_data(self):

        if not computer.next_burn:
            computer.program_alarm(alarm_code=115, message="No burn data loaded")
            return False
        time_until_ignition = utils.seconds_to_time(computer.next_burn.calculate_time_to_ignition())
        hours = str(int(time_until_ignition["hours"]))
        minutes = str(int(time_until_ignition["minutes"]))
        seconds = str(int(time_until_ignition["seconds"])).replace(".", "")

        data = {
            1: "-" + hours,
            2: "-000" + minutes,
            3: "-000" + seconds,
            "tooltips": [
                "Time To Ignition (hhhhh)",
                "Time To Ignition (bbbmm)",
                "Time To Ignition (bbbss)",
            ],
            "is_octal": False,
        }
        return data


class Noun36(Noun):

    def __init__(self):
        super().__init__("Mission Elapsed Time (MET) (dddhh, bbbmm, bss.ss)", number="36")

    def return_data(self):
        try:
            telemetry = get_telemetry("missionTime")
        except TelemetryNotAvailable:
            raise

        minutes, seconds = divmod(telemetry, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        days = str(int(days)).zfill(2)
        hours = str(int(hours)).zfill(2)
        minutes = str(int(minutes)).zfill(2)
        seconds = str(round(seconds, 2)).replace(".", "").zfill(4)
        data = {
            1: days + "b" + hours,
            2: "bbb" + minutes,
            3: "b" + seconds,
            "tooltips": [
                "Mission Elapsed Time (ddbhh)",
                "Mission Elapsed Time (bbbmm)",
                "Mission Elapsed Time (bss.ss)",
            ],
            "is_octal": False,
        }
        return data

class Noun38(Noun):
    
    def __init__(self):
        
        super().__init__("Specific Impulse", number="38")

    def return_data(self):

        
        data = {
            1: computer.noun_data["38"][0],
            2: "bbbbb",
            3: "bbbbb",
            "tooltips": ["Stage Specific Impulse (s) ", None, None],
            "is_octal": False,
        }
        return data


class Noun40(Noun):

    def __init__(self):
        super().__init__("Burn Data (Time from ignition, orbital velocity, accumulated Δv", number="40")

    def return_data(self):
        if not computer.next_burn:
            computer.program_alarm(115)
            return False
        burn = computer.next_burn
        time_to_ignition = utils.seconds_to_time(burn.time_until_ignition)
        minutes_to_ignition = str(int(time_to_ignition["minutes"])).zfill(2)
        seconds_to_ignition = str(int(time_to_ignition["seconds"])).zfill(2)
        velocity = str(int(get_telemetry("orbitalVelocity"))).replace(".", "")
        accumulated_delta_v = str(int(burn.accumulated_delta_v)).replace(".", "")

        data = {
            1: "-" + minutes_to_ignition + "b" + seconds_to_ignition,
            2: velocity,
            3: accumulated_delta_v,
            "is_octal": False,
            "tooltips": [
                "Time From Ignition (mmbss minutes, seconds)",
                "Orbital Velocity (xxxxx m/s)",
                "Accumulated Δv (xxxxx m/s)",
            ],
        }
        return data

class Noun43(Noun):

    def __init__(self):
        super().__init__("Geographic Position (Latitude, Longitude, Altitude)", number="43")

    def return_data(self):
        try:

            latitude = str(round(get_telemetry("lat"), 2))
            longitude = str(round(get_telemetry("long"), 2))
            altitude = str(round(get_telemetry("altitude") / 1000, 1))
        except TelemetryNotAvailable:
            raise


        if latitude[-2] == ".":
            latitude += "0"
        if longitude[-2] == ".":
            longitude += "0"

        latitude = latitude.replace(".", "")
        longitude = longitude.replace(".", "")
        altitude = altitude.replace(".", "")

        data = {
            1: latitude,
            2: longitude,
            3: altitude,
            "is_octal": False,
            "tooltips": [
                "Latitude (xxx.xx°)",
                "Longitude (xxx.xx°)",
                "Altitude",  # TODO
            ],
        }
        return data

class Noun44(Noun):
    def __init__(self):
        super().__init__("Apoapsis (xxx.xx km), Periapsis (xxx.xx km), Time To Apoapsis (hmmss)",
                                     number="44")

    def return_data(self):
        try:
            apoapsis = str(round(get_telemetry("ApA") / 100, 1))
            periapsis = str(round(get_telemetry("PeA") / 100, 1))
            tff = int(get_telemetry("timeToAp"))
        except TelemetryNotAvailable:
            raise

        apoapsis = apoapsis.replace(".", "")
        periapsis = periapsis.replace(".", "")

        tff_minutes, tff_seconds = divmod(tff, 60)
        tff_hours, tff_minutes = divmod(tff_minutes, 60)

        tff = str(tff_hours).zfill(1) + str(tff_minutes).zfill(2) + str(tff_seconds).zfill(2)

        data = {
            1: apoapsis,
            2: periapsis,
            3: tff,
            "tooltips": [
                "Apoapsis Altitude (xxx.xx km)",
                "Periapsis Altitude (xxx.xx km)",
                "Time to Apoapsis (hmmss)"
            ],
            "is_octal": False,
        }
        return data




class Noun50(Noun):
    def __init__(self):
        super().__init__("Surface Velocity Display (X, Y, Z in xxxx.x m/s)", number="50")

    def return_data(self):
        surface_velocity_x = str(round(get_telemetry("surfaceVelocityx"), 1)).replace(".", "")
        surface_velocity_y = str(round(get_telemetry("surfaceVelocityy"), 1)).replace(".", "")
        surface_velocity_z = str(round(get_telemetry("surfaceVelocityz"), 1)).replace(".", "")

        data = {
            1: surface_velocity_x,
            2: surface_velocity_y,
            3: surface_velocity_z,
            "tooltips": [
                "Surface Velocity X (xxxx.x m/s)",
                "Surface Velocity Y (xxxx.x m/s)",
                "Surface Velocity Z (xxxx.x m/s)"
            ],
            "is_octal": False,
        }
        return data


class Noun62(Noun):
    def __init__(self):
        super().__init__("Orbital Velocity, Altitude Rate, Altitude", number="62")

    def return_data(self):
        surface_velocity = str(round(get_telemetry("relativeVelocity"), 1))
        altitude_rate = str(round(get_telemetry("verticalSpeed"), 1))
        altitude = str(round(get_telemetry("altitude") / 1000, 1))

        surface_velocity = surface_velocity.replace(".", "")
        altitude_rate = altitude_rate.replace(".", "")
        altitude = altitude.replace(".", "")

        data = {
            1: surface_velocity,
            2: altitude_rate,
            3: altitude,
            "is_octal": False,
            "tooltips": [
                "Inertial Velocity (xxxx.x m/s)",
                "Altitude Rate (xxxx.x m/s)",
                "Altitude (xxxx.x km)",
            ],
        }
        return data


class Noun95(Noun):
    
    def __init__(self):
        super().__init__(description="TMI Burn Data Display", number="95")

    def return_data(self):

        if not computer.next_burn:
            computer.program_alarm(115)
            return False

        time_to_ignition = utils.seconds_to_time(computer.next_burn.time_until_ignition)
        minutes_to_ignition = str(int(time_to_ignition["minutes"])).zfill(2)
        seconds_to_ignition = str(int(time_to_ignition["seconds"])).zfill(2)
        delta_v = str(int(computer.next_burn.delta_v_required))
        burn_duration = str(int(computer.next_burn.burn_duration))

        data = {
            1: "-" + minutes_to_ignition + "b" + seconds_to_ignition,
            2: delta_v,
            3: burn_duration,
            "is_octal": False,
            "tooltips": [
                "Time To Ignition (TIG) (xxbxx mins, seconds)",
                "Δv (xxxxx m/s)",
                "Burn duration (xxxxx seconds)",
            ],
        }
        return data

class OrderedDictDefaultNoun(OrderedDict):

    def __init__(self):
        super().__init__()
    
    def __getitem__(self, name):
        try:
            return super().__getitem__(name)
        except KeyError:
            self[name] = type("Noun" + name, (Noun,), {'__init__' : lambda self: Noun.__init__(self, description='Undefined', number=name)})
            return self[name]
            
nouns = OrderedDictDefaultNoun()
clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
for class_tuple in clsmembers:
    if class_tuple[0][-1].isdigit():
        nouns[class_tuple[0][-2:]] = class_tuple[1]