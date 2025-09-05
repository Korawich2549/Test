# Break, Continue
# Break ใน loop ทำงานเมื่อไหร่ จบการทำงาน loop ทันที
# Continue ใน loop ทำงานเมื่อไหร่ จบ loop แค่รอบนั้นทันทีแล้วไปต่อรอบต่อไปได้เลย  // ข้าม loop รอบนั้นไป แล้วไปรอบต่อไป

for aa in range(5):
    if aa == 2 :
        break
    print(aa, "hi")
print("----------------")
for aa in range(5):
    if aa == 2 :
        continue
    print(aa, "hi")