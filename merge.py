"""
Function that merges a single row or column in 2048
"""

def merge(line):
    """
    Function that merges a single row or column in 2048
    """
    length = len(line)
    result = [0] * length
    last_index = 0
            
    for current_index in range(length):
        if line[current_index] != 0:
            result[last_index] = line[current_index]
            last_index += 1
    
    for key in range(length - 1):
        if result[key] is result[key + 1]:
            result[key] = result[key] * 2
            result.pop(key + 1)
            result.append(0)
    
    return result