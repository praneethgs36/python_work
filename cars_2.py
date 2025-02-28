def car_details(manufacturer, model, **kwarg):
    kwarg["manufacturer"] = manufacturer
    kwarg["model"] = model
    return kwarg

car = car_details("Tesla", "Model S", color="blue")
print(car)