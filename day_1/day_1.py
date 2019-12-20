import math
with open('input.txt', 'r') as f:
    puzzle_input = f.readlines()

puzzle_input = [inpute.strip('\n') for inpute in puzzle_input]
print(puzzle_input)
sum = 0
for mass in puzzle_input:
   fuel = math.floor(int(mass)/3) - 2
   print('Mass of the input was ' + str(mass) + '. The fuel needed is:' + str(fuel))
   sum = sum + fuel
   add_sum= 0
   while fuel > 0:
       add_fuel = max(math.floor(fuel/3) - 2, 0)
       print('Additional fuel requiered for ' +str(fuel)+ ' of fuel is: ' +str(add_fuel))
       fuel = add_fuel
       print('Now calculating how much additional fuel is needed for ' +str(fuel))

       add_sum = add_sum + add_fuel
   sum = sum+add_sum
   print('Total is now:', sum)

   print( '=====================================')



## PART 2