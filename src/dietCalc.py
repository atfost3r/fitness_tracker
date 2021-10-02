#!python3

# dietCalc.py - this subroutine will take current body stats and and calculate the calories, protein, carbs and fat that should be the goal

import adjustmentCalc


def harris_benedict(weight, height, age):
    BMR = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
    return BMR


def bulkMacros(weight):
    # This portion is from 'Bigger Leaner Stronger' by Michael Matthews
    protein = round(weight)  # 1 gram of protein per pound of body
    carbs = 2 * round(weight)  # 2 grams of carbs per pound of body weight
    fat = round(0.4 * weight)
    calories = 4 * (protein + carbs) + (
        9 * fat
    )  # calculate total calories where fat = 9 cals/gram, protein and carbs are 4 cals/gram
    return protein, carbs, fat, calories


def cutMacros(weight, bodyFat):
    # This portion is from 'Bigger Leaner Stronger' by Michael Matthews
    if (
        bodyFat >= 0.25
    ):  # if body fat is higher than 25% then the calculation is slightly different
        protein = round(0.8 * weight)  # 1 gram of protein per pound of body
        carbs = 2 * round(0.6 * weight)  # 2 grams of carbs per pound of body weight
        fat = round(0.3 * weight)

    else:
        protein = round(1.2 * weight)  # 1
        carbs = round(weight)
        fat = round(0.2 * weight)
    calories = 4 * (protein + carbs) + (
        9 * fat
    )  # calculate total calories where fat = 9 cals/gram, protein and carbs are 4 cals/gram
    return protein, carbs, fat, calories


def maintMacros(weight):
    protein = round(1 * weight)  # 1
    carbs = round(1.6 * weight)
    fat = round(0.35 * weight)
    calories = 4 * (protein + carbs) + (
        9 * fat
    )  # calculate total calories where fat = 9 cals/gram, protein and carbs are 4 cals/gram
    return protein, carbs, fat, calories


def refeedMacros(calories, weight):
    protein = round(weight)
    fat = 20  # as little as possible, shoot for <20g of fat
    carbs = (calories - ((4 * protein) + (9 * fat))) / 4
    return protein, carbs, fat


def carbCycling(weight, height, age):
    bmr = harris_benedict(weight, height, age)
    tdee = 1.35 * bmr
    weekly_target = 7 * tdee
    # Calculate rest day value
    restday_cals = bmr
    restday_protein = (bmr * 0.45) / 4
    restday_carbs = (bmr * 0.25) / 4
    restday_fat = (bmr * 0.3) / 9

    training_cals = (weekly_target - (2 * restday_cals)) / 5
    training_protein = round(weight)
    training_fat = (training_cals * 0.2) / 9
    training_carbs = (training_cals - (training_protein * 4) + (training_fat * 9)) / 4

    return (
        restday_cals,
        restday_carbs,
        restday_fat,
        restday_protein,
        training_cals,
        training_protein,
        training_carbs,
        training_fat,
    )


def macroCheck(df_progress, goal_tolerances, goal):
    cal_delta = df_progress["calories_weekly_delta"].iloc[-1]
    weight_delta = df_progress["weight_weekly"].iloc[-1]

    # TODO check if you're moving in the right direction
    if goal == "cut" and weight_delta < goal_tolerances.get("Min"):
        if weight_delta > goal_tolerances.get("Max") and cal_delta > 500:
            print(
                "You'll need to get your calories in line.\nWe'll keep them the same this week."
            )
        else:
            calories, carbs = adjustmentCalc.cutAdjustment()
    return calories, carbs  # protein, fat, carbs
