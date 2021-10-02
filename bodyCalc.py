#! python3

# bodyCalc.py - Here we calculate the various data bits for the entry

import math


def bodyFat(waist, neck):
    navy_bodyfat = (
        495 / (1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(75))
        - 450
    ) / 100
    return navy_bodyfat  # returns the body fat in %


def bodyComp(weight, bodyFat):
    leanWeight = weight * (1 - bodyFat)
    fatWeight = weight * bodyFat

    return leanWeight, fatWeight
