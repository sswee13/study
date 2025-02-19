#!/usr/bin/env python
# coding: utf-8

# In[93]:


#Функция проверки ввода генерации, положительное число
def input_check1(input_value, value):
    input_value = input()
    while input_value.isdigit() == False:
        print("Вы ввели неверное значение. Введите число!")
        input_value = input()
    value = int(input_value)
    
#Функция проверки ввода мин, макс, натуральное число
def input_check2(input_value, value):
    input_value = input()
    while input_value.lstrip("-").isdigit() == False:
        print("Вы ввели неверное значение. Введите число!")
        input_value = input()
    value = int(input_value)


# In[66]:


#Вычисление положения
def search(list, min, max, x):
    if max >= min:
        
        mid = (max + min) // 2                                #Нахождение центрального элемента

        if list[mid] == x:                                    #Если искомый элемент в центре
            return mid
        elif list[mid] > x:                                   #Если х меньше центрального элемента
            return search(list, min, mid - 1, x)
        else:
            return search(list, mid + 1, max, x)
        
    else:                                                     #Если элемента нет в списке
        return -1


# In[ ]:


import random


# In[112]:


i = 1
list = []

#Ввод значений и создание сортированного списка
print("Сколько необходимо сгенерировать чисел?")
input_value = input()
while (input_value.isdigit() == False) or (int(input_value) == 0):
    print("Вы ввели неверное значение. Введите положительное число!")
    input_value = input()
num_number = int(input_value)

print("От какого значения (минимальное число)?")
input_value = input()
while input_value.lstrip("-").isdigit() == False:
    print("Вы ввели неверное значение. Введите число!")
    input_value = input()
num_min = int(input_value)

print("До какого значения (максимальное число)?")
input_value = input()
while input_value.lstrip("-").isdigit() == False:
    print("Вы ввели неверное значение. Введите число!")
    input_value = input()
num_max = int(input_value)

if (num_min < num_max):
    while (i <= num_number):
        list.append(random.randint(num_min, num_max))
        i += 1
    list = sorted(list)
    print("Созданный список: ", list)
else: print("Максимальное число меньше минимального. Введите верные значения!")


# In[134]:


print("Какое число нужно найти?")
input_value = input()
while input_value.lstrip("-").isdigit() == False:
    print("Вы ввели неверное значение. Введите число!")
    input_value = input()
x = int(input_value)

result = search(list, 0, len(list), x)

if result != -1:
    print("Искомый элемент находится на позиции ", str(result))
else:
    print("Элемента в списке нет")


# In[91]:


print(list)


# In[ ]:




