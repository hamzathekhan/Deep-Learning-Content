##Duck Typing : If an object can do same thing as other then it must of same type as other, even if it is declared as a different entity.
## In simpe term . If it walk and quack like a duck it is duck.


def fly(bird):
  bird.fly()

class Duck():
  def fly(self):
    print("Duck can fly")

class Eagle():
  def fly(self):
    print("Eagle can fly")


duck = Duck()
eagle = Eagle()

fly(duck)   # Output : "Duck can fly"
fly(eagle)   # Output : "Eagle can fly"
