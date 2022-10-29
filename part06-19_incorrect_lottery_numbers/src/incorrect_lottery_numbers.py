# Write your solution here

def filter_incorrect():    

    with open("lottery_numbers.csv", 'r') as old_file, open("correct_numbers.csv", 'w') as new_file:
        for line in old_file:
            valid = True            
            parts = line.split(";")
            days = parts[1].strip().split(",")
            try:
                int(parts[0].split(" ")[1])                
            except:
                valid = False
            try:
                for i in range(0, 7):                                      
                    if int(days[i]) < 1 or int(days[i]) > 39 or days[i] in days[i+1:6]:  
                        valid = False
            except:
                valid = False

            if valid:                
                new_file.write(line)


