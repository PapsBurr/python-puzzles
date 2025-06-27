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
