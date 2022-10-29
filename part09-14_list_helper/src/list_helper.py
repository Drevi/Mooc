# WRITE YOUR SOLUTION HERE:

class ListHelper:
        @classmethod
        def greatest_frequency(cls, my_list: list):
            most_freq =  None
            times = 0
            for element in my_list:
                if my_list.count(element) > times:
                    most_freq = element
                    times = my_list.count(element)
            return most_freq

        @classmethod
        def doubles(cls, my_list: list):
            already_found = []
            doubles = 0
            for element in my_list:
                if element not in already_found and my_list.count(element) >= 2:       
                    already_found.append(element)             
                    doubles += 1
            return doubles