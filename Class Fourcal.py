class FourCal:
    def __init__(self, first, second):
        self.first=first
        self.second=second
    def setdata(self, first, second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    
class MoreFourCal(FourCal):
    pass
a=MoreFourCal(4,2)
print(a.add())
