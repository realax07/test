from json import dumps as dmp
import decors

class dataset:
    # Callable objects:
    #   .data = data under head. Call as <list> of <list>'s
    #   .head = Head of data. Type <list>
    def __init__(self, f):
        self.data = self.__parseCsv(f)

    # Work with errors
    def __getattr__(self, item):
        print "Oops, we didn't have '%s' as object :(" % item

    # Modify len() function
    def __len__(self):
        return len(self.data)

    # Private method. Parsing .csv file as list of lists object.
    # Input 'file' as string's type of resulting reading .csv file
    def __parseCsv(self, file):
        i, data = 0, [""]
        for item in file:
            if item != "\n":
                data[i] += item
            else:
                data[i] = data[i].split(",")
                data.append("")
                i += 1

        data[i] = data[i].split(",")
        self.head = data[0]
        return data[1:]

    # parsing selected row as .json format. Input 'row' as Integer type
    @decors.catchErr
    def json(self, row):
        j, jsn = 0, {}
        for i in self.data[row]:
            if i[0] == ".":
                jsn[self.head[j]] = "0" + i
            else:
                jsn[self.head[j]] = i
            j += 1

        return dmp(jsn, sort_keys=True, indent=4)

    # Get array of values of column by columnName. Default - "Grade"
    @decors.catchErr
    def getColumn(self, key="Grade"):
        a, index = [], self.head.index(key)
        for item in self.data:
            a.append(item[index])

        return a