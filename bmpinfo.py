import struct
#注意在Print输出参数是，%后需要加（），把变量变成tuple
def readFile(s):
	with open(s,'rb') as f:
		bmpinfo = f.read(30)
		listBmpInfo = struct.unpack('<ccIIIIIIHH',bmpinfo)
		if listBmpInfo[0].decode('utf-8')=='B' and listBmpInfo[1].decode('utf-8')=='M':
			print('图片的大小为%d*%d,颜色数为%d'%(listBmpInfo[6],listBmpInfo[7],listBmpInfo[9]))
		
if __name__=='__main__':
	readFile('1.bmp')