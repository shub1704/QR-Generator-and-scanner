import qrcode
from datetime import datetime

def qrmaker(self):

    img = qrcode.make(self)
    date = str(datetime.now())
    print(f"filename_{date}")
    print(img.size)
    file = open(barcodedata,)
    img.save('barcodedata/qrcode{no}.png'.format(no=date))



if __name__ == '__main__':
    qrmaker("dddffgghh")