class Solution:
	num_dict = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,  
	}

	def romanToInt(self, s: str) -> int:
		result = 0

		for i, value in enumerate(s[:-1]):
			current_num = self.num_dict[value]

			if current_num < self.num_dict[s[i + 1]]:
				result -= current_num
			else:
				result += current_num

		result += self.num_dict[s[-1]]
		return result
