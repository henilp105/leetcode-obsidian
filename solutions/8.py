import re 
class Solution:
    def custom_min(self,x, y):
        return x if x < y else y

    def custom_max(self,x, y):
        return x if x > y else y
        
    def myAtoi(self, s: str) -> int:
        pattern = r"^\s*([-+]?\d+)"
        match = re.match(pattern, s)
        
        # Extracting the matched integer or defaulting to 0.
        integer_str = match.group(1) if match else "0"
        
        # Parsing the integer string to an actual integer.
        parsed_integer = int(integer_str, 10)
        
        # Setting the boundaries of the integer.
        min_boundary = -2**31
        max_boundary = 2**31 - 1
        bounded_integer = self.custom_max(self.custom_min(parsed_integer, max_boundary), min_boundary)
        
        return bounded_integer