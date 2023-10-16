#This is a weight converter!

#User is entering their input
weight = input('Weight: ')
unit = input('K(g) or L(lbs): ')

#Runs the "if" statement
#!! REMEMBER to change the input from a string to an integer or float !!
#The ".upper" method is used to indicate whether the input was in lowercase or uppercase
if unit.upper() == 'K':
    kg = float(weight) * 0.45
    print('Kg: ', kg)
elif unit.upper() =='L':
    lbs = float(weight)/0.45
    print('Lbs: ', lbs)
else:
    print('Bad')