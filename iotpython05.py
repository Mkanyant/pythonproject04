#หาพื้นที่สี่เหลี่ยม และสามเหลี่ยม โดยรับกว้าง ยาว/ฐาน สูง ทางแป้นพิมพ์และแสดงผลทางหน้าจอ
#feature การทำงานอะไรบ้าง
#1.รับค่า กว้าง ยาว 2.รับค่า ฐาน สูง 3.คำนวณพื้นที่ 
def inputWitdhLong( ) :
    wi = float( input('ป้อนกว้าง : ') )
    lo = float( input('ป้อนยาว : ') )
    return wi, lo

def inputBaseHigh( ) :
    ba = float( input('ป้อนฐาน : ') )
    hi = float( input('ป้อนสูง : ' ) )
    return ba, hi

def calAndshowAreaSquare( wi, lo ) :
    area = wi * lo
    print(f'สี่เหลี่ยมกว้าง {wi} ยาว {lo} มีพื้นที่ {area}' )

def calAndShowAreaSquare( ba, hi ) :
    area = ba *hi /2
    print(f'สามเหลี่ยมฐาน {ba} ยาว {hi} มีพื้นที่ {area}')

wi, lo = inputWitdhLong( )
calAndshowAreaSquare( wi, lo )
print('...........................................')
ba, hi = inputBaseHigh( )
calAndShowAreaSquare( ba, hi )