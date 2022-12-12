
def area_volume(length, width, height):
    '''
    return area and volume of any object
    '''
    area = length * width
    volume = length * width * height
    return area, volume, length, width

test = area_volume(2,3,4)
print(test)
# print(type(test))

# print(test)
# print(test[0])
# print(test[1])
# print(test[2])
# print(test[3])
# print(test[-1])

# test[0]=8
# print(test)     # tuple unchangeable


test_list = list(test)
# print(test_list)
test_list[0] = 9
# print(test_list)
test_tup = tuple(test_list)
print(test_tup)






fruits = ('apple','banana','cherry')
x, y,xz = fruits

print(y)