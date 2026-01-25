import pandas as pd

# โหลดไฟล์
eeg = pd.read_csv("C:\\Users\\ADMIN\\Desktop\\Sleep recording\\SN018\\SN018_data.txt")          # ไฟล์สัญญาณ EEG
events = pd.read_csv("C:\\Users\\ADMIN\\Desktop\\Sleep recording\\SN018\\SN018_sleepscoring.txt")         # ไฟล์ event/annotation

# สร้างคอลัมน์ใหม่สำหรับ annotation
eeg["Annotation"] = ""

# ใส่ label ตาม event
for _, row in events.iterrows():
    onset = row[" Recording onset"]
    duration = row[" Duration"]
    label = row[" Annotation"]

    # หาช่วงเวลา (onset → onset+duration)
    mask = (eeg["Time"] >= onset) & (eeg["Time"] < onset + duration)
    
    # ใส่ annotation ลงไป
    eeg.loc[mask, "Annotation"] = label

# บันทึกเป็นไฟล์ใหม่
eeg.to_csv("C:\\Users\\ADMIN\\Desktop\\Sleep recording\\data\\SN018.csv", index=False)
print(events.head())