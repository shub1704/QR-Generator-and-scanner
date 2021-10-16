import qrcode
from PIL import Image,ImageDraw


img = qrcode.make('shubham')
print(type(img))
print(img.size)
img.save('qrcode_test.png')

'''
def qrmaker(self):
    img = qrcode.make(self.info())
    print(type(img))
    print(img.size)
    print(self.name)

def saveqr(self):
    img.save('qrcode_test.png')
    
    import qrcode
import pandas as pd
import os,time
def codes(name):
    img = qrcode.make(name)
    print(type(img))
    print(img.size)
    return img

df=pd.read_csv(r'C:\Users\mayur\Desktop\ml\titanic.csv')
df["qrcode"] = df["Name"].apply(codes)
df.head(5)

    
    '''