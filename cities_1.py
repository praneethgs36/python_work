prompt = "\nPlease enter the name of the city you have vistited. "
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I would like to visit {city.title()}. ")

