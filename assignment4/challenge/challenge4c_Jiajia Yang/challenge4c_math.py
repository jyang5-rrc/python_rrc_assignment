import math

class MyMath (): 
    '''This class contains methods for calculating the average and standard deviation of a list of numbers'''   
    
    def __init__(self, *args):
        '''This function initializes the MyMath class'''
        if args:
            self.num_list = list(args)
        else:
            self.num_list = []
    
    def avg(self):
        '''This function calculates the average of a list of numbers'''
        if self.num_list == []:
            return 0  # Average is undefined for an empty list
        
        avg = sum(self.num_list) / len(self.num_list)
        return avg
    
    def stdDev(self):
        '''This function calculates the standard deviation of a list of numbers'''
        if len(self.num_list) < 2:
            return 0  # Sample standard deviation is undefined for a single number
        
        mean = sum(self.num_list) / len(self.num_list)
        squared_diff = [(num - mean) ** 2 for num in self.num_list]
        sample_variance = sum(squared_diff) / (len(self.num_list) - 1)
        sample_std_deviation = math.sqrt(sample_variance)
        
        return sample_std_deviation
    

def getNums():
    '''This function prompts the user for a list of numbers, and returns a tuple of the numbers'''
    num_list = []
    nums = input("Enter a list of numbers, separated by spaces:").split()
    for num in nums:
        #check if num is a number
        try:
            # Try to convert the input to a float
            num_value = float(num)
            num_list.append(num_value)
        except ValueError:
            print("Invalid input. Please enter a list of numbers, separated by spaces.")
            return getNums()
            
    return tuple(num_list)

def main():
    '''This function calculates the average and standard deviation of a list of numbers'''
    num_list = getNums()
    my_math = MyMath(*num_list)
   
    print("Average:", my_math.avg())
    print("Standard Deviation:", my_math.stdDev())

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    