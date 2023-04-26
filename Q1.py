def intersection(list1, list2):
    intersection_list = []
    for element in list1:
        if element in list2:
            intersection_list.append(element)

    return intersection_list

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 5, 6, 7]

intersectlist = intersection(list1, list2)
print(intersectlist)
