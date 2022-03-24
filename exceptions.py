# BROAD REASONS WHY YOU MIGHT GET AN EXCEPTION
# (1) Trying to refer to something that doesn't exist
# (2) Using a value that is inappropriate in some way

# CORE EXAMPLES OF EXCEPTIONS IN THIS FILE
# AttributeError (1)
# KeyError (1)
# IndexError (1)
# NameError (1)
# UnboundLocalError (1)
# TypeError (2)
# ValueError (2)
# ZeroDivisionError (2)
# OverflowError (2)
# FileNotFoundError (1)
# UnicodeEncodeError (2)
# ModuleNotFoundError (1)
# ImportError (1)

# BONUS EXAMPLES YOU CAN TRY IF YOU WISH
# PermissionError (2)
# IsADirectoryError (2)


# AttributeError - EXAMPLE
def produce_attribute_error():
    print(1.234.upper())
    pass

# KeyError
def produce_key_error():
    dictionary = {
        1: "a",
        2: "b"
    }
    x = dictionary["c"]
    pass

# IndexError
def produce_index_error():
    a = [1, 2, 3, 4, 5]
    print(a[5])
    pass

# NameError
def produce_name_error():
    print(x)
    pass

# UnboundLocalError
def produce_unbound_local_error():
    carrots = 7
    rabbits = 7
    if carrots > rabbits:
        amount = "Too many carrots"
    elif carrots < rabbits:
        amount = "Not enough carrots"
    print(amount)
    pass

# TypeError
def produce_type_error():
    multiply_string = "a" * "b"
    pass

# ValueError
import math

def produce_value_error():
    number = math.sqrt(-2)
    pass

# ZeroDivisionError
def produce_zero_division_error():
    devision = 4 / 0
    pass

# OverflowError
def produce_overflow_error():
    big_float = 324092349023940923.3900934209234092309
    big_float** 8322128399821398129839849834298239489823982983298329839032
    pass

# FileNotFoundError
def produce_file_not_found_error():
    open("lalala.txt", "r")
    pass

# UnicodeEncodeError
def produce_unicode_encode_error():
    u = chr(40960) + 'abcd' + chr(1972)
    u.encode('ascii')
    pass

# ModuleNotFoundError
# import emma
def produce_module_not_found_error():
    import emma
    pass

# ImportError
def produce_import_error():
    from . import a
    pass
