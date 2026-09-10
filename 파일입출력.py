# file=open("test.txt","w",encoding="utf-8")
# file.write("안녕하세요")
# file.close()

# with open("test.txt","w",encoding="utf-8")as file:
# 	file.write("안녕하세요")


# while True:
# 	memo=input("메모를 입력하세요. 종료하려면 q 입력: ").strip()

# 	if memo.lower()=="q":
# 		break
	
# 	with open("memo.txt","a",encoding="utf-8")as file:
# 		file.write(memo+"\n")
	
# 	print("메모 저장이 완료되었습니다.")

import os

print(os.getcwd())


import os
d = os.getcwd()
print(d)