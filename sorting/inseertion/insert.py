def InsertionSort(new_list):
    for i in range(1, len(new_list)):
        index = i - 1
        temp = new_list[i]

        while index >= 0 and temp < new_list[index]:
            new_list[index + 1] = new_list[index]
            index -= 1

        new_list[index + 1] = temp

    return new_list