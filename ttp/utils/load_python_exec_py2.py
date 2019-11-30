def load_python_exec(text_data, builtins=None):
    """
    Function to provide compatibility with python 2.6 for loading text formwatted in 
    python using exec buil-in method. Exec syntaxis in pyton 2.6 different
    comared to python3.x and python3 spits "Invlaid Syntaxis error" while trying to 
    run code below.
    """
    data = {}
    globals_dict = {"__builtins__" : builtins, "_ttp_": _ttp_}
    # below can run on python2.7 as exec is a statements not function for python2.7:
    exec compile(text_data, '<string>', 'exec') in globals_dict, data
    # add extracted functions to globals for recursion to work
    globals_dict.update(data)
    # run eval in case if data still empty as we might have python dictionary or list
    # expressed as string
    if not data:
        data = eval(text_data, None, None)
    return data