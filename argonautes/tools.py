def dispatch_members_3_columns(members):
    """ Dispach members in 3 lists.
        Split the members list in 3 lists.
        It's use to display 3 column un web page.
    """
    # init destination lists
    column1 = []
    column2 = []
    column3 = []
    column = 1
    # split the memebers list
    for member in members:
        if column == 1:
            column1.append(member)
        if column == 2:
            column2.append(member)
        if column == 3:
            column3.append(member)
        column += 1
        if column > 3:
            column = 1
    # send results as dict
    dispatch = {
        'column1': column1,
        'column2': column2,
        'column3': column3,
    }
    return dispatch
