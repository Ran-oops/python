
#国家
zhuxi = '习大大'

#省份
def shandong():

    shengzhang = '曹睿'
    #济南市
    def jinan():

        #槐荫区
        def huaiyin():
            print(zhuxi)
            print(shengzhang)

        #调用槐荫区
        huaiyin()

    #调用济南市
    jinan()

#调用山东省
shandong()
