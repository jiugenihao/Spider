# Filename : test.py
# author by : www.runoob.com
 
# 引入日历模块
import calendar
 
i = 1
opt         = "ul"
uniqueid    = "253_18439422019_92" + str(i)
channel     = '1'
deviceid    = '864294049954898'
devicetype  = "ios7.2"
ip          = "49.233.52.212"
svrid       = '1'
sid         = 100000000 + i
strdata = opt + ',' + uniqueid + ',' + channel + ',' + deviceid + ',' + devicetype + ',' + ip + ',' + svrid + ',' + str(sid)
print(strdata)
print(b'ul,253_18439422019_925,1,864294049954898,ios7.2,49.233.52.212,1,122518143\r\n')
bstr = bytes(strdata, 'utf-8')
print(bstr)

# 输入指定年月
#yy = int(input("输入年份: "))
#mm = int(input("输入月份: "))
 
# 显示日历
#print(calendar.month(1970,1))
#print(calendar.month(2020,2))
#print(calendar.month(2020,3))
#print(calendar.month(2020,4))
#print(calendar.month(2020,5))
#print(calendar.calendar(1970))
#def greetPerson(*name):
#    print('Hello', name)
#  
#greetPerson('Runoob', 'Google')

#list_sort = [2,55,11,44,33,777,8,1,42]
#list_sort.sort()
#print(list_sort)
#for token in tokens:
#    token = int(token)
#    pass
#for i in range(len(tokens)):
#    tokens[i] = int(tokens[i])
#

#list1 = [1,2,3]
#list2 = list1
#list3 = list1[:]
#
#list1[0] = 111
#print(list2)
#print(list3)
#
#day,hour = divmod(20,3)
#print(day)
#print(hour)
#list1 = [ '1', '2', ['1', '2', '3'] ]
#print(list1)
##list2 = list1 * 2
##list2 = [int(x) for x in list1]
##print(list2)
#
#str1 = "hello"
#str2 = "python"
#str3 = str1 + str2
#print(str3)
#strlist = ['hello', 'python', 'nihao']
#str4 = '@'
#str4.join(strlist)
#print(str4)