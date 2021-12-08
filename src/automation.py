#!python3

# automation.py - this script is used to automate the timing and input types that are being done

import bodyCalc, dietCalc, csv


def dailyUpdate(date):  # Create function to do the daily update of data
    # Get user inputs for the day
    print("Updating Fitness log for: ", date)
    weight = float(input("Weight: "))
    calories_actual = float(input("Calories: "))
    protein_actual = float(input("Protein: "))
    carbs_actual = float(input("Carbs: "))
    fat_actual = float(input("Fat: "))
    calories_goal = 2752
    protein_goal = 275
    carbs_goal = 172
    fat_goal = 107
    calories_burnt = float(input("Calories Burnt: "))
    calories_delta = calories_actual - calories_burnt
    dailyFields = (
        date,
        weight,
        calories_actual,
        protein_actual,
        carbs_actual,
        fat_actual,
        calories_goal,
        protein_goal,
        carbs_goal,
        fat_goal,
        calories_burnt,
        calories_delta,
    )
    # write out
    with open("databases/dailyBodyStats.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(dailyFields)
    return weight


def weeklyUpdate(date):

    print("Time to Update your body measurements.\nGrab a tape measure!")
    bicep_r = float(input("Right Bicep (in): "))
    bicep_l = float(input("Left Bicep (in): "))
    forearm_r = float(input("Right Forearm (in): "))
    forearm_l = float(input("Left Forearm (in): "))
    calf_r = float(input("Right Calf (in): "))
    calf_l = float(input("Left Calf (in): "))
    thigh_r = float(input("Right Thigh (in): "))
    thigh_l = float(input("Left Thigh (in): "))
    neck = float(input("Neck (in): "))
    shoulders = float(input("Shoulders (in): "))
    chest = float(input("Chest (in): "))
    waist = float(input("Waist (in): "))
    navy_bodyfat = bodyCalc.bodyFat(
        waist, neck
    )  # calculate body fat percentage with U.S. Navy's formula
    glutes = float(input("Glutes (in): "))
    weeklyFields = (date, bicep_r,bicep_l,forearm_r,forearm_l,calf_r,calf_l,thigh_r,thigh_l, neck, shoulders,chest, waist, navy_bodyfat, glutes)
    with open("src/databases/weeklyBodyStats.csv", "a") as f:
       writer = csv.writer(f)
       writer.writerow(weeklyFields)
    return (
        bicep_l,
        bicep_r,
        forearm_l,
        forearm_r,
        calf_l,
        calf_r,
        thigh_l,
        thigh_r,
        shoulders,
        chest,
        waist,
        navy_bodyfat,
        glutes
    )
