def calculateSum(list_data):
    total = 0
    if list_data.__len__() == 0:
        return 0
    else:
        for i in list_data:
            total += i
    return total


def calculateProduct(list_data):
    total = 1
    if list_data.__len__() == 0:
        return 1
    else:
        for i in list_data:
            total *= i
    return total


def calculateAverage(list_data):
    total = 0
    if list_data.__len__() == 0:
        return 'Nan'
    else:
        for i in list_data:
            total += i
        return total/list_data.__len__()


def calulateMedian(list_data):
    index = 0
    list_data.sort()
    if list_data.__len__() == 0:
        return 'None'
    elif list_data.__len__() % 2 == 1:
        index = (list_data.__len__()//2)
        return list_data[index]
    elif list_data.__len__() % 2 == 0:
        index = (list_data.__len__()//2)
        return (list_data[index] + list_data[index-1])/2


def calculateMode(list_data):
    mode_count = 0
    number = 0
    if list_data.__len__() == 0:
        return 'None'
    else:
        for x in list_data:
            count = list_data.count(x)
            if count > mode_count:
                mode_count = count
                number = x
    return number


if __name__ == '__main__':
    print(calculateSum([]) == 0)
    print(calculateSum([2,4,6,8,10]) == 30)
    print(calculateProduct([]) == 1)
    print(calculateProduct([2, 4, 6, 8, 10]) == 3840)
    print(calculateAverage([1,2,3]) == 2)
    print(calculateAverage([1,2,3,1,2,3,1,2,3]) == 2)
    print(calculateAverage([12,20,37]) == 23)
    print(calculateAverage([0,0,0,0]) == 0)
#   print(calculateAverage([]))
    print(calulateMedian([]) == 'None')
    print(calulateMedian([1,2,3]) == 2)
    print(calulateMedian([3,7,10,4,1,9,6,5,2,8]) == 5.5)
    print(calulateMedian([3,7,10,4,1,9,6,2,8]) == 6)
    print(calculateMode([]) == 'None')
    print(calculateMode([1,2,3,4,4]) == 4)
    print(calculateMode([1,1,2,3,4]) == 1)

