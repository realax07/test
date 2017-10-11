# coding: utf8
#Uri and headers - is <list> type variables
def get(uri, headers):
    head, ammo = "", []
    for h in headers:                                                                                                   # Перебираем массив заголовков, и формируем строку со всеми заголовками и переносами
        head += h + "\n"

    for u in uri:                                                                                                       # Формируем запрос, который в последствии добавляем в массив ammo
        ammo.append("GET " + u + " HTTP/1.0" + "\n" + head)

    return ammo                                                                                                         # Возвращаем массив, каждый элемент которого - запрос

#ar - <list> type
def get_b(ar):
    a = []
    for q in ar:                                                                                                        # Считаем длину запроса и добавляем ее в начало запроса
        a.append(str(len(q) + q.count("\n")*2) + "\n" + q)

    return a                                                                                                            # Возвращаем массив с посчитанной длиной

#Headers - list type, uribody - dict type, where key is uri, value is body
def post(headers, uribody):
    s = ""
    for element in headers:                                                                                             # Формируем список заголовков и добавляем его в тело запроса
        s += "[" + element + "]" + "\n"

    for key in uribody:                                                                                                 # Формируем нагружаемые URL, тело запроса и считаем длину строки в символах.
        s += str(len(uribody[key])) + " " + key + "\n" + uribody[key] + "\n"

    return s                                                                                                            # Возвращаем строку, представляющую собой готовое тело "патрона"


