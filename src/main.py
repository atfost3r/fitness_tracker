#! python3

# main.py - This is the main part of the program for fitness universe updating and computing

from datetime import date
import pandas as pd
from pandas.core.indexes.base import ensure_index
import bodyCalc, automation, progress, dietCalc


# Get the current date

today = date.today()
dayOfTheWeek = date.today().weekday()  # Get the current day of the week
# set the date format to m/d/y
dt_string = today.strftime("%m/%d/%y")

# Alex's Birthday
birthday = date(1991, 10, 9)
# Calculate age
age = (
    today.year
    - birthday.year
    - ((today.month, today.day) < (birthday.month, birthday.day))
)

# for now, just put the goal here
goal = "cut"
goal_tolerances = {"Min": 0.0, "Goal": -1.0, "Max": -2.0}

# automatic update logic

## Run daily updates
weight = automation.dailyUpdate(dt_string)
# Calulate progress
progress.progressDaily()

# Weekly update
if dayOfTheWeek == 5:  # Update some stuff on Saturdays
    (
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
    ) = automation.weeklyUpdate(dayOfTheWeek)
    leanWeight, fatWeight = bodyCalc.bodyComp(weight, navy_bodyfat)
    print("Your body fat percentage is: {:2.2f}% ".format(navy_bodyfat * 100))
    print(
        "You you have {:3.2f}  pounds of fat and {:3.2f} pounds of lean mucsle".format(
            leanWeight, fatWeight
        )
    )
    # Check Macro adherence
    df_progress = progress.progressWeekly(dayOfTheWeek)
    [updated_macros] = dietCalc.macroCheck(df_progress, goal_tolerances, goal)

# TODO create JSON form for updating
x = {
    "name": "Alex",
    "birthday": "10/09/1991",
    "goal": "cut",
    "macros": {
        "calories": 2753,
        "protein": 262,
        "carbs": 200,
        "fat": 102
    },
    "bulk": {
        "min": 0.5,
        "max": 1
    },
    "cut": {
        "min": -1,
        "max": -2
    },
    "maxes": {
        "bench": 315,
        "squat": 405,
        "deadlift": 505
    },
    "weight": weight
}