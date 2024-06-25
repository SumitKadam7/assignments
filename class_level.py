class Test:
    total = 0
    def __init__(self):
        Test.increament()

    @classmethod
    def increament(cls):
        cls.total += 1

    @classmethod
    def totalObject(cls):
        return cls.total 


t1 = Test()
t2 = Test()

print(Test.totalObject())
