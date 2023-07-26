# Functions for check before validations

# strip() : The method removes any leading, and trailing whitespaces.
# isinstance() : The method ensure that the right input

def isNonEmptyString(s):
    return isinstance(s, str) and len(s.strip) > 0

def isValidTitle(title):
    return isinstance(title, str) and len(title) <= 100

def isValidAuthor(author):
    return isinstance(author, str) and len(author) <= 100


