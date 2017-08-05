import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def calc_md5(password):
	md5 = hashlib.md5()
	md5.update(password.encode('utf-8'))
	return md5.hexdigest()
	
def login(logUser,pwd):
	if db.get(logUser,'用户名不存在') and calc_md5(pwd + logUser + 'the-Salt') == db.get(logUser):
		print('pass.')
	else:
		print('No pass.')
		
def register(username,pwd):
	db[username] = calc_md5(pwd + username + 'the-Salt')
	print(db[username])
	
if __name__ == '__main__':
	while True:
		strOpt = input('input your opt:')
		if strOpt == '2':
			strUser = input('input your administrator:')
			strPassword = input('input your PASSWORD:')
			login(strUser, strPassword)
		elif strOpt == '1':
			break;
		else:
			strUser = input('Reinput your administrator:')
			strPassword = input('Reinput your PASSWORD:')
			register(strUser, strPassword)	