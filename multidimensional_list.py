"""This module contains a set of utily functions to work with multidimensional lists"""


def filter_list(function, items):
    """
    This function will filter a multidimensional list

    Parameters:
        function (fun): The function for filtering
        items (list): List of items to filter

    Returns:
        list: A new list with filtered items

    """
    new_list = []
    for i in items:
        if isinstance(i, list):
            new_list.append(filter_list(function, i))
        else:
            if function(i):
                new_list.append(i)
    return new_list


def map_list(function, items):
    """
    This function maps multidimensional lists
    
    Parameter:
    function (func): The function to apply
    items (list): The list of items to map

    Returns:
    list: A new mappend list
    """
    new_list = []
    for i in range(len(items)): # pylint: disable=consider-using-enumerate
        if isinstance(items[i], list):
            new_list.append(map_list(function, items[i]))
        else:
            new_list.append(function(items[i]))
    return new_list
