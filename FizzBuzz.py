Number_List = input('please insert the list of Numbers: ')

def FizzBuzz(Numbers):
    RefineNumbers = Number_List.split(',')
    RefineNumbers = sorted([eval(i) for i in RefineNumbers])
    Final_Numbers = ['BuzzFizz' if i % 3 == 0 and i % 5 == 0 
                     else 'Fizz' if i % 3 == 0
                     else 'Buzz' if i % 5 == 0
                     else i for i in RefineNumbers]
    print(Final_Numbers)
    
FizzBuzz(Number_List)