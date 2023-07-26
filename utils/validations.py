# Function for check if there's a string or not
def isNonEmptyString(s):
    return isinstance(s, str) and len(s.strip) > 0

