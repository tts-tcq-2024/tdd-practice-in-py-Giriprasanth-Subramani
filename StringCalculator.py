import re

def check_negatives(numbers):
     for value in numbers:
         try:
             if value.startswith('-'):                 
                 raise ValueError(f"Negatives not allowed: {value}")                 
         except ValueError as e:
            print(e)
          
        
def generate_number_list(input):    
        numbers = re.findall(r'-\d+', input)
        if not numbers:
            numbers = re.findall(r'\d+', input)
        else:
            numbers = check_negatives(numbers)
            
        return numbers
    
def add(input):
    
    numbers = generate_number_list(input)   
    number_list = []
    for number in numbers:
        if int(number) < 1000:
            number_list.append(int(number))
    return sum(number_list)
  
    
  
