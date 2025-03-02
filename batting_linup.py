# This file defines two functions related to players coming to bat in cricket.   

def batsman_arrives(name, age):
    """Prints the basic details of the new batsman. """
    print(f"{name.title()} aged {age} comes to bat. ")


def batsman_takes_stance(position, batting_avg, *career_record):
    """Prints career details of the batsman. """
    print(f"He came at {position} with a batting average of {batting_avg}. ")
    print("His other career details includes the following: ")
    print(f"{career_record}")

    