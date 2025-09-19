import re
def validation(user_name,email,name,password):
    user_name_pattern=r"^\w+\_\w+$"
    email_pattern=r"^\w+@\w+\.\w+.com\Z$"
    password_pattern=r"^\w+{8:}@\d+$"
    name_pattern=r"^\w+$"
    if re.match(user_name_pattern,user_name):
        pass #بازگشت به منو کاربر  عادی
    if re.match(email_pattern,email):
        pass #بازگشت به منو کاربر عادی
    if re.match(password_pattern,password):
        pass #بازگشت به منو کاربر عادی
    if re.match(name_pattern,name):
        pass #بازگشت به منو کاربر عادی
user_list=[]
for user_name,email,name,password in user_list:#بررسی تکراری بودن 
    if user_name in user_list and email in user_list and name in user_list and password in user_list:
        print("شما قبلا ثبت نام کرده اید، گزینه ورود را انتخاب کنید") #پیامی که نشون میده اگه تکراری باشه
        pass #کد برای بازگشت به منو شروع





