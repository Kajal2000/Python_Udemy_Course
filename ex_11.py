def func_0(arr_1, arr_2):
    pass
    i = 0
    num = []
    while i <len(arr_1):
        if arr_1[i] < arr_2[i]:
            a = arr_1[i]
            num.append(a)
        else:
            b = arr_2[i]
            num.append(b)
        i = i + 1
    return(num)
print(func_0([5,9,3],[2,16,4]))
# 
def func_1(arr_1, arr_2):
    pass
    new_arr1 =  sorted(arr_1)
    new_arr2 = sorted(arr_2)
    return (func_0(new_arr1,new_arr2))
print(func_1([6,3,9],[11,2,4]))

def func_2(my_string):
    pass
    s = '->'
    return (s.join(my_string))
print(func_2("hello."))
