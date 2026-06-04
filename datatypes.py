# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two)


mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

max=1909
if max==199:
    print("Amount Mached: %d" %max)
else:
    print("Amount Not mached")

mylist=[]
mylist.append(10)
mylist.append(20)
mylist.append(29)
print(mylist[0])
print(mylist[0:3])

for x in mylist:
    print(+x)
    print(-x)

numbers = [1,2,3]
strings = ["hello","world"]
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = ["Eric"]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

number = 1 + 2 * 3 / 4.0
print(number)

rem = 11 % 3
print(rem)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

x = object()
y = object()

# TODO: change this code
x_list = ([x]*10)
y_list = ([y]*10)
big_list = []
big_list.push(x_list, y_list)
# big_list.insert(y_list)

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
# print(big_list.x)

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")