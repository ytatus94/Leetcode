# 背包型 DP, 計數型 DP
# 轉移方程
#   f[i] = f[i -a[0]] + f[i-a[1]] +...+ f[i-a[n-1]]
#   f[i] = 有多少種組合能拼出 i
#   要注意 i > a[j] 的時候才能加入到公式裡面
# 初始條件
# f[0] = 1 有一種組合能拼出 0 (就是什麼都不選的時候)
# TC = O(N * target) = 計算步數, SC = O(target)

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
