def MIS_X_Statistics(row):
    return row['MIS'] * row['Statistics']

def MIS_X_GPA(row):
    return row['MIS'] * row['GPA']

def GPA_X_Statistics(row):
    return row['GPA'] * row['Statistics']

def AGE_POWER_2(row):
    return row['Age'] * row['Age']

transformersDict = {
    # For Advance_regression.ipynb
    "MIS_X_Statistics": MIS_X_Statistics,
    "MIS_X_GPA": MIS_X_GPA,
    "GPA_X_Statistics": GPA_X_Statistics,
    # For Advance_regression2.ipynb
    "AGE_POWER_2": AGE_POWER_2
}