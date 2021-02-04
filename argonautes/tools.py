def columns_spliter(data_source, columns_number):
    """ Dispach members in 3 lists.
        Split the members list in 3 lists.
        It's use to display 3 columns un web page.
        Input :  Members in list format
        Output:  Dict with many members in list format
    """
    # init destination lists
    # init dispatch (dict)
    dispatch = {}
    for num in range(1, columns_number + 1):
        dispatch[f"column{num}"] = []
    # split the memebers list
    index = 1
    for data in data_source:
        dispatch[f"column{index}"].append(data)
        if index >= columns_number:
            index = 0
        index += 1
    # send results as dict
    return dispatch
