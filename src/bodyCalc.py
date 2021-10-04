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

def idealBodyCalc(wrist, waist, knee):
    # This is based on the 'Grecian' ideal from Beyond Bigger Leaner Stronger by Michael Matthews, pg40
    ideal_arm = wrist * 2.5
    ideal_calf = ideal_arm
    ideal_shoulder = waist * 1.618 
    ideal_chest = 6.5 * wrist
    ideal_thigh = 1.75 * knee
    return ideal_arm, ideal_calf, ideal_shoulder, ideal_chest, ideal_thigh