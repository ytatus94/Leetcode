class Solution:
    def simplifyPath(self, path: str) -> str:
        if path[-1] == '/':
            path = path[: -1]

        res = []

        for i in path.split('/'):
            if i != '' and i != '.' and i != '..':
                res.append(i)
            elif i == '..':
                if len(res) == 0:
                    continue
                else:
                    res.pop()
            else:
                continue
        
        return "/" + "/".join(res)
        
