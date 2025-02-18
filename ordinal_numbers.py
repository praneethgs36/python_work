ord_nums = [num for num in range(1, 10)]

for number_ in ord_nums:
    if number_ == 1:
        ordinal = f"{number_}st"
    elif number_ == 2:
        ordinal = f"{number_}nd"
    elif number_ == 3:
        ordinal = f"{number_}rd"
    else:
        ordinal = f"{number_}th"
    print(ordinal)