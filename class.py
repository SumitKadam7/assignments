# class character:
# #    def __init__(self,health,damage,speed):
# #     self.health = health
# #     self.damage = damage
# #     self.speed = speed

# # sumit = character(100,50,10)
# # suraj = character(80,40,100)

# # print(f"sumit speed: {sumit.speed}")
# # print(f"suraj speed: {suraj.speed}")
# # sumit.Damage()
# # sumit.Health()

#     def __init__(self,damage):      
#       self.damage = damage    
#       def sumit(self):       
#         def suraj(self):
#           print (f"{self.damage}")                    
#           sumit = damage(100)
#           suraj = damage(80)
#           sumit.damage()
#           suraj.damage()


# def calculate(a, b):
#     return a+b

# print(calculate(1, 2))

class character:
    damage = 0
    power = 100
    kickI = 5
    name = "none"
    def __init__(self, power, name):
      if power > self.power:
          self.power = power
      self.name = name
      return

    def kick(self):
        self.power = self.power + self.kickI
        if self.power > 100:
            self.power = 100
        return self.kickI

    def impact(self, kick):
      self.power = self.power - kick
      if self.power < 0:
          print(f"{self.name} are dead")

    def info(self):
      print(f"charecter :{self.name}")
      print(f"power :{self.power}")
      print(f"kick :{self.kickI}")
      print("------------------------------------------------")
      print()


suraj = character(50, "suraj")
sumit = character(150, "sumit")

print(suraj.power)
print(sumit.power)

kick = suraj.kick()
sumit.impact(kick)

suraj.info()
sumit.info()




# suraj.info()

# charectare : "suraj"
# power : 10
# kick = 10
# -----------------------------------------------


# value = value + 10

# class -> rectangleinfo area prameter
# we need to deteremine properties for these
















