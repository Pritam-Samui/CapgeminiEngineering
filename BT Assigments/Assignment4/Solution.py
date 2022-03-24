from Concetination import Concetinate as con
from Equal_or_not import Equal_o_n as eon
class Solution:
	def solution(self):
		print("Enter the string1")
		string1=input()
		print("Enter the string2")
		string2=input()
		con.concatinate(string1, string2)
		eon.equal_n(string1, string2)

obj = Solution()
obj.solution()
