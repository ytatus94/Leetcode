class Solution:
  def nameDeduplication(self, names):
        result = []

        d = {}
        for name in names:
            name = name.lower()
            if name not in d.keys():
                d[name] = 1
                result.append(name)

        return result
