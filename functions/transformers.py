def MIS_X_Statistics(row):
    return row['MIS'] * row['Statistics']

def MIS_X_GPA(row):
    return row['MIS'] * row['GPA']

def GPA_X_Statistics(row):
    return row['GPA'] * row['Statistics']

transformersDict = {
    "MIS_X_Statistics": MIS_X_Statistics,
    "MIS_X_GPA": MIS_X_GPA,
    "GPA_X_Statistics": GPA_X_Statistics
}