class A():
	__slots__ = ('name',)
	
	@property
	def names(self):
		return self._name
	@names.setter
	def names(self,value):
		if(value=='qingzhou'):
			self._name = value
		else:
			self._name = 'weifang'
			
	def charge(self):
		print('charge')
		
def runPro():
	s = A()
	s.name = 'qingzhou'
	print(s.name)
	
if __name__ == '__main__':
	runPro()