#! python3 

# main.py - This is the main script from where all the extra stuff is done

from datetime import date
from datetime import datetime
import json
import pandas as pd
from pandas.core.indexes.base import ensure_index
import bodyCalc
import automation
import progress
import dietCalc

# Format variables
date_format = '%m/%d/%Y'


# Get the current date
today = date.today()
dayOfTheWeek = date.today().weekday()  # Get the current day of the week
# set the date format to m/d/y
dt_string = today.strftime("%m/%d/%y")

# Read In User info json file
f = open('databases/userInfo.json')
userData = json.load(f)
f.close()

# Grab data from userData variable to load local variables
goal = userData['goal']
birthday = datetime.strptime(userData['birthday'], '%m/%d/%Y').date()
currentMacros = userData['macros']
for i in currentMacros:
    print(currentMacros)
# Calculate user's age (for some calorie/BMR rates)
age = (
    today.year
    - birthday.year
    - ((today.month, today.day) < (birthday.month, birthday.day))
)