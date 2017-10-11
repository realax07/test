def catchErr(function):
    def wrapper(self, row):
        try:
            return function(self, row)
        except (ValueError, KeyError, IndexError):
            print "Dataset didn't have that value"
    return wrapper
