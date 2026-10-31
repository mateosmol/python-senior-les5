from typing import final


class PostaravsaPodilytNaNulError(Exception):
    def __str__(self):
        return "Nasho ty dilysh na nul yakscho ty sam znayesh shcho tak ne mozhshna?"

try:
    numerator = int(input("Vvedit chyselnyk "))
    denominator = int(input("Vvedit znamennyk "))
    result = numerator/denominator
    print(result)
except ZeroDivisionError:
    raise PostaravsaPodilytNaNulError
else:
    print("narmaldy")