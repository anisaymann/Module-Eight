
def multiple_output(a,b):
    add = a+b
    subs = a-b
    mult = a*b
    return add, subs, mult

print(multiple_output(5,2))
# x,y = multiple_output(5,2)
# print(x,y)

# x = multiple_output(5,2)
# print(x)
# print(type(x))


# x,y = multiple_output(5,2)
# print(x)
# print(y)


x,y,z = multiple_output(5,2)
print(x)
print(y)
print(z)