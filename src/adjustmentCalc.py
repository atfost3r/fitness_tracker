#! python3

# adjustmentCalc.py - this contains all the calculators for adjusting macros depending on goals and progress so far


def cutAdjustment(calories, bmr, weight):
    # remove 100 calories from carbs as long as that doesn't take you below your current weight's BMR
    if calories - 100 >= bmr:
        calories = calories - 100
        carbs = (calories - ((1.2 * weight) / 4 + (0.2 * weight) / 9)) / 4
    else:
        print(
            "You are about as low as recommended.\nGoing any lower might result in some metabolic damange.\nTry staying here and moving a little more."
        )
    return calories, carbs


def bulkAdjustment(calories, weight):
    calories = calories + 100
    carbs = (calories - ((1 * weight) / 4 + (0.4 * weight) / 9)) / 4
    return calories, carbs
