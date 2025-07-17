## DATA TYPES
# int           45
# float         2.5
# strings      "Hello world"
# Tuple
# Dictionary


## CONCATENATE
a, b, c = 1, 2, "great"

# print ("Value is"+b)
## TypeError: can only concatenate str (not "int") to str ##

## {} = **value** which in this case we have two "value is" and "b"
print ("{} {}" .format("value is", b))

##____________FINDING DATA TYPE_____________##

## FINDING DATA TYPE
print(type(b))

## example

age = 25
height = 5.9
favorite_color = "blue"

## lets print each Variable and their type:
print("Age:",age, "Type:", type(age))
print("Height:",height, "Type:", type(height))
print("Favorite Color:",favorite_color, "Type:", type(favorite_color))

##____________LIST______________##

## PRINT VALUES FROM LIST
values = [1,2,"Tairone", 4, 5]
print(values[2])
print(values[0]) ## values = [1,2,"Tairone", 4, 5]
##                            0 1     2      3  4
## Print between 1-"Tairone"
print(values[0:3])
## Shortcut to print the last value
print(values[-1])

## CHANGE a VALUE
values[2] = "Jessica"
print(values[2])
## now the value "Tairone" changed to "Jessica"

##____________TUPLE______________##

## TUPLE and DICTIONARY
# Data type (same as list data type but immutable)
## TUPLE can't change a variable value like [L,I,S,T]  with []

val = (1, 2, "Tairone", 4, 5)
print(val[2])
## now lets try to change val "Tairone" to "Pedro"
##  command: val[2] = "Pedro"
## lets try to print with:
## print(val[2])
## error: Tuples don't support item assignment!!!

##____________DICTIONARY____________##

## dictionary is a Key-Value Pair form.
x = {21:"first name", 22:"last name", "age":33}

## CHANGE VALUE in Dictionary
x[21] = "tai"
print(x[21])

## you can also mix match like:
y = {"Rahul":25, "Tony":26, "John":"Timmy"}

## ADD VALUE in DICTIONARY
y["Apple"] = "Banana"

print(y)