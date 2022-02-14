class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        value_before = 0
        for letter in s:
            current_value = roman_to_int_dictionary[letter]
            result += current_value
            if current_value > value_before:
                result = result - (2 * value_before)
            value_before = current_value
        return result


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
