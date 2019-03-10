class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash = {}
        for item in cpdomains:
            count, domain = item.split(' ')
            # 拆解 domain
            domain_split = domain.split('.')
            for i in range(len(domain_split)):
                d = '.'.join(domain_split[i:])
                
                if d in hash:
                    hash[d] += int(count) # 注意 count 是 str 要轉成 int
                else:
                    hash[d] = int(count)

        res = []
        for k, v in hash.items():
            res.append(str(v) + ' ' + k)
        
        return res
