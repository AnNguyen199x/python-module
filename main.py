"""
This is a module return the name of module
"""
def principal():
    """
        This is a function to return the module name
    """
    return f"The name of the module: {__name__}"
    # code here
    # anything ...

if __name__ == "__main__":
    print(principal())
