class Solution(object):
    def restoreIpAddresses(self, s):
        result = []

        def backtrack(start, parts, path):
            # If 4 parts formed
            if parts == 4:
                # valid only if entire string used
                if start == len(s):
                    result.append(".".join(path))
                return

            # Try lengths 1 to 3
            for length in range(1, 4):
                if start + length > len(s):
                    break

                segment = s[start:start+length]

                # Rule 1: no leading zero
                if segment[0] == '0' and length > 1:
                    continue

                # Rule 2: value <= 255
                if int(segment) > 255:
                    continue

                backtrack(start + length,
                          parts + 1,
                          path + [segment])

        backtrack(0, 0, [])
        return result
        