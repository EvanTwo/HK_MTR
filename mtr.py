import requests
import json
from flask import Flask, render_template

url = f"https://rt.data.gov.hk/v1/transport/mtr/getSchedule.php?line=TKL&sta=TKO"
app = Flask(__name__)

AEL = ["AWE", "AIR", "TSY", "KOW", "HOK"]
TCL = ["TUC", "SUN", "TSY", "LAK", "NAC", "OLY", "KOW", "HOK"]
TML = ["TUM", "SIH", "TIS", "LOP", "YUL", "KSR", "TWW", "MEF", "NAC", "AUS", "ETS", "HUH", "HOM", "TKW", "SUW", "KAT", "DIH", "HIK", "TAW", "CKT", "STW", "CIO", "SHM", "TSH", "HEO", "MOS", "WKS"]
TKL = ["POA", "HAH", "LHP", "TKO", "TIK", "YAT", "QUB", "NOP"]
EAL = ["LMC", "LOW", "SHS", "FAN", "TWO", "TAP", "UNI", "FOT", "RAC", "SHT", "TAW", "KOT", "MKK", "HUH", "EXC", "ADM"]
SIL = ["SOH", "LET", "WCH", "OCP", "ADM"]
TWL = ["TSW", "TWH", "KWH", "KWF", "LAK", "MEF", "LCK", "CSW", "SSP", "PRE", "MOK", "YMT", "JOR", "TST", "ADM", "CEN"]
ISL = ["CHW", "HFC", "SKW", "SWH", "TAK", "QUB", "NOP", "FOH", "TIH", "CAB", "WAC", "ADM", "CEN", "SHW", "SYP", "HKU", "KET"]
KTL = ["TIK", "YAT", "LAT", "KWT", "NTK", "KOB", "CHH", "DIH", "WTS", "LOF", "KOT", "PRE", "MOK", "YMT", "HOM", "WHA"]

mtrStops = [AEL, TCL, TML, TKL, EAL, SIL, TWL, ISL, KTL]

def fetch_MTR_data():
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return None


def render_MTR():
    MTR_data = fetch_MTR_data()
    print (MTR_data)



render_MTR()
