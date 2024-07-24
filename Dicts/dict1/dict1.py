def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    result_dict = dict(zip(keys, values))
    return(result_dict)

    pass  # implement me

def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    # update method didn't work
    result = {**d1, **d2}
    return result
    pass  # implement me

def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    #
    new_dict ={key: d1 for key in lst}
    return new_dict

    pass  # implement me

def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    #
    extracted_dict = {}
    for key in keylist:
        if key in datadict:
            extracted_dict[key] = datadict[key]
    return extracted_dict
    
    pass  # implement me

def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    for key in keylist:
        if key in datadict:
            del datadict[key]
    return datadict
    pass

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    return (key in datadict.values())
    pass

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    return (min(ddd, key=ddd.get))
    pass

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    return (max(ddd, key=ddd.get))
    pass