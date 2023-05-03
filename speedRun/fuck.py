# HW3_List_processing_Function (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

def get_sid_section(stu_rec):
    """
    รับ stu_rec ซึ่งเป็นข้อมูลประเภทสตริง ซึ่งจะประกอบด้วย
    - รหัสนิสิต (แต่ในการบ้านนี้จะใช้นามแฝงแทนรหัสนิสิตจริงๆ)
    - ตอนเรียน จะเป็นเลขตอนเรียนที่มีเลขศูนย์นำหน้ากี่ตัวก็ได้ หรือไม่มีศูนย์นำหน้าเลยก็ได้
    - รหัสอาจารย์ผู้สอน 
    คั่นด้วยเครื่องหมาย "," 

    ให้คืนค่าเป็น ลิสต์ ที่ประกอบด้วยสมาชิกสองตัว
    - ตัวแรก จะเป็นรหัสนิสิต เป็นข้อมูลประเภทสตริง
    - ตัวที่สอง จะเป็นเลขตอนเรียนที่ตัดเลขศูนย์ที่นำหน้าออกแล้ว เป็นข้อมูลประเภทสตริง

    ตัวอย่าง
    ให้ stu_rec เป็น "MrBond,007,BND" 
    ถ้าเรียก get_sid_section(stu_rec) ก็จะคืนค่าเป็น ["MrBond", "7"]
    ให้ stu_rec เป็น "stu_CompProg,101,CPG" 
    ถ้าเรียก get_sid_section(stu_rec) ก็จะคืนค่าเป็น ["stu_CompProg", "101"]
    """

    stu_rec = stu_rec.split(",")
    return [stu_rec[0], str(int(stu_rec[1]))]



def get_sid_sections(stu_recs):
    """
    รับ stu_recs ซึ่งเป็นข้อมูลประเภทลิสต์
    โดยสมาชิกแต่ละตัวจะเป็นข้อมูลประเภทสตริงที่อยู่ในแบบเดียวกับ argument stu_rec ของฟังก์ชัน
    get_sid_section ซึ่งจะประกอบด้วย
    - รหัสนิสิต
    - ตอนเรียน จะเป็นเลขตอนเรียนที่มีเลขศูนย์นำหน้ากี่ตัวก็ได้ หรือไม่มีศูนย์นำหน้าเลยก็ได้
    - รหัสอาจารย์ผู้สอน 
    คั่นด้วยเครื่องหมาย "," 

    ให้คืนค่าเป็น ลิสต์ ที่มีคุณสมบัติดังนี้ 
    - มีสมาชิกแต่ละตัวเป็นลิสต์ ซึ่งประกอบด้วยสมาชิกสองตัว
      - ตัวแรก จะเป็นรหัสนิสิต เป็นข้อมูลประเภทสตริง
      - ตัวที่สอง จะเป็นเลขตอนเรียนที่ตัดเลขศูนย์ที่นำหน้าออกแล้ว เป็นข้อมูลประเภทสตริง
    - เรียงลำดับลิสต์ตามรหัสนิสิต

    ตัวอย่าง
    ให้ stu_recs เป็น ["stu_CompProg,101,CPG", "MrBond,007,BND"]
    ถ้าเรียก get_sid_sections(stu_recs) ก็จะคืนค่าเป็น 
    [["MrBond", "7"], ["stu_CompProg", "101"]]
    (โปรดสังเกตว่า "MrBond" มีค่าน้อยกว่า "stu_CompProg")

    คำแนะนำ
    ให้ใช้ประโยชน์จากฟังก์ชัน get_sid_section
    """

    re = []
    for st in stu_recs:
        re.append(get_sid_section(st))
    re.sort()

    return re

    
        



def get_section(sid_sections, sid):
    """
    รับ sid_sections และ sid โดย
    - sid_sections จะเป็นลิสต์ที่อยู่ในแบบเดียวกับค่าที่คืนมาจาก get_sid_sections
    - sid จะเป็นข้อมูลประเภทสตริง เก็บรหัสนิสิต

    ให้คืนค่าเป็น สตริง ซึ่งเป็นเลขตอนเรียนของนิสิตที่มีรหัสนิสิตเป็น sid
    ถ้าไม่มีนิสิตดังกล่าวใน sid_sections ให้คืน สตริง ที่มีค่า 0

    ตัวอย่าง
    ให้ sid_sections เป็น [["MrBond", "7"], ["stu_CompProg", "101"]]
    ถ้าเรียก get_section(sid_sections, "MrBond") ก็จะคืนค่าเป็น "7" 
    ถ้าเรียก get_section(sid_sections, "Luffy") ก็จะคืนค่าเป็น "0" 
    """
    for s in sid_sections:
        if s[0] == sid: return s[1]
    return "0"

def get_stu_points(grader_points):
    """
    รับ grader_points ซึ่งเป็นข้อมูลประเภทลิสต์
    โดยสมาชิกแต่ละตัวจะเป็นข้อมูลประเภทสตริง ที่เก็บรายละเอียดการส่งคำตอบเข้าระบบเกรดเดอร์
    ซึ่งจะประกอบด้วย
    - รหัสนิสิต (แต่ในการบ้านนี้จะใช้นามแฝงแทนรหัสนิสิตจริงๆ)
    - เวลาที่ส่งคำตอบ
    - คะแนนที่ได้ (ไม่มีศูนย์นำหน้า)
    คั่นด้วยเครื่องหมาย "," 

    ให้คืนค่าเป็น ลิสต์ ที่มีคุณสมบัติดังนี้ 
    - มีสมาชิกแต่ละตัวเป็นลิสต์ ที่ประกอบด้วยสมาชิกสองตัว
      - ตัวแรก จะเป็นรหัสนิสิต เป็นข้อมูลประเภทสตริง
        - ตัวที่สอง คะแนนที่นิสิตคนนี้ได้ครั้งที่มากที่สุด เป็นข้อมูลประเภทจำนวนเต็ม
    - เรียงลำดับลิสต์ตามรหัสนิสิต

    ตัวอย่าง
    ให้ grader_points เป็น ["MrBond,9:55:10,80", "stu_CompProg,9:40:18,60", 
    "MrBond,9:59:19,100", "MrBond,10:02:43,0", "Luffy,10:09:59,0", 
    "Lalisa,9:50:09,100", "Zoro,10:05:55,0"]
    ถ้าเรียก get_stu_points(grader_points) ก็จะคืนค่าเป็น
    [["Lalisa", 100], ["Luffy", 0], ["MrBond", 100], ["Zoro", 0], ["stu_CompProg", 60]]
    """
    #น่าจะเรียงตามชื่อ

    re = []
    g = []

    for gp in grader_points:
        gp = gp.split(",")
        if gp[0] not in g:
            g.append(gp[0])
            re.append([gp[0], 0])
        for r in re:
            if gp[0] == r[0]:
                r[1] = max(r[1], int(gp[2]))
    re.sort()
    return re


def get_stu_section_points(stu_points, sid_sections):
    """
    รับ stu_points และ sid_sections โดย
    - stu_points จะเป็นลิสต์ที่อยู่ในแบบเดียวกับค่าที่คืนมาจาก get_stu_points
    - sid_sections จะเป็นลิสต์ที่อยู่ในแบบเดียวกับค่าที่คืนมาจาก get_sid_sections

    ให้คืนค่าเป็น ลิสต์ ที่มีจำนวนสมาชิกเท่ากับ stu_points 
    โดยที่สมาชิกแต่ละตัวจะแทนตอนเรียน คะแนนสูงสุดที่ได้ และรหัสนิสิต โดยจะเป็นข้อมูลประเภทลิสต์
    ที่ประกอบด้วยสมาชิกสามตัว
    - ตัวแรก จะเป็นตอนเรียน เป็นข้อมูลประเภทสตริง ถ้ารหัสนิสิตไม่มีใน sid_sections ให้ใส่สตริง 0
    - ตัวที่สอง คะแนนที่นิสิตคนนี้ได้ครั้งที่มากที่สุด เป็นข้อมูลประเภทจำนวนเต็ม
    - ตัวที่สาม จะเป็นรหัสนิสิต เป็นข้อมูลประเภทสตริง

    ตัวอย่าง
    ให้ stu_points เป็น 
    [["Lalisa", 100], ["Luffy", 0], ["MrBond", 100], ["Zoro", 0], ["stu_CompProg", 60]]
    และให้ sid_sections เป็น
    [["Lalisa", "101"], ["MrBond", "7"], ["Zoro", "7"], ["stu_CompProg", "101"]]
    ถ้าเรียก get_stu_section_points(stu_points, sid_sections) จะสามารถคืนค่าได้เป็น 
    [["101", 100, "Lalisa"], ["0", 0, "Luffy"], ["7", 100, "MrBond"], 
     ["7", 0, "Zoro"], ["101", 60, "stu_CompProg"]]

    คำแนะนำ
    ให้ใช้ประโยชน์จากฟังก์ชัน get_section
    """
    ans = []
    for point in stu_points:
        isFound = False
        for sec in sid_sections:
            if point[0] in sec:
                ans.append([sec[1], point[1], point[0]])
                isFound = True
                break
        if isFound == False:
            ans.append(["0", point[1], point[0]])
    return ans




def get_section_point_count(stu_section_points, min_point):
    """
    รับ stu_section_points และ min_point โดย
    - stu_section_points จะเป็นลิสต์ที่อยู่ในแบบเดียวกับค่าที่คืนมาจาก get_stu_section_points
    - min_point จะเป็นจำนวนเต็ม

    ให้คืนค่าเป็น ลิสต์ ที่มีจำนวนสมาชิกเท่ากับ จำนวนตอนเรียนทั้งหมดใน stu_section_points (นับตอนเรียน "0" ด้วย)
    โดยที่สมาชิกแต่ละตัวจะแทนตอนเรียน และจำนวนนิสิตที่ได้คะแนนไม่น้อยกว่า min_point 
    โดยจะเป็นข้อมูลประเภทลิสต์ ประกอบด้วยสมาชิก 2 ตัว
    - ตัวแรก จะเป็นตอนเรียน เป็นข้อมูลประเภทสตริง 
    - ตัวที่สอง จำนวนนิสิตของตอนเรียนนี้ที่ได้คะแนนไม่น้อยกว่า min_point เป็นข้อมูลประเภทจำนวนเต็ม
    เรียงตอนเรียนตามพจนานุกรม (ใช้ method sort())

    ตัวอย่าง
    ให้ stu_section_points เป็น 
    [["101", 100, "Lalisa"], ["0", 0, "Luffy"], ["7", 100, "MrBond"], 
     ["7", 0, "Zoro"], ["101", 60, "stu_CompProg"]]
    และให้ min_point เป็น 60
    ถ้าเรียก get_section_point_count(stu_section_points, min_point) ก็จะคืนค่าเป็น
    [["0", 0], ["101", 2], ["7", 1]]
    """



    sec = []
    ans = []
    for sp in stu_section_points:
        if sp[0] not in sec:
            ans.append([sp[0],0])
            sec.append(sp[0])
        
        for a in ans:
            if a[0] == sp[0] and sp[1] >= min_point:
                a[1] += 1
    ans.sort()

    return ans