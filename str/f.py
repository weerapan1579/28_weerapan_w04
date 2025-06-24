exe = "======================================================="
print(exe)
print("เครื่องคิดเลข")
# รับตัวเลข
num1 = float(input("ใส่ตัวเลขแรก : "))
num2 = float(input("ใส่ตัวเลขตัวที่ 2 : "))
print(exe)

# แสดงตัวเลือกการคำนวณ
print("\nเลือกการดำเนินการ:")
print("1. บวก (+)")
print("2. ลบ (-)")
print("3. คูณ (*)")
print("4. หาร (/)")
print("5. ยกกำลัง (^)")

# รับตัวเลือก
choice = input("กรุณาเลือก (1/2/3/4/5): ")
print(exe)

# คำนวณตามตัวเลือก
if choice == '1':
    result = num1 + num2
    print(f"\nผลลัพธ์: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"\nผลลัพธ์: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"\nผลลัพธ์: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 == 0:
        print("\nข้อผิดพลาด: ไม่สามารถหารด้วยศูนย์ได้")
    else:
        result = num1 / num2
        print(f"\nผลลัพธ์: {num1} / {num2} = {result}")
elif choice == '5':
    result = num1 ** num2

print(f"ผลลัพธ์ : {result}")