# generator/utils.py
import os
import re

def get_image_files(folder_path, extensions=(".png", ".jpg", ".jpeg", ".webp")):
    files_with_numbers = []
    for f in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(extensions):
            name_without_ext = os.path.splitext(f)[0]
            # ลองหาตัวเลขในชื่อไฟล์
            numbers = re.findall(r'(\d+)', name_without_ext)
            if numbers:
                # ถ้ามีตัวเลข ให้ใช้ตัวเลขแรกเป็น key ในการเรียงลำดับ
                files_with_numbers.append((f, int(numbers[0])))
            else:
                # ถ้าไม่มีตัวเลข ให้ใช้ชื่อไฟล์เดิมเป็น key (สำหรับการเรียงตามตัวอักษร)
                files_with_numbers.append((f, name_without_ext))

    # เรียงลำดับโดยใช้ตัวเลข (index 1 ของ tuple) เป็นหลัก
    files_with_numbers.sort(key=lambda item: item[1])

    # ส่งกลับเฉพาะชื่อไฟล์ที่ไม่มีนามสกุล
    return [os.path.splitext(file_tuple[0])[0] for file_tuple in files_with_numbers]