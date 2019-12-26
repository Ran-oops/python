#声明纸张的厚度0.08mm

paperh = 0.08

#计算纸张折叠次数
num = 0

while True:

    #纸张对折
    paperh *= 2
    #进行计数操作
    num += 1

    #判断是否达到了珠穆朗玛峰的高度
    if paperh >= 8848.13*1000:
        print('对折',num,'次可以达到珠穆朗玛峰的高度',paperh)
        #终止循环
        break
    
