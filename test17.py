# โปรแกรมคำนวณราคาสินค้าที่รับส่วนลดแล้ว โดยป้อนรหัสสินค้า ชื่อสินค้า ประเภทสินค้า ซึ่งมี 4 ประเภท คือ food(F/f), woman(W/w), man(M/m), kitchen(K/k) โดยป้อนเป็นตัวย่อ  และราคาสินค้าทางแป้นพิมพ์ แล้วคำนวณราคาสินค้าที่รับส่วนลดแล้วทางหน้าจอ โดยสินค้าประเภท food ลด 2% ของราคาสินค้า, woman ลด 4% ของราคาสินค้า, man ลด 6% ของราคาสินค้า, kitchen ลด 10% ของราคาสินค้า หากป้อนประเภทสินค้าผิดจากที่กำหนดให้แสดงข้อความ "คุณป้อนประเภทผิด !!!"

print('-----------------------------')
print('โปรแกรม Product Sale')
print('-----------------------------')
pro_id = input('ป้อนรหัสสินค้า : ')
pro_name = input('ป้อนชื่อสินค้า : ')
pro_type = input('ป้อนประเภทสินค้า (F/f, W/w, M/m, K/k): ')
pro_price = float(input('ป้อนราคาสินค้า : '))
print('-----------------------------')
if pro_type == 'F' or (pro_type == 'f'):
    pro_sale = pro_price - (pro_price * 2 / 100)
    print(f'ราคาสินค้าที่ลดแล้วเป็น {pro_sale} บาท')
elif pro_type == 'W' or (pro_type == 'w'):
    pro_sale = pro_price - (pro_price * 4 / 100)
    print(f'ราคาสินค้าที่ลดแล้วเป็น {pro_sale} บาท')
elif pro_type == 'M' or (pro_type == 'm'):
    pro_sale = pro_price - (pro_price * 6 / 100)
    print(f'ราคาสินค้าที่ลดแล้วเป็น {pro_sale} บาท')      
elif pro_type == 'K' or (pro_type == 'k'):
    pro_sale = pro_price - (pro_price * 10 / 100)
    print(f'ราคาสินค้าที่ลดแล้วเป็น {pro_sale} บาท')
else:
    print('คุณป้อนประเภทผิด !!! ต๋าย ตาย ป้อนผิด ป้อนใหม่อีกครั้งนะ...')
print('-----------------------------')