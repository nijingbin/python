#预编译
import re

def rematch(strReEmail):
	strRE = r'^([0-9a-zA-Z\.]+)@(\w+).(\w{1,4})$'
	strRE2nd = r'^<([a-zA-Z][a-zA-Z\s]+)>\s*([0-9a-zA-Z\.]+)@(\w+).(\w{1,4})$'
	listEmail = re.match(strRE,strReEmail)
	listEmail2nd = re.match(strRE2nd,strReEmail)
	if not listEmail and not listEmail2nd:	
		print('Error：不正确的Email的格式。')
		return False
	if listEmail2nd:
		strName = listEmail2nd.group(1)
		print('Email的主人是：%s'%strName)
	return True
	
if __name__=="__main__":
	while True:
		strEmail = input('请输入Email地址：')
		if rematch(strEmail):
			break