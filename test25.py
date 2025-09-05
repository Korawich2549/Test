# สร้างโปรแกรมคำนวนอายุจากปีเกิด พศ ของพนั

from datetime import datetime

print('---------------------')
print('---Ages Calculeted---')
print('---------------------')

while True :
    emp_name = input("ป้อนชื่อพนักงาน: ")
    if emp_name.upper() == 'SAU' :
        break
    emp_year = int(input("ป้อนปีเกิด(พ.ศ.): "))
    emp_age = (datetime.now().year +543) - emp_year
    print(f"คุณ {emp_name} เกิดปี {emp_year} อายุ {emp_age} ปี")

print('---------------------')