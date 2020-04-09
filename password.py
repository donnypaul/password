x = 0
while x < 3:
    password = input('請輸入密碼： ')
    if password == 'a123456':
        print('登入成功！')
        break
    else:
        y = 2 - x
        if y == 0:
            print('登入失敗')
            break
        print('密碼錯誤！ 還有', y, '次機會')
        x = x + 1


