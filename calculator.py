def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
      print("error!!, not divisable")
      return None
    else:
      return x / y
def calculator():
       print("operation choice")
       print("(1). add")
       print("(2).subtract")
       print("(3). multiply")
       print("(4). divide")

       choice = input("choose operation:  ")
       while True:
        if choice in ('1', '2', '3', '4'):
            first_num = int(input("first number: "))
            second_num = int(input("second number: "))
            if choice == '1':
              print("Result:", add(first_num, second_num))
            elif choice == '2':
              print("Result:", subtract(first_num, second_num))
            elif choice == '3':
              print("Result:", multiply(first_num, second_num))
            elif choice == '4':
              print("Result:", divide(first_num, second_num))
        else:
          print("Invalid choice!")
          pass
        user = input("do you want to run another operation? ('YES') or ('NO'):  ")
        if user.upper() == 'YES':
           return calculator()
        else:
         break

calculator()



    
          

    
