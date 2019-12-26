#用于初始化用户角色信息

def chuanqi(name,yifu,maozi,xiezi,wuqi,jiezhi):
    #名字
    print('名字',name)
    #衣服
    print('身穿:',yifu)
    #帽子
    print('头戴:',maozi)
    #鞋
    print('脚穿:',xiezi)
    #武器
    print('手持:',wuqi)
    #戒指
    print('手戴:',jiezhi)


#调用函数(创建任务)

#chuanqi('法身披风','易拉环','绿钢盔','今生为你偷','草鞋','皮鞭')


#关键字参数（实参）
chuanqi(yifu='法身披风',jiezhi='易拉环',maozi='绿钢盔',name='今生为你偷',xiezi='草鞋',wuqi='皮鞭')
