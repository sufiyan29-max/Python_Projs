full_dot = '●'
empty_dot = '○'

def create_character(name,strength,intelligence,charisma):
    if type(name) != str :
        return"The character name should be a string"
    elif len(name) == 0:
        return "The character should have a name"
    elif len(name) > 10 :
        return "The character name is too long"
    elif " " in name :
        return "The character name should not contain spaces"
    elif type(strength) != int or type(intelligence) != int or type(charisma) != int:
        return "All stats should be integers"
    elif min (strength,intelligence,charisma)<1:
        return "All stats should be no less than 1"
    elif max(strength,intelligence,charisma) >4 :
        return "All stats should be no more than 4"
    elif strength + intelligence + charisma != 7 :
        return "The character should start with 7 points"
    else :
        full_dot = '●'
empty_dot = '○'

def create_character(name,strength,intelligence,charisma):
    if type(name) != str :
        return"The character name should be a string"
    elif len(name) == 0:
        return "The character should have a name"
    elif len(name) > 10 :
        return "The character name is too long"
    elif " " in name :
        return "The character name should not contain spaces"
    elif type(strength) != int or type(intelligence) != int or type(charisma) != int:
        return "All stats should be integers"
    elif min (strength,intelligence,charisma)<1:
        return "All stats should be no less than 1"
    elif max(strength,intelligence,charisma) >4 :
        return "All stats should be no more than 4"
    elif strength + intelligence + charisma != 7 :
        return "The character should start with 7 points"
    else:
        str_visual = (full_dot * strength) + (empty_dot * (10 - strength))
        int_visual = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
        cha_visual = (full_dot * charisma) + (empty_dot * (10 - charisma))
        

        return f"{name}\nSTR {str_visual}\nINT {int_visual}\nCHA {cha_visual}"
        

create_character('ren', 4, 2, 1)
