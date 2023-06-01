def multi_constructor(cls):
    # Get the original __init__ function
    init = cls.__init__
    # Get the parameter names (skip "self")
    params = init.__code__.co_varnames[1:init.__code__.co_argcount]

    # Define a new __init__ function that takes **kwargs
    def new_init(self, **kwargs):
        # Call the old __init__ with the kwargs
        init(self, **{k: kwargs[k] for k in params if k in kwargs})

    # Overwrite the original __init__ function
    cls.__init__ = new_init
    return cls
