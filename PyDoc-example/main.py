"""
This example module shows various types of documentation available for use with pydoc.  
To generate HTML documentation for this module issue the command:

    pydoc -w bar
"""

def bar(baz):
    """
    Prints baz to the display.
    """
    print(baz)

if __name__ == '__main__':
    bar("hello world")
