# Function for check if there's a string or not

# strip() : The method removes any leading, and trailing whitespaces.

def isNonEmptyString(s):
    return isinstance(s, str) and len(s.strip) > 0

def isValidTitle(title):
    return isinstance(title, str) and len(title) <= 100

def isValidAuthor(author):
    return isinstance(author, str) and len(author) <= 100

