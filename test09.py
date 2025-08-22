# สร้างโปรแกรมคำนวณเงินเดือนสุทธิที่ต้องจ่ายหลังจากโดนภาษีแล้ว 7% ของเงินเดือน 
# และหักค่าประกันสังคม 3% ของเงินเดือน
# โดยรับค่ารหัสพนักงาน ชื่อพนักงาน เงินเดือน ทางแป้นพิมพ์
# พร้อมแสดงผลข้อมูล และรายละเอียดการหักต่าง ๆ

print('+++++++++++++++++++++++++')
print('โปรแกรมคํานวณเงินเดือน')
print('+++++++++++++++++++++++++')

emp_code = input('ป้อนรหัสพนักงาน : ')
emp_name = input('ป้อนชื่อพนักงาน : ')
emp_salary = float(input('ป้อนเงินเดือน : '))

print('+++++++++++++++++++++++++')

tax = emp_salary * 7 / 100
insurance = emp_salary * 3 / 100
emp_salary_net = emp_salary - tax - insurance

# แบบ f-string
print(f'รหัส; {emp_code} ชื่อ {emp_name} เงินเดือน {int(emp_salary)}')
print(f'หักภาษี {int(tax)} บาท')
print(f'หักค่าประกันสังคม {int(insurance)} บาท')
print(f'ต้องจ่ายเงินเดือนสุทธิ {int(emp_salary_net)} บาท')
print('+++++++++++++++++++++++++')

# แบบใช้ ,
print('+++++++++++++++++++++++++')
print('รหัส', emp_code, 'ชื่อ', emp_name, 'เงินเดือน', int(emp_salary))
print('หักภาษี', int(tax), 'บาท')
print('หักค่าประกันสังคม', int(insurance), 'บาท')
print('ต้องจ่ายเงินเดือนสุทธิ', int(emp_salary_net), 'บาท')
print('+++++++++++++++++++++++++')

# แบบใช้ +
print('+++++++++++++++++++++++++')
print('รหัส' + emp_code + ' ชื่อ' + emp_name + ' เงินเดือน' + str(int(emp_salary)))
print('หักภาษี' + str(int(tax)) + 'บาท')
print('หักค่าประกันสังคม' + str(int(insurance)) + 'บาท')
print('ต้องจ่ายเงินเดือนสุทธิ' + str(int(emp_salary_net)) + 'บาท')
print('+++++++++++++++++++++++++')

# แบบใช้ format()
print('+++++++++++++++++++++++++')
print('รหัส {}'.format(emp_code))
print('ชื่อ {}'.format(emp_name))
print('เงินเดือน {}'.format(int(emp_salary)))
print('หักภาษี {} บาท'.format(int(tax)))
print('หักค่าประกันสังคม {} บาท'.format(int(insurance)))
print('ต้องจ่ายเงินเดือนสุทธิ {} บาท'.format(int(emp_salary_net)))
print('+++++++++++++++++++++++++')
