# def find_6(list1):
#     for i in range (len(list1)):
#       if list1[i] == 6:
#             return " 6 Индексі списте:",i
# print(find_6(list1=[5,8,8,5,8,9,5,4,6,5,1,7]))

def find_6(list1):
    index = 0
    for i in list1:
        if i == 6:
            return "6 Индексі списте:", index
        index += 1
    return "6 не знайдено"
    
print(find_6(list1=[5,8,8,5,8,9,5,4,5,1,7]))


