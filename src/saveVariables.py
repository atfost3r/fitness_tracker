#! python

# saveVariables.py - this is a funtion that will save off the relevant storage variables from use next session

import pickle

# obj0, obj1, obj2 are created here...

# Saving the objects:
with open("objs.pkl", "w") as f:  # Python 3: open(..., 'wb')
    pickle.dump([obj0, obj1, obj2], f)

# Getting back the objects:
with open("objs.pkl") as f:  # Python 3: open(..., 'rb')
    obj0, obj1, obj2 = pickle.load(f)
