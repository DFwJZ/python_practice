import copy
import sys

def demonstrate_float_object_creation():
    a = [1, [2, 3e19], 4]
    deep_copy = copy.deepcopy(a)
    
    print("Original:")
    print("a =", a)
    print("ID of a[1][1]:", id(a[1][1]))
    
    print("\nDeep copy:")
    print("deep_copy =", deep_copy)
    print("ID of deep_copy[1][1]:", id(deep_copy[1][1]))
    
    # Modify the deep copy
    deep_copy[1][1] = 6
    print("\nAfter deep_copy[1][1] = 6:")
    print("deep_copy =", deep_copy)
    print("ID of deep_copy[1][1]:", id(deep_copy[1][1]))
    
    # Change to a significantly different large float
    deep_copy[1][1] = 3.1e19
    print("\nAfter changing to 3.1e19:")
    print("deep_copy =", deep_copy)
    print("ID of deep_copy[1][1]:", id(deep_copy[1][1]))
    print("ID of a[1][1]:", id(a[1][1]))
    
    # Force creation of a new float object with a slightly different value
    deep_copy[1][1] = 3e19 + sys.float_info.epsilon
    print("\nAfter changing to 3e19 + sys.float_info.epsilon:")
    print("deep_copy =", deep_copy)
    print("ID of deep_copy[1][1]:", id(deep_copy[1][1]))
    print("ID of a[1][1]:", id(a[1][1]))
    
    # Another way to force new object creation
    deep_copy[1][1] = float.fromhex('0x1.5f8a1d891d91p+66')  # Approximately 3e19
    print("\nAfter changing to float.fromhex('0x1.5f8a1d891d91p+66'):")
    print("deep_copy =", deep_copy)
    print("ID of deep_copy[1][1]:", id(deep_copy[1][1]))
    print("ID of a[1][1]:", id(a[1][1]))

    deep_copy[1][1] = 3e19
    print("\nAfter changing back to 3e19'):")
    print("deep_copy =", deep_copy)
    print("ID of deep_copy[1][1]:", id(deep_copy[1][1]))
    print("ID of a[1][1]:", id(a[1][1]))
demonstrate_float_object_creation()