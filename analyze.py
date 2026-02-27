import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# 1. หาไฟล์ CSV ในโฟลเดอร์ปัจจุบัน
csv_files = glob.glob("*.csv")

if not csv_files:
    print("ไม่พบไฟล์ CSV ในโฟลเดอร์นี้")
    exit()

file_path = csv_files[0]
print(f"กำลังวิเคราะห์ไฟล์: {file_path}")

# 2. โหลดข้อมูล
df = pd.read_csv(file_path)

# 3. แสดงตัวอย่างข้อมูล
print("\nตัวอย่างข้อมูล:")
print(df.head())

# 4. สรุปสถิติพื้นฐาน
print("\nสถิติพื้นฐาน:")
print(df.describe(include='all'))

# 5. ตรวจสอบค่าที่หายไป
print("\nค่าที่หายไปในแต่ละคอลัมน์:")
print(df.isnull().sum())

# 6. Correlation (เฉพาะตัวเลข)
numeric_df = df.select_dtypes(include=['number'])
if not numeric_df.empty:
    print("\nCorrelation Matrix:")
    print(numeric_df.corr())

    # 7. สร้างกราฟ
    numeric_df.hist(figsize=(10, 8))
    plt.tight_layout()
    plt.show()
else:
    print("\nไม่มีคอลัมน์ตัวเลขสำหรับสร้างกราฟ")
