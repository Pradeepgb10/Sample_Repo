import math
import sys
import numpy as np
from os import rename
import requests

print(sys.version)
print(sys.executable)

print("********************************")

def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting
