#產生一個隨機變數1~100
#讓使用者重複輸入數字去猜
#猜對的話 印出'終於猜對了'
#猜錯的話 要告訴它 比答案大/小


import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	count += 1 #count = count + 1
	num = input('請猜數字:')
	num = int(num)
	print('你已經猜了', count, '次')
	if num == r:
		print('終於猜對了！')
		break
	elif num > r:
		print('比答案大')
	else:
		print('比答案小')