"""
RICH COMPARISON
"""
"""
These are the so-called “rich comparison” methods.
The correspondence between operator symbols and method names is as follows:

"""
object.__lt__(self, other)      # x < y calls x.__lt__(y)
object.__gt__(self, other)      # x > y calls x.__gt__(y)

object.__le__(self, other)      # x <= y calls x.__le__(y)
object.__ge__(self, other)      # x >= y calls x.__ge__(y)

object.__eq__(self, other)      # x == y calls x.__eq__(y)
object.__ne__(self, other)      # x != y calls x.__ne__(y)

"""
A rich comparison method may return the singleton NotImplemented 
    if it does not implement the operation for a given pair of arguments. 
By convention, False and True are returned for a successful comparison. 
However, these methods can return any value, 
    so if the comparison operator is used in a Boolean context 
        (e.g., in the condition of an if statement), 
    Python will call bool() on the value to determine if the result is true or false.

By default, object implements __eq__() by using is, 
    returning NotImplemented in the case of a false comparison: 
        True if x is y else NotImplemented. 
        
        For __ne__(), by default it delegates to __eq__() and inverts the result unless it is NotImplemented. 
        There are no other implied relationships among the comparison operators or default implementations; 
        for example, the truth of (x<y or x==y) does not imply x<=y. 
        To automatically generate ordering operations from a single root operation, 
            see functools.total_ordering().

See the paragraph on __hash__() for some important notes on creating hashable objects 
    which support custom comparison operations and are usable as dictionary keys.

There are no swapped-argument versions of these methods 
    (to be used when the left argument does not support the operation but the right argument does); rather, 
        __lt__() and __gt__() are each other’s reflection, 
        __le__() and __ge__() are each other’s reflection,
        __eq__() and __ne__() are their own reflection. 
        
    If the operands are of different types, 
        and the right operand’s type is a direct or indirect subclass of the left operand’s type, 
        the reflected method of the right operand has priority, 
        otherwise the left operand’s method has priority. 
        Virtual subclassing is not considered.
"""
