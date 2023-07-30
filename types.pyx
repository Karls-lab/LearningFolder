


# Don't use the == for checking if something is a type:
def check_type_equality():
    """
    The "==" operator does not account for subclassing, so 
    it's not recommended. Use isinstance(obj, MyClass)
    """
    x = 5
    if isinstance(x, int):
        print("x is an int")

    """
    If checking if something is None, Ture or False, 
    don't use ==, but "is"
    """
    foo = True
    if foo is True: 
        print(f"Foo is True! :)")

    """
    to iterate over dictionary keys, use for key in d, that
    is the default behavior instead of d.keys()
    """
    example_dict = {'dog': 'bark', 'cat': 'meow'}
    for key in example_dict:
        print(key, end=" ")
        print()

    """
    Here's an easy way to iterate over a dictionary using a
    key/value pair
    """
    for key, val in example_dict.items():
        print(f"key: {key}, value: {val}")

    """
    Use the logging module instead of print 
    """
    import logging
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    logging.debug("debug info")
    logging.info("just some info")
    logging.error("uh oh :(")


check_type_equality()
