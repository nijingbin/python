import base64
#在python中，可以用*表示添加几个，比如2**2表示2的平方 ，‘str’*2表示两个‘str’字符
def safe_base64_decode(s):
	return base64.b64decode(s+b'='*((4-len(s)%4)%4))	
	
if __name__ =='__main__':
	assert b'abcd' == safe_base64_decode(b'YWJjZA=='),safe_base64_decode('YWJjZA==')
	assert b'abcd' == safe_base64_decode(b'YWJjZA'),safe_base64_decode('YWJjZA')
	print('Pass')