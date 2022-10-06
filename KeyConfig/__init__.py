import os

__version__ = "0.0.2"

class config():
    """This object must be initialized only once."""
    __file = ""
    def __init__(self, pathToFile: str):
        """This function creates the basis for the program and *must* be called!"""
        try:
            def makeDirectory(path: str):
                if not os.path.isdir(path):
                    os.makedirs(path)
            self.__file = pathToFile
            fileDir = os.path.dirname(os.path.abspath(self.__file))
            makeDirectory(fileDir)
        except Exception as e:
            #print(e)
            pass
    def getConfig(self, targetKey, file = None):
        """Through this function you get the value to a key. The second value (file) can be passed if the file is different from the initially specified path."""
        if file == None:
            file = self.__file
        try:
            with open(file, "a+"): pass
            with open(file, "r") as f:
                content = f.read().split("\n")
            for lines in content:
                lines = lines.strip()
                if not lines.startswith("#>") and lines != "":
                    key, value = lines.split(":", 1)
                    if key == targetKey:
                        return value
            return None
        except Exception as e:
            #print(e)
            return "error"
    def setConfig(self, targetKey, targetValue, file = None):
        """Through this function you write the value to a key. The third value (file) can be passed if the file is different from the initially specified path."""
        if file == None:
            file = self.__file
        try:
            #print("File" + file)
            with open(file, "a+"): pass
            with open(file, "r") as f:
                content = f.read().split("\n")
            contents = []
            edited = False
            for lines in content:
                lines = lines.strip()
                if not lines.startswith("#>") and lines != "":
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
            #print(e)
            return "error"
    def addComment(self, text, removeOld = None, file = None):
        """This function creates a comment in the configuration file. It can also edit it."""
        if file == None:
            file = self.__file
        try:
            with open(file, "a+"): pass
            with open(file, "r") as f:
                content = f.read().split("\n")
                contentText = f.read()
            if removeOld != None:
                contents = []
                edited = False
                for lines in content:
                    lines = lines.strip()
                    if lines == "#> " + removeOld:
                        lines = "#> " + text
                        edited = True
                    contents.append(lines)
            with open(file, "w+") as f:
                if removeOld == None:
                    f.write(contentText.removeprefix("\n"))
                else:
                    f.write("\n".join(contents).removeprefix("\n"))
            return True
        except Exception as e:
            #print(e)
            return "error"