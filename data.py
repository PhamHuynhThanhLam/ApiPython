from models import Motel
import requests
import utils

def title(id):
    r = requests.get('http://localhost:61101/api/Motels/GetDataTitlePython/'+ id)
    return r.text       

def requre(id):
    r = requests.get('http://localhost:61101/api/Motels/GetDataPython/'+ id)
    d = r.json()
    data = []
    test = 0
    if len(d) != 0:
        test = 1
    return test
    # if len(data) != 0:
    #     data = []
    # if len(d) != 0:
    #     for i in range(0, len(d), 1):
    #         merge = d[i]['title']+' '+ utils.cleanhtml(d[i]['description'])
    #         key = utils.clean_text(merge)
    #         removeKey = utils.remove_stopwords(key)
    #         motel = Motel(d[i]['id'], d[i]['title'], d[i]['price'], d[i]['priceType'], d[i]['dateUpdate'], d[i]['dateDue'], d[i]['time'], d[i]['status'], 
    #                 d[i]['verify'], d[i]['address'], utils.cleanhtml(d[i]['description']), d[i]['phone'], d[i]['typemotel'], d[i]['areaZone'], d[i]['areaZoneType'], 
    #                 d[i]['typeservice'], d[i]['bathroom'], d[i]['livingroom'], d[i]['latitude'], d[i]['longitude'], d[i]['city'], d[i]['province'], 
    #                 d[i]['district'], d[i]['street'], d[i]['user'], merge, removeKey)
    #         data.append(motel.__dict__)
    # return data
    