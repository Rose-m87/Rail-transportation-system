class admin:
    def __init__(self,username,password):
        pass
    def authenticate(self, input_username, input_password):
        pass
class admin_panel:
    def __init__(self):
        pass
    def add_employee(self,name,lastname,password,username):
        pass
    def delet_employee(self,username):
        pass
    def employeed_list(self):
        pass
    def log_out(self):
        pass
class train_employee:
    def __init__(self,username,password):
        pass
    def authenticate(self, input_username, input_password):
        pass
class empoloyee_panel:
    def __init__(self):
        self.lines_listt=[]

    def add_line(self,lines_name,origin,destination,stations):
        if lines_name=="":
            return
        if origin=="":
            return
        if destination=="":
            return
        if not stations:
            return
        for line in self.lines_listt:
            if line[0]==lines_name:
                print("This name exists, enter another name")
                return
        line_record=[lines_name,origin,destination,stations]
        self.lines_listt.append(line_record)
        print(f"line'{lines_name}'added successfully")
panel=empoloyee_panel()
while True:
    lines_name=input("inter line name :")
    origin=input("enter origin: ")
    destination=input("enter destination: ")
    stations=input("enter stations separated by cammas: ").split(",")
    panel.add_line(lines_name,origin,destination,stations)
    continue_=input("do you want to add another line?")
    if continue_.lower()!="yes":
        break
    def update_lines_info(self,lines_name):
        pass
    def delet_line(self,lines_name):
        pass
    def lines_list(self):
        pass
    def add_train(self,trains_name,move_line,av_v,stop_rate,stations,quality_grade,ticket_price,train_capacity,id):
        pass
    def update_trian_info(self,id):
        pass
    def delet_train(self,id):
        pass
    def trains_list(self):
        pass
    def log_out(self):
        pass
class normal_user:
    def __init__(self):
        pass
    def sign_in(self,name,user_name,password,email):
        pass
    def log_in(self,user_name,password):
        pass
    def log_out(self):
        pass
class shopping:
    def __init__(self):
        pass
    def wallet(self):
        pass
    def edit_info(self):
        pass

