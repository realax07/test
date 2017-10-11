import Tank as q


h = ["content-type: text/xml", "user-agent: YaTank", "host: ozon.ru"]
d = {"/index.html":"<lol>azaza</lol>", "/main/public/void":"<head class='css'>Zagolovok</head>", "/s/v/a/%fsadfasrfas%/":"123"}

a = ["/index.xml", "/main/page/", "/search/"]



# print q.post(h, d)
i = 0

qwe = q.get(a, h)
print qwe




qwe = q.get_b(qwe)
qwe = qwe

for item in qwe:
    print item
