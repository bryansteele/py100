import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()


"""
The code originally was choosing between two list string values, on line 4;
'True' and 'False'.

The strings will always evaluate to a truthy value, hence the if statement
was always truthy.

After removing the ' ' around the list values, True and False became Boolean 
values instead of strings. 

Now the choice is between True and False not truthy and truthy.
"""