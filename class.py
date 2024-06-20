class character:
  def __init__(self,health,damage,speed):
    self.health = health
    self.damage = damage
    self.speed = speed

sumit = character(100,50,10)
suraj = character(80,40,100)

print(f"sumit speed: {sumit.speed}")
print(f"suraj speed: {suraj.speed}")


