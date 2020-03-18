
#######################
prthon 头部模板设置：File---settings---Editor---File and Code Templates---Python script

${PROJECT_NAME} - 当前的项目名
${NAME} - 在文件创建过程中，新文件对话框的命名
${USER} - 当前的登录用户
${DATE} - 现在的系统日期
${TIME} - 现在的系统时间
${YEAR} - 当前年份
${MONTH} - 当前月份
${DAY} - 当前月份中的第几日
${HOUR} - 现在的小时
${MINUTE} - 现在的分钟
${PRODUCT_NAME} - IDE创建文件的名称
${MONTH_NAME_SHORT} - 月份的前三个字母缩写
${MONTH_NAME_FULL} - 完整的月份名
————————————————
版权声明：本文为CSDN博主「CN-AllenRen」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/RKun595/article/details/78666636


########################
pycharm修改文件保存默认路径：PyCharm——>Settings——>Appearance&Behavior——>System Setting——>Project Opening——>Default directory


########################
必须参数：函数调用时必须传入的参数
关键字参数：键值对参数，以“=”连接
默认参数：定义函数时传入带值的参数，在调用函数时传入对应值则使用传入值
不定长参数：加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。参数带两个星号 **，传入不限个关键字参数。
如果单独出现星号 * 后的参数必须用关键字传入。如：
def f(a,b,*,c):
    return a+b+c
调用时：f(1,2,c=3)


*iterables：
*args：*args是用来发送一个非键值对的可变数量的参数列表给一个函数
**kwargs：**kwargs	允许你将不定长度的键值对作为参数传递给一个函数。











