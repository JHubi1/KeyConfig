import os

__version__ = "0.0.2"

class config():
    __file = ""
    def __init__(self, pathToFile):
        def makeDirectory(path: str):
            if not os.path.isdir(path):
                os.makedirs(path)
        self.__file = pathToFile
        fileDir = os.path.dirname(os.path.abspath(self.__file))
        makeDirectory(fileDir)
    def getConfig(self, targetKey, file = None):
        if file == None:
            file = self.__file
        try:
            with open(file, "a+"): pass
            with open(file, "r") as f:
                content = f.read().split("\n")
            for lines in content:
                if not lines.startswith("#>"):
                    key, value = lines.split(":", 1)
                    if key == targetKey:
                        return value
            return False
        except Exception as e:
            #print(e)
            return False
    def setConfig(self, targetKey, targetValue, file = None):
        if file == None:
            file = self.__file
        try:
            print("File" + file)
            with open(file, "a+"): pass
            with open(file, "r") as f:
                content = f.read().split("\n")
            contents = []
            edited = False
            for lines in content:
                if not lines.startswith("#>"):
                    key = lines.split(":", 1)[0]
                    if key == targetKey:
                        lines = key + ":" + targetValue
                        edited = True
                    contents.append(lines)
            if edited == False:
                contents.append(targetKey + ":" + targetValue)
            with open(file, "w+") as f:
                f.write("\n".join(contents).removeprefix("\n"))
            return True
        except Exception as e:
            print(e)
            return False