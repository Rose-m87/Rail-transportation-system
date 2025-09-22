def admin_panel(admin_user: User):
    while True:
        print("\n--- پنل مدیریتی (ادمین) ---")
        print("1) اضافه‌کردن کارمند قطار")
        print("2) حذف کارمند قطار")
        print("3) مشاهده لیست کارمندان")
        print("4) خروج از مدیریت")
        c = input("انتخاب: ").strip()
        if c == "1":
            add_staff()
        elif c == "2":
            remove_staff()
        elif c == "3":
            list_staff()
        elif c == "4":
            print("بازگشت به منوی شروع.")
            return
        else:
            print("نامعتبر.")

def add_staff():
    print("\nافزودن کارمند:")
    first = input("نام: ").strip()
    last = input("نام‌خانوادگی: ").strip()
    email = input("ایمیل: ").strip()
    username = input("نام کاربری: ").strip()
    password = input("رمز عبور: ").strip()

    if username in USERS or username in STAFF_CREDS:
        print("❌ نام کاربری تکراری است.")
        return
    if any(u.email == email for u in USERS.values()):
        print("❌ ایمیل تکراری است.")
        return
    if not valid_username(username) or not valid_password(password) or not valid_email(email):
        print("❌ اعتبارسنجی ناموفق. الگوی نام/رمز/ایمیل را رعایت کنید.")
        return

    user = User(username, password, email, first, last, role="staff")
    USERS[username] = user
    STAFF_CREDS[username] = password
    print("✅ کارمند افزوده شد.")

def remove_staff():
    print("\nحذف کارمند:")
    username = input("نام کاربری کارمند: ").strip()
    if username in STAFF_CREDS and username in USERS and USERS[username].role == "staff":
        del STAFF_CREDS[username]
        del USERS[username]
        print("✅ حذف شد.")
    else:
        print("❌ چنین کارمندی وجود ندارد.")

def list_staff():
    print("\n--- لیست کارمندان ---")
    any_staff = False
    for u in USERS.values():
        if u.role == "staff":
            any_staff = True
            print(f"- {u.username} | {u.full_name()} | {u.email}")
    if not any_staff:
        print("هیچ کارمندی ثبت نشده است.")
