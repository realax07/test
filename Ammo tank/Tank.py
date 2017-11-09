# coding: utf8
import random
#ar - <list> type
def get_b(ar):
    a = []
    for q in ar:                                                                                                        # Считаем длину запроса и добавляем ее в начало запроса
        a.append(str(len(q) + q.count("\n")*2) + "\n" + q)

    return a                                                                                                            # Возвращаем массив с посчитанной длиной

#Headers - <list> type
#Uribody - <dict> type, where key is uri, value is body
def post(headers, uribody):
    st = ""
    for element in headers:                                                                                             # Формируем список заголовков и добавляем его в тело запроса
        st += "[" + element + "]" + "\n"

    for key in uribody:                                                                                                 # Формируем нагружаемые URL, тело запроса и считаем длину строки в символах.
        st += str(len(uribody[key])) + " " + key + "\n" + uribody[key] + "\n"

    return st                                                                                                           # Возвращаем строку, представляющую собой готовое тело "патрона"

#Count - <int>
#Uri - <list>
#Headers - <dict> where key is <str> type and value is <list> type
#Http_ver - <str>
def get(count, uri, headers, http_ver = "HTTP 1.0"):
    ammo = []
    for patron in range(1, count + 1):
        s = "GET " + uri[random.randint(0, len(uri)-1)] + " " + http_ver
        for p in headers:
            s += "\n" + p + ": " + headers[p][random.randint(0, len(headers[p])-1)]
        ammo.append(s)

    return ammo

