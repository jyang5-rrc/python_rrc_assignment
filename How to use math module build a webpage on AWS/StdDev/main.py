import math

def cal_StdDev(event,context):
    nums = event['nums']
    if len(nums) < 2:
        return 0  # Sample standard deviation is undefined for a single number
    
    mean = sum(nums) / len(nums)
    squared_diff = [(x - mean) ** 2 for x in nums]
    sample_variance = sum(squared_diff) / (len(nums) - 1)
    sample_std_deviation = math.sqrt(sample_variance)
    
    return {
        "nums": nums,
        "standard deviation": sample_std_deviation
    }
