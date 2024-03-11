class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Count occurrences of characters in T
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Construct the sorted string based on S
        sorted_str = ''
        for char in order:
            if char in count:
                sorted_str += char * count[char]
                count.pop(char)

        # Append remaining characters from T
        for char in count:
            sorted_str += char * count[char]

        return sorted_str
        