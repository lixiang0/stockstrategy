class Stock:
    def __init__(self,args):
        self.name=args[0]
        self.today=args[1]
        self.yesterday=args[2]
        self.now=args[3]
        self.top=args[4]
        self.low=args[5]
        self.time=' '.join(args[-3:-2])
        self.code=args[-1]
    def __str__(self):
        return ' '.join([self.name,self.code,"现价：",'{0:8s}'.format(self.now),"最高：",'{0:8s}'.format(self.top),"最低：",'{0:8s}'.format(self.low),"今开：",'{0:8s}'.format(self.today),"昨收：",'{0:8s}'.format(self.yesterday),' {0:.4s} '.format(str((float(self.now)-float(self.yesterday))/float(self.yesterday)*100)),self.time])
                             #今开  昨收   现价   最高  最低               成交量   成交额        买1    价格  买2   价格   买3   价格   买4    价格  买5    价格  卖1         卖2          卖3          卖4         卖5         时间
#var hq_str_sh600538="国发股份,5.940,5.950,6.010,6.020,5.930,6.000,6.010,5211267,31156630.000,11200,6.000,84833,5.990,54000,5.980,41900,5.970,77500,5.960,5000,6.010,134100,6.020,77300,6.030,38900,6.040,84800,6.050,2017-08-25,15:00:00,00";


class Volume:
    def __init__(self,args):
        self.code=args[0]
        self.name=args[1]
        self.change=args[2]
        self.cost=args[3]
    def __str__(self):
        return ' '.join([self.name,self.code,self.change,self.cost])