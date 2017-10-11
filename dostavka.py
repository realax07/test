body = """<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetArticleTrackingList xmlns="http://Ocourier.Services.Tracking/"><login>ApiUserIROrderApi</login><password>kqfheu54</password><Articles><Article>03414564-0048-1</Article></Articles><contractID>72179368000</contractID></GetArticleTrackingList></soap:Body></soap:Envelope>"""
headers = {'content-type': 'text/xml'}
url = '/principal/TrackingService.asmx?wsdl'

body1 = open("C:\\1\\1.txt", "r")
d = body1.read()
arr = d.split("\n")
stri = ""
body1 = open("C:\\1\\2.txt", "w")

for i in arr:
    stri += "490 " + url + "\n"
    stri += """<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetArticleTrackingList xmlns="http://Ocourier.Services.Tracking/"><login>ApiUserIROrderApi</login><password>kqfheu54</password><Articles><Article>%s</Article></Articles><contractID>72179368000</contractID></GetArticleTrackingList></soap:Body></soap:Envelope>\n""" % i

body1.write(stri)

print arr