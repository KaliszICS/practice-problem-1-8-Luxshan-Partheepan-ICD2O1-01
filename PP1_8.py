
def q1():

  _bool1_ = True
  _bool2_ = False

  print(_bool1_ and _bool2_)
  print(_bool1_ or _bool2_)

def q2():

num = input("Enter an integer: ")
show = int(num) != 0  
print(show)


  

def q3():
  
number = float(input("Enter a number: "))
work = 0 <= number <= 10  
math = number > 0 
print(work and math or "Invalid input")



def q4():
  food = input("Input food: ")
  drink = input("Input drink: ")
  pizza_and_pop = (food == "pizza" and drink == "pop")
  print(not pizza_and_pop)


def q5():
  
  noidea = int(input("Enter an integer: "))
  coding = noidea % 2 == 0
  print(f"The integer {noidea} is {coding}.")


#Do not edit code after this
#Comment out the followwing code when running tests

#q1()
#q2()
#q3()
#q4()
#q5()
