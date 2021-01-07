def columns_spliter(members, columns_number):
    """ Dispach members in 3 lists.
        Split the members list in 3 lists.
        It's use to display 3 columns un web page.
        Input :  Members in list format
        Output:  Dict with many members in list format
    """
    # init destination lists
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column = 1
    # split the memebers list
    print(f"members lengt={len(members)}")
    for member in members:
        if column == 1:
            column1.append(member)
        if column == 2:
            column2.append(member)
        if column == 3:
            column3.append(member)
        if column == 4:
            column4.append(member)
        column += 1
        if column > 4:
            column = 1
    # send results as dict
    dispatch = {
        'column1': column1,
        'column2': column2,
        'column3': column3,
        'column4': column4,
    }
    return dispatch
