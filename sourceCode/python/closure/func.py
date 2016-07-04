#codeing=utf-8
#闭包
def func_100(val):
    passline = 60
    if val >= passline:
        print ("pass")
    else:
        print ("failed")
    
def func_150(val):
    passline = 90
    if val >= passline:
        print ("pass")
    else:
        print ("failed")

def set_passline(passline):
    def cmp(val):
        if val >= passline:
            print ("pass")
        else:
            print ("failed")
    return cmp

f_100 = set_passline(60)
f_150 = set_passline(90)

f_100(89)
f_150(89)
        
# func_100(89)
# func_150(89)
# print (Max(90,100))