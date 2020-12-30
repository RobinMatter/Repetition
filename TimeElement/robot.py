class Robot(object):

    def __init__(self, name):
        self.name = name

    def GetName(self):
        return self.__name

    def SetName(self, name):
        if name == "Hugo":
            self.__name = "Marvin"
        else:
            self.__name = name

    name = property(GetName, SetName)


x = Robot("Marvin")
y = Robot("Hugo")
print(x.name, y.name)
