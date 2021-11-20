# Ex 4: Any type of BaseException or inherit from that.All type of errors
try:
    pass
except:
    print("Any type of BaseException or inherit from that.All type of errors")

# Ex 5
# Reasons it's not a good idea:
# 1. It catches all types of errors,
# include those the program is not expected to handle
# Thus it is recommended to be more specific
try:
    pass
except:
    pass

# 2. if there are several excepts, this will hide all the other excepts that follows it.
# In the example bellow ValueError and ZeroDivisionError will never be caught
# Hence we get error- unreachable code
try:
    pass
except:
    pass
except ValueError:
    pass
except ZeroDivisionError:
    pass