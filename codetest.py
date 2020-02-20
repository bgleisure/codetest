password = input('請輸入密碼:')
while True:
	if password == 'a123456':
		print('恭喜你！登入成功')
		break
	else:
		print('你還有2次機會')
		password = input('請輸入密碼:')
		while True:
			if password == 'a123456':
				print('恭喜你!登入成功')
				break
			else:
				print('你還剩1次機會')
				password = input('請輸入密碼')
				while True:
					if password == 'a123456':
						print('恭喜你!登入成功')
						break
					else:
						print('登入失敗，請洽技術人員')
						break
				break
		break





