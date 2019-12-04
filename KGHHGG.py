import random
import datetime
import prettytable                  # пакет для таблицы

def selection_sort(nums):
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


def insertion_sort(nums):
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for fst in range(1, len(nums)):
        item_to_insert = nums[fst]
        # Сохраняем ссылку на индекс предыдущего элемента
        lst = fst - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while lst >= 0 and nums[fst] > item_to_insert:
            nums[lst + 1] = nums[lst]
            lst -= 1
        # Вставляем элемент
        nums[lst + 1] = item_to_insert


table = prettytable.PrettyTable(["Размер списка", "Время Выборки", "Время Вставками"])
x=[]
y1=[]
y2=[]



for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    nums=[]
    for i in range (N):
        nums.append(int(round(random.random()*(max-min)+min)))

    #print(A)

    B = nums.copy()
    # print(B)

    # выборка(A)
    print("---")
    # print(A)


    # вставками(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    selection_sort(nums)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Выборка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    insertion_sort(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Вставками   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds())])
print(table)
