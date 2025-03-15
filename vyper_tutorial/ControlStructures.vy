# @version ^0.3.10

@pure
@external
def sum() -> int128:
    s: int128 = 0
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        s += i
    return s

@pure
@external
def greet(time: String[10]) -> String[20]:
    if time == "morning":
        return "good morning!"
    elif time == "evening":
        return "good evening!"
    else:
        return "how are you?"


    
