
# text = "AS12SD25S"


# dict_char_to_int = {'O': '0',
#                     'I': '1',
#                     'J': '3',
#                     'A': '4',
#                     'G': '6',
#                     'S': '5'}

# dict_int_to_char = {'0': 'O',
#                     '1': 'I',
#                     '3': 'J',
#                     '4': 'A',
#                     '6': 'G',
#                     '5': 'S'}


# def license_complies_format(text):
#     """
#     Check if the license plate text complies with the required format.

#     Args:
#         text (str): License plate text.

#     Returns:
#         bool: True if the license plate complies with the format, False otherwise.
#     """
#     if len(text) != 9:
#         return False

#     if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
#        (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
#        (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
#        (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
#        (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
#        (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
#        (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
#        (text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
#        (text[8] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()):
#         return True
#     else:
#         return False



# def format_license(text):
#     """
#     Format the license plate text by converting characters using the mapping dictionaries.

#     Args:
#         text (str): License plate text.

#     Returns:
#         str: Formatted license plate text.
#     """
#     license_plate_ = ''
#     mapping = {0: dict_char_to_int, 1: dict_char_to_int, 4: dict_char_to_int, 5: dict_char_to_int, 6: dict_int_to_char,
#                2: dict_int_to_char, 3: dict_int_to_char, 7: dict_int_to_char, 8: dict_int_to_char}
#     for j in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
#         if text[j] in mapping[j].keys():
#             license_plate_ += mapping[j][text[j]]
#         else:
#             license_plate_ += text[j]

#     return license_plate_





# if license_complies_format(text):
#     print(format_license(text))
# else:
#     print("Invalid License Plate")



import string

dict_char_to_int = {'O': '0',
                    'I': '1',
                    'J': '3',
                    'A': '4',
                    'G': '6',
                    'S': '5'}

dict_int_to_char = {'0': 'O',
                    '1': 'I',
                    '3': 'J',
                    '4': 'A',
                    '6': 'G',
                    '5': 'S'}

def license_complies_format(text):
    """
    Check if the license plate text complies with the required format.

    Args:
        text (str): License plate text.

    Returns:
        bool: True if the license plate complies with the format, False otherwise.
    """
    if len(text) != 9:
        return False
    if (text[0] in string.ascii_uppercase or text[0] in dict_int_to_char.keys()) and \
       (text[1] in string.ascii_uppercase or text[1] in dict_int_to_char.keys()) and \
       (text[2] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
       (text[3] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[3] in dict_char_to_int.keys()) and \
       (text[4] in string.ascii_uppercase or text[4] in dict_int_to_char.keys()) and \
       (text[5] in string.ascii_uppercase or text[5] in dict_int_to_char.keys()) and \
       (text[6] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
       (text[7] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()) and \
       (text[8] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or text[2] in dict_char_to_int.keys()):
        return True
    else:
        return False
    # # Check if the first two characters are alphabets
    # if not text[:2].isalpha():
    #     return False

    # # Check if the next two characters are digits
    # if not text[2:4].isdigit():
    #     return False

    # # Check if the next two characters are alphabets
    # if not text[4:6].isalpha():
    #     return False

    # # Check if the last three characters are digits
    # if not text[6:].isdigit():
    #     return False

    # return True

def format_license(text):
    """
    Format the license plate text by converting characters using the mapping dictionaries.

    Args:
        text (str): License plate text.

    Returns:
        str: Formatted license plate text.
    """
    formatted_text = ""

    for char in text:
        if char in dict_char_to_int:
            formatted_text += dict_char_to_int[char]
        elif char in dict_int_to_char:  # Check for keys, not values
            formatted_text += dict_int_to_char[char]
        else:
            # If the character is neither in dict_char_to_int nor dict_int_to_char keys,
            # it's an invalid character, so replace it with an appropriate mapping or keep it as it is.
            formatted_text += char

    return formatted_text.upper()


# Test the functions
text = "KL12HJ2A2"
if license_complies_format(text):
    print(format_license(text))
else:
    print("Invalid License Plate")
