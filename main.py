#Fill in the contents of the is_old_enough_to_drink function. This function takes in a number, called age, and returns whether a person of this age old enough to legally drink in the United States. If the person is old enough to drink, the function should return True. If they are not old enough to drink in the united states, the function should return False. Notes:
#The legal drinking age in the United States is 21

# output = is_old_enough_to_drink(22)
# print(output) # --> True

def is_old_enough_to_drink(age):
  if age>=21:
    return True
  else:
    return False

print(is_old_enough_to_drink(20))

