class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        # value-symbol pairs (including subtractive forms)
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        result = []

        # build roman numeral
        for value, symbol in values:
            if num == 0:
                break

            count = num // value      # how many times symbol fits
            result.append(symbol * count)
            num -= value * count

        return "".join(result)