## Part A: Input Space Partitioning for Ratings

### Step A1: Input Domain Model

คำสั่ง `POST /api/ratings` ใช้สร้าง rating โดยรับ `pizza_id` และ `stars` ใน request body พร้อม token ของผู้ใช้ใน header

แบ่ง input ออกเป็น 4 characteristics ตามเงื่อนไขของ API โดยเลือก base block เป็นค่าที่ถูกต้องและใช้งานทั่วไป

| Characteristic | Blocks | Values in the tests |
|---|---|---|
| C1 Value of stars | below 1, 1 to 5 (base), above 5 | 0, 3, 6 |
| C2 Type of stars | whole number (base), decimal, text, missing | 3, 3.5, "3", no field |
| C3 Pizza | exists (base), does not exist | a new pizza, 999999999 |
| C4 Token | the user's own (base), none, wrong length | from auth, no header, short token |

### Step A2: Test Coverage for POST /api/ratings

ใช้แนวทาง Base Choice Coverage โดยเริ่มจาก test ที่ใช้ base block ของทุก characteristic จากนั้นเปลี่ยน input ทีละ characteristic ไปยัง block อื่น โดยคง characteristic ที่เหลือไว้ที่ base

| Characteristic | Block | Test |
|---|---|---|
| C1: Value of stars | Below 1 | `test_stars_out_of_range[0]` |
| C1: Value of stars | 1 to 5 (base) | `test_base_choice_is_saved` |
| C1: Value of stars | Above 5 | `test_stars_out_of_range[6]` |
| C2: Type of stars | Whole number (base) | `test_base_choice_is_saved` |
| C2: Type of stars | Decimal | `test_stars_decimal_is_refused` |
| C2: Type of stars | Text | `test_stars_text_is_refused` |
| C2: Type of stars | Missing | `test_stars_missing_is_refused` |
| C3: Pizza | Exists (base) | `test_base_choice_is_saved` |
| C3: Pizza | Does not exist | `test_pizza_not_found_is_refused` |
| C4: Token | Own token (base) | `test_base_choice_is_saved` |
| C4: Token | No token | `test_missing_token_is_refused` |
| C4: Token | Wrong token | `test_invalid_token_is_refused` |

**ผลการทดสอบ:** `pytest -v` ได้ผล **25 passed, 1 xfailed** 