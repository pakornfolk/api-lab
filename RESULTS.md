# ผลการทดลอง API Lab

## Part 0
- Step 0.1 จำนวนชื่อพิซซ่าที่พบ: 18
- Step 0.3 รหัสสถานะเมื่อส่งคำขอโดยไม่มี Token: 401
- Step 0.4 ชื่อพิซซ่าที่ API สร้าง: An Orange Quattro Stagioni

### Step 0.12: Test without a session

Ran `pytest -v test_no_session.py` three times.

- Run 1: FAILED — login returned 401 instead of 200.
- Run 2: FAILED — login returned 401 instead of 200.
- Run 3: FAILED — login returned 401 instead of 200.

## Step 0.16 – Defect 1

**Title:** Excluding all available tools returns 500

**Request:** POST `/api/pizza` โดยกำหนด `excludedTools` เป็น `["Knife", "Pizza cutter", "Scissors"]`

**ผลที่คาดหวัง:** `400 Bad Request` พร้อมข้อความ error ในรูปแบบ JSON เพราะไม่มีเครื่องมือเหลือสำหรับทำพิซซ่า

**ผลที่เกิดขึ้นจริง:** `500 Internal Server Error` และ response body ว่างเปล่า

**ความรุนแรง:** ปานกลาง (Medium) – API ตอบกลับเป็น server error ทั้งที่เป็นคำขอที่ไม่สามารถดำเนินการได้ และควรจัดการเป็น client error

- Step 0.16, blocks of "how many of the three tools are excluded":
  - Block 0: ไม่ exclude เลย
  - Block 1: exclude 1 รายการ
  - Block 2: exclude 2 รายการ
  - Block 3: exclude ทั้ง 3 รายการ

### Step A4: Rating ownership

A second user attempted to read, update, and delete a rating created by the owner.

| Operation | Status Code | Result |
|---|---:|---|
| Read another user's rating | 404 | Refused |
| Update another user's rating | 400 | Refused |
| Delete another user's rating | 400 | Refused |

After each attempt, the owner could still read the rating and its stars value remained unchanged.

## Part B: Reflection

**1.** API tests สามารถพบปัญหาการเชื่อมต่อระหว่าง server กับ database และปัญหาจากการตั้งค่าหรือการทำงานของระบบจริง ซึ่ง unit test ที่ใช้ stubs อาจตรวจไม่พบ ส่วน unit test ยังมีประโยชน์เพราะทดสอบ logic ของแต่ละ function ได้เร็วและแยกสาเหตุของปัญหาได้ง่าย

**2.** แต่ละ test สร้าง user ใหม่เพื่อไม่ให้ข้อมูลจาก test อื่นมารบกวนผล และไม่ต้องใช้ public token ร่วมกัน ใน Project 2 จะสร้างบัญชีหรือข้อมูลทดสอบแยกในแต่ละ test เพื่อป้องกันข้อมูลชนกัน

**3.** การใช้ session เดียวช่วยให้ request ต่อเนื่องใช้การเชื่อมต่อและข้อมูล session เดิมได้  
จาก Step 0.12 เมื่อทดสอบโดยไม่ใช้ session ทั้ง 3 runs ล้มเหลว โดย login ได้ status code 401 แทน 200

**4.** Step 0.16 พบ defect เมื่อ exclude tools ครบทั้ง 3 รายการ API ตอบ 500 พร้อม body ว่าง แทนที่จะปฏิเสธด้วย 400 และข้อความอธิบาย ซึ่งทำให้ client เข้าใจสาเหตุได้ยากกว่า เก็บ test เป็น xfail เพื่อบันทึก defect ที่ยังไม่แก้ และตรวจสอบได้เมื่อมีการแก้ไข

**5.** Base choice coverage ใช้ 9 tests: 1 + 2 + 3 + 1 + 2 = 9 ส่วน all combinations coverage ใช้ 72 tests: 3 × 4 × 2 × 3 = 72

**6.** ผู้ใช้คนอื่นอ่าน rating ได้ 404, update ได้ 400 และ delete ได้ 400 โดยคาดหวังให้ทุก operation ถูกปฏิเสธด้วย status code 400–499 ความแตกต่างของ 404 กับ 400 ไม่ใช่ defect เพราะทั้งคู่ปฏิเสธการเข้าถึงได้ถูกต้อง และ rating ของเจ้าของไม่เปลี่ยนแปลง

**7.** เมื่อใช้ made-up token เรียก `GET /api/ratings` ได้ status code 200 OK และรายการ ratings กลับมา ถือเป็น defect ด้าน authentication เพราะ token ปลอมยังอ่านข้อมูลได้ ในระบบจริงผู้ที่ไม่มีสิทธิ์อาจเข้าถึงข้อมูลของผู้อื่นได้

**8.** API test ตรวจสอบ status code, response body และข้อมูลที่ server บันทึกได้โดยตรง ส่วน UI test ตรวจสอบสิ่งที่ผู้ใช้เห็นและโต้ตอบได้ เช่น layout ปุ่ม และการแสดงผลบนหน้าจอ