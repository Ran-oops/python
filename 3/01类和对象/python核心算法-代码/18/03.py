#自定义异常类(数据不能为负数)
class NEGError(RuntimeError):

    #实例化对象的时候自动触发
    def __init__(self,errmsg,errline):
        #将错误信息存入对象
        self.errmsg = errmsg
        self.errline = errline

    #print（对象的时候自动触发）
    def __str__(self):
        return self.errmsg+self.errline



try:
    num = -99
    if num < 0:
        #主动抛出异常对象（只有系统异常可以自动抛出）
        raise NEGError('NEGError：变量的值小于0的','错误行数为19')

except NEGError as obj:
    print('数据不能为负数')
    print(obj)


