from models import Motel
import requests
import utils

def title(id):
    r = requests.get('http://localhost:61101/api/Motels/GetDataTitlePython/'+ id) 
    return r.text       

def requre(id):
    r = requests.get('http://localhost:61101/api/Motels/GetDataPython/'+ id)
    d = r.json()
    data = 0
    if len(d) != 0:
	data = 1
    return data
    