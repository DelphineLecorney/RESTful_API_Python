from flask import jsonify, request

# Functions for check before validations

# strip() : The method removes any leading, and trailing whitespaces.
# isinstance() : The method ensure that the right input

def isNonEmptyString(s):
    return isinstance(s, str) and len(s.strip) > 0

def isValidTitle(title):
    return isinstance(title, str) and len(title) <= 100

def isValidAuthor(author):
    return isinstance(author, str) and len(author) <= 100

def confirmDelete(message, delete_callback):
    confirm = request.args.get('confirm')
    if not confirm or confirm.lower() != 'true':
        return jsonify({'message': message, 'confirm_delete': True})
    
    return delete_callback()

