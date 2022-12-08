    if nums is None:
      return 0
    n = len(nums)
    if n == 0:
      return 0
    
    f = [0 for i in range(target + 1)]
    
    f[0] = 1
    for i in range(1, target + 1):
        for j in range(n):
            if i > nums[j]:
                f[i] += f[i - nums[j]]
                
    return f[target]
