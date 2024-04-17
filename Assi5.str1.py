#  Find all occurrences of “USA” from right to left in a given string ignoring the case. also display the
# starting position
# # Given:
str1 = "Welcome to USA. usa awesome, isn't it?"
str1="usa,Usa,usa,Usa,usa,Usa"
# # Expected answer : 16, 11

str1 = str1.lower()
s=0
e=len(str1)
for idx in range(len(str1)):
    idx =str1.rfind("usa",s,e)
    if idx == -1:
        break
    print(idx)
    e=idx











# str1 =str1.lower()
# s=0
# e=len(str1)
# idx=str1.rfind("usa",s,e)
# print(idx)
# e=idx
# print(str1.rfind("usa",s,e))

