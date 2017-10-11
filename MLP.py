from ML import dataset as ds

c = open("C:\wine.csv", "r")
d = ds(c.read())


print d.json(10)