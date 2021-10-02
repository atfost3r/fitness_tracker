#! python3

# startUp.py - this script is to be run the first time to set up stuff like goal calories, etc.

from types import WrapperDescriptorType
import dietCalc, automation, csv
from datetime import date


# Start and welcome
print("Hey there!\nBefore we get going I have a few questions.")
weight = float(input("OK, first, what is your weight?:\n"))
ans = input("Do you want #GAINZ? (y/n):\n")
if ans == "y":
    [protein_goal, carbs_goal, fat_goal, calories_goal] = dietCalc.bulkMacros(weight)


elif ans == "n":
    ans = input("Do you want #CUTZ? (y/n):\n")
    if ans == "y":
        [protein_goal, carbs_goal, fat_goal, calories_goal] = dietCalc.cutMacros(
            weight, 0.2
        )  # We'll just assume a 20% body fat to start
    else:
        [protein_goal, carbs_goal, fat_goal, calories_goal] = dietCalc.maintMacros(
            weight
        )

print("Your macros to start are:")
print(
    "Calories: {:.0f} \t Protein: {:.0f}\t Carbs: {:.0f}\t Fat: {:.0f}".format(
        calories_goal, protein_goal, carbs_goal, fat_goal
    )
)

ans = input(
    "OK cool. Now that that is out of the way, do you want to take body measurements? (y/n):\n"
)
if ans == "y":
    automation.weeklyUpdate(date.today())


start_Values = {
    "Weight": weight,
    "Protein": protein_goal,
    "Carbs": carbs_goal,
    "Fat": fat_goal,
    "Calories": calories_goal,
}
# start_Values = (weight,protein_goal, carbs_goal, fat_goal, calories_goal)
with open("databases/startPoint.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(start_Values)

print(
    "\nAlright, everything is all set up. Now just run the program each night and update how prompted.\nIf you track everything and update everyday, the program should adjust your macros based on how well you follow and how you're progressing!"
)
print("\n\n\nGood Luck!\n\n\n")


def idealBodyCalc(wrist, waist, knee):
    # This is based on the 'Grecian' ideal from Beyond Bigger Leaner Stronger by Michael Matthews, pg40
    ideal_arm = wrist * 2.5
    ideal_calf = ideal_arm
    ideal_shoulder = waist * 1.618 
    ideal_chest = 6.5 * wrist
    ideal_thigh = 1.75 * knee
    return ideal_arm, ideal_calf, ideal_shoulder, ideal_chest, ideal_thigh