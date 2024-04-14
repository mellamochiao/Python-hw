def max_water_units(heights):
    n = len(heights)
    if n <= 2:
        return 0
    
    left_max = [0] * n
    right_max = [0] * n
    
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], heights[i])
    
    right_max[n-1] = heights[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i])
    
    water_units = 0
    for i in range(n):
        water_units += max(0, min(left_max[i], right_max[i]) - heights[i])
    
    return water_units

# Example usage:
heights = [5,0,3,4,5,6,0,1,2,0,1,0,4]
print("Maximum units of water that can be trapped:", max_water_units(heights))
