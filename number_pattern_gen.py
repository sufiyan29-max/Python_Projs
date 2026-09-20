# def number_pattern(n):
#     result = ""  # 1. Start with an empty string
    
#     for number in range(1, n + 1):
#         result += f"{number} "  # 2. Append the number and a space
        
#     return result.strip()  # 3. Return and strip the trailing space

# print(number_pattern(4))
# # Output: 1 2 3 4


def number_pattern(n):
    if type(n) != int :
        return "Argument must be an integer value."

    elif n <1 :
        return "Argument must be an integer greater than 0."
    else:

        result = "" 
        
        for number in range(1, n + 1):
            result += f"{number} "  
            
        return result.strip()  

print(number_pattern(4))

