import datetime
import json

class Motel:
    Id = "",
    Title = "",
    Price = "",
    PriceType = "",
    DateUpdate = datetime,
    DateDue = datetime,
    Time = "",
    Status = "",
    Verify = "",
    Address = "",
    Description = "",
    Phone = "",
    Typemotel = "",
    AreaZone = "",
    AreaZoneType = "",
    Typeservice = "",
    Bathroom = "",
    Livingroom = "",
    Latitude = "",
    Longitude = "",
    CityId = "",
    CityName = "",
    ProvinceId = "",
    ProvinceName = "",
    DistrictId = "",
    DistrictName = "",
    StreetId = "",
    StreetName = "",
    UserId = "",
    HovaTen = ""
    MergerTable = ""
    Keyword = ""

    def __init__(self,id, title, price, priceType, dateUpdate, dateDue, time, status, verify, address, description, phone, typemotel, areaZone, 
                    areaZoneType, typeservice, bathroom, livingroom, latitude, longitude, city, province, district , street, user, mergerTable, keyword):
        self.Id = id
        self.Title = title
        self.Price = price
        self.PriceType = priceType
        self.DateUpdate = dateUpdate
        self.DateDue = dateDue
        self.Time = time
        self.Status = status
        self.Verify = verify
        self.Address = address
        self.Description = description
        self.Phone = phone
        self.Typemotel = typemotel
        self.AreaZone = areaZone
        self.AreaZoneType = areaZoneType
        self.Typeservice = typeservice
        self.Bathroom = bathroom
        self.Livingroom = livingroom
        self.Latitude = latitude
        self.Longitude = longitude
        self.CityId = city['id']
        self.CityName = city['name']
        self.ProvinceId = province['id']
        self.ProvinceName = province['name']
        self.DistrictId = district['id']
        self.DistrictName = district['name']
        self.StreetId = street['id']
        self.StreetName = street['name']
        self.UserId = user['id']
        self.HovaTen = user['hovaTen']
        self.MergerTable = mergerTable
        self.Keyword = keyword
