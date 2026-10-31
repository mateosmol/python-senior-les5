# print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")
#
# try:
#     print("Hello")
#     print(error)
#     print("Hello")
# except:
#     print("broo you made a mistake")
#
# try:
#     print(10 / 0)
# except NameError:
#     print("NameError bro")
# except ZeroDivisionError as error:
#     print("How it could even be a NameError are you serious, it's definitely", error)
#
# try:
#     print("Hello")
# except NameError as error:
#     print(error,", would you look at that")
# else:
#     print("It's okay")
# finally:
#     print("Why do I even need this part?")
#
# def checker(var_1):
#     if type(var_1) != str:
#         raise TypeError(f"We can't work with the {type(var_1)}, we need str")
#     else:
#         return var_1
#
# checker(2)
#
# class BuildingError(Exception):
#     def __str__(self):
#         return "Not enough materials GIMME MOREEE"
#
# def check_materials(amount, maximum):
#     if amount >= maximum:
#         return "Can be built"
#     else:
#         raise BuildingError
#
# check_materials(5, 7)

import warnings

warnings.warn("я тебе хочу попередити що це попередження", SyntaxWarning)
