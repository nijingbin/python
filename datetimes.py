# -*- coding:utf-8 -*-
#转换任意时间字符为UTC时间
#在书写文件名时，需注意不要写成系统import的文件名，否则，编译报错ImportError
import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str, tz_str):
	dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	atime = dt.replace(tzinfo = timezone(timedelta(hours = int(re.match(r'^(UTC)([\+|\-]?[0-9]+)(:*)', tz_str).group(2)))))
	return atime.timestamp()

if __name__=='__main__':
	t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
	assert t1 == 1433121030.0, t1
	t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
	assert t2 == 1433121030.0, t2
	print('Pass')