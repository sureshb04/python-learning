def cal(a,b,c):
    print(a+b)
    print(a-b)
    print("Hi everyone")
    print(c)
    print("           ")
    return print(b*c)
    print(a/c)
cal(2,3,4)

name = 'Infosys'
print (name)
print (name[3],name[-3])
print(name[0:3],name[2:4])
print(name[5:8])
print(name[9:11])
myname= 'suresh reddy'
print(len(myname))
#List
nums=[10,20,30,40,50]
print(nums)
print(nums[2],nums[0:3],nums[0:-3])
bit=['suresh',33,88.8]
print(bit)
mil=[bit,nums]
print(mil)
#append
bit.append(60)
print(bit)
#insert
print(nums)
nums.insert(2,44)
#remove
print(nums)
nums.remove(44)
#pop
print(nums)
nums.pop(1)
print(nums)
#delete
hal=[2,3,4,5]
del hal[0:2]
print(hal)
#extend
run=[4,44,77,99]
run.extend([33,66,88])
print(run)
#minimum value
print(min(run))
#maximum value
print(max(run))
#sum
print(sum(run))
#sort
tell=[33,99,66,22]
print(sorted(tell))
#reverse
tell.sort(reverse=True)
print(tell)
iot=[66,9,4,2,5]
x=iot.count(iot)
print(x)