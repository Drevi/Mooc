# Write your solution here

def create_tuple(x: int, y: int, z: int):
    temp = sorted([x , y , z])    
    return (temp[0] , temp[2], sum([x,y,z]))