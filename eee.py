def max_water_units(heights):
    n = len(heights)
    if n <= 2:
        return 0
    
    left_max = [0] * n
    right_max = [0] * n
    
    left_max[0] = heights[0]
    i = 1
    while i < n:
        left_max[i] = max(left_max[i-1], heights[i])
        i += 1
    
    right_max[n-1] = heights[n-1]
    i = n - 2
    while i >= 0:
        right_max[i] = max(right_max[i+1], heights[i])
        i -= 1
    
    water_units = 0
    i = 0
    j = n - 1
    
    while i < j:
        if heights[i] < heights[j]:
            water_units += max(0, min(left_max[i], right_max[j]) - heights[i])
            i += 1
        else:
            water_units += max(0, min(left_max[i], right_max[j]) - heights[j])
            j -= 1
    
    return water_units


# 示例输入序列
heights = [5,0,3,4,5,6,0,1,2,0,1,0,4]
print("Maximum units of water that can be trapped:", max_water_units(heights))
