def puzzle_1(num_list):
    """
    1. Check Nineteen and Five Occurrences

    Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
    Input:
    [19, 19, 15, 5, 3, 5, 5, 2]
    Output:
    True
    Input:
    [19, 15, 15, 5, 3, 3, 5, 2]
    Output:
    False
    Input:
    [19, 19, 5, 5, 5, 5, 5]
    Output:
    True
    """
    nineteen_counter = 0
    five_counter = 0
    for num in num_list:
        match num:
            case 5:
                five_counter += 1
            case 19:
                nineteen_counter += 1
    if five_counter >= 3 and nineteen_counter == 2:
        return True
    return False


def puzzle_2(num_list):
    """
    2. Fifth Element and List Length Check

    Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
    Input:
    [19, 19, 15, 5, 5, 5, 1, 2]
    Output:
    True
    Input:
    [19, 15, 5, 7, 5, 5, 2]
    Output:
    False
    Input:
    [11, 12, 14, 13, 14, 13, 15, 14]
    Output:
    True
    Input:
    [19, 15, 11, 7, 5, 6, 2]
    Output:
    False
    """
    is_len_eight = True
    fifth_element = num_list[4]
    fifth_element_counter = 0
    if len(num_list) != 8:
        return False
    for num in num_list:
        if num == fifth_element:
            fifth_element_counter += 1
    if fifth_element_counter == 3:
        return True
    return False


def puzzle_4(num):
    """
    4. Stone Piles Distribution

    We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.
    Input: 2
    Output:
    [2, 4]
    Input: 10
    Output:
    [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    Input: 3
    Output:
    [3, 5, 7]
    Input: 17
    Output:
    [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
    """
    res_list = []
    for i in range(num):
        res_list.append(num)
        num += 2
    return res_list
















