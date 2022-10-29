# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    code = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    century_marker = "+-A"   

    if len(pic) != 11:
        return False
    if pic[6] not in century_marker:
        return False

    try:
        century = 20
        if pic[6] == "+":
            century = 18
        elif pic[6] ==  "-":
            century = 19   
        dob = datetime(century+ int(pic[4:6]), int(pic[2:4]), int(pic[0:2]))
    except:
        return False

    if pic[10] != code[int(pic[0:6] + pic[7:10]) % 31] :
        return False
        
    return True
