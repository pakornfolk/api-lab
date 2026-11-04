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