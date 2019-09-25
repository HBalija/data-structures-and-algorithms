def selection_sort(lst):

    for el in enumerate(lst):
        minimum = el[0]
        for item in enumerate(lst[(minimum + 1) :], el[0] + 1):  # noqa
            if item[1] < lst[minimum]:
                minimum = item[0]
        if minimum != el[0]:
            lst[el[0]], lst[minimum] = lst[minimum], lst[el[0]]

    return lst


print(selection_sort([6, 4, 15, 10]))  # [ 4, 6, 10, 15 ]
print(selection_sort([7, 1, 2, 3, 4, 5, 6, 8]))  # [1, 2, 3, 4, 5, 6, 7, 8]
