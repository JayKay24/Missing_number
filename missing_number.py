def find_missing(list_1, list_2):
    """
    This function accepts two lists as arguments which contain positive
    integers and returns the integer absent from both lists.
    """
    # Convert the lists into sets.
    set_1 = set(list_1)
    set_2 = set(list_2)
    
    item = list(set_1 ^ set_2) # Find the symmetric difference between both sets.
    if len(item) == 0:
        return 0
        
    return item[0]