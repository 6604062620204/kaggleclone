import h5py
from PIL import Image
import numpy as np
import os

# เส้นทางไปยังไฟล์ HDF5
hdf5_path = r"D:\KMUTNB-CS\OOPject\comfile\isic-2024-challenge\train-image.hdf5"

# โฟลเดอร์ปลายทางสำหรับบันทึกรูป JPG
output_dir = r"D:\KMUTNB-CS\OOPject\comfile\isic-2024-challenge\output_images"
os.makedirs(output_dir, exist_ok=True)

# เปิดไฟล์ HDF5
with h5py.File(hdf5_path, 'r') as hdf5_file:
    print("Datasets ที่มีอยู่ในไฟล์นี้:")
    print(list(hdf5_file.keys()))   
    # สมมติว่าภาพเก็บอยู่ภายใต้คีย์ 'isic_id'
    for key in hdf5_file.keys():
        print(f"กำลังแปลงภาพจากคีย์: {key}")
        image_array = hdf5_file[key][:]
        
        # ถ้าภาพยังไม่ได้อยู่ใน uint8 (0-255) ต้องแปลงเป็นรูปแบบนี้ก่อน
        if image_array.max() <= 1:
            image_array = (image_array * 255).astype(np.uint8)
        else:
            image_array = image_array.astype(np.uint8)
        
        # แปลง NumPy array ให้เป็นวัตถุภาพ
        img = Image.fromarray(image_array)
        
        # บันทึกเป็นไฟล์ JPG
        img.save(os.path.join(output_dir, f"{key}.jpg"))

print("การแปลงเสร็จสมบูรณ์!")
