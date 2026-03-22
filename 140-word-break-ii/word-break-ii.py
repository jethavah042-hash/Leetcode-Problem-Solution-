class Solution(object):
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        memo = {}

        def dfs(sub):
            # if already solved
            if sub in memo:
                return memo[sub]

            # base case
            if not sub:
                return [""]

            result = []

            for i in range(1, len(sub) + 1):
                prefix = sub[:i]

                if prefix in word_set:
                    remaining_sentences = dfs(sub[i:])

                    for sentence in remaining_sentences:
                        if sentence:
                            result.append(prefix + " " + sentence)
                        else:
                            result.append(prefix)

            memo[sub] = result
            return result

        return dfs(s)
        