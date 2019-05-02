vegetables = ['carrot', 'lettuce', 'onion', 'radish']

def my_function(some_list):
    if len(some_list) == 0:
        print('No items.') 

    if len(some_list) == 1: 
        return (str(some_list[0])+'.')

    if len(some_list) == 2: 
        return (str(some_list[0]) + ' and ' + str(some_list[1]) + '.')

    if len(some_list) >=3: 
        listed = ''
        for i in range(len(some_list[:-1])):
            listed = listed + str(some_list[i]) + ', '
        listed = listed + 'and ' + str(some_list[-1])
        return (listed)

print(my_function(vegetables))


