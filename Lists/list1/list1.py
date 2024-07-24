from xml.dom.expatbuilder import parseString


## Think SLICING for many of these.

def create_list_from_tuple(t):
    """
    This function takes a tuple of elements and returns a list containing those elements of the tuple.
    """
    return list(t)
    pass  # implement me
    
def drop_last(lst):
    """
    This function takes a list and returns a list with the last item removed.
    """
    # use pop?
    # return lst.pop()?
    lst.pop()
    # don't return pop()
    return lst
    pass  # implement me
    pass  # implement me


def drop_first_two(lst):
    """
    This function takes a list and returns a list with the first two items removed.
    """
     # del twice
    del lst[0]
    # del lst[1]
    del lst[0]
    return lst
    pass  # implement me
    pass  # implement me

def drop_mangle(lst):
    """
    This function takes a list and returns a list with the first two items AND last item removed.
    """
    # pop last
    lst.pop()
    # del
    del lst[0]
    # del lst[1] shifted?
    del lst[0]
    return lst
    pass  # implement me
    pass  # implement me

def add_item_front(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item prepended to the list
    """
    lst.insert(0,a)
    return lst
    pass  # implement me

def add_item_end(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item appended to the list
    """
    lst.insert(len(lst),a)
    return lst
    pass  # implement me

def add_list_to_list(lsta, lstb):
    """
    This function takes two lists and appends one to the other,
    returning a list
    """
    two_listst = lsta + lstb
    return two_listst
    pass  # implement me

def list_and_list_to_tuple(lsta, lstb):
    """
    This function takes two lists and returns a tuple containing the two lists
    """
    tuple_of_lists = (lsta, lstb)

    return tuple_of_lists
    pass # implement me

def list_and_list_to_list(lsta, lstb):
    """
    This function takes two lists and returns a list containing the two lists
    """
    lists_of_lists = []
    lists_of_lists.append(lsta)
    lists_of_lists.append(lstb)
    return lists_of_lists
    pass # implement me

##
##
##

def list_from_range(n):
    """
    This function returns list with 0..n as integers in a list
    """
    list_range_n =[*range(0,n)]
    return list_range_n
    pass # implement me

def list_from_range2(n, m):
    """
    This function returns list with n..m (without m) as integers in a list
    """
    list_range_n2m =[*range(n,m)]
    return list_range_n2m
    pass # implement me

def list_from_range3(n, m):
    """
    This function returns list with n..m (including m(!)) as integers in a list
    """
    list_range_n2m =[*range(n,m+1)]
    return list_range_n2m
    
    pass # implement me

def list_from_range4(n, m):
    """
    This function returns list with n..m (WITHOUT n and including m) as integers in a list
    """
    list_range_n2m =[*range(n+1,m+1)]
    return list_range_n2m
    pass # implement me

def list_from_range_by(n, step):
    """
    This function returns list with 0..n as integers by step in a list
    (read the test)
    """
    list_range_step =[*range(0,n,step)]
    return list_range_step
    pass # implement me


def rev_list(lst):
    """
    This function returns list which is a reverse of the argument list
    (read the test)
    """
    rev_list = lst[::-1]
    return rev_list
    pass # implement me
  
def concat_list_indexwise(lst1, lst2):
    """
    Write a program to add two lists index-wise. 
    Create a new list that contains the 0th index item from both the list, 
    then the 1st index item, and so on till the last element. 
    Any leftover items will get added at the end of the new list.
    """
    # concat_list =[index + x for index, x in zip(lst1, lst2)]
    #find length of shorter list
    min_len = min(len(lst1), len(lst2))
    concat_list_indexwise = [lst1[i] + lst2[i] for i in range(min_len)]

    if len(lst1) > len(lst2):
        concat_list_indexwise.extend(lst1[min_len:])
    else:
        concat_list_indexwise.extend(lst2[min_len:])

    return concat_list_indexwise
    #parseString # implement me

def square_each_item(lst):
    """
    This function returns list which each item in argument list has been squared
    (read the test)
    """
    return [x ** 2 for x in lst]
    pass # implement me

def remove_empty_strs(lst):
     """
     Remove empty strings from the list of strings
     """
     filtered_list = list(filter(None,lst))
     return filtered_list
     pass
    


def remove_item_from(lst, aaa):
    """
    Remove all occurrences of a specific item from a list.
    """
    filtered_list = [x for x in lst if x != aaa]
    return filtered_list
    pass

def leave_item_in(lst, aaa):
    """
    Leave all occurrences of a specific item in a list.
    """

    filtered_list = [x for x in lst if x == aaa]
    return filtered_list
    pass

def length_of(lst):
    """
    return the length of the list
    """
    return len(lst)
    pass