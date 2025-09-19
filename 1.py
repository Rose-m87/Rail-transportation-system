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
        self.lines_listt = []
        self.lines_dict = {}

    def add_line(self, lines_name, origin, destination, stations):
        if lines_name == "":
            print("name is empty")
            return
        if origin == "":
            print("origin is empty")
            return
        if destination == "":
            print("destination is empty")
            return
        stations=[s.strip() for s in stations if s.strip()]
        if not stations:
            print("stations list is empty")
            return
        for line in self.lines_listt:
            if line[0].lower() == lines_name.lower():
                print("This name exists, enter another name")
                return
        line_record = [lines_name, origin, destination, stations]
        self.lines_listt.append(line_record)
        self.all_info
        print(f"line '{lines_name}' added successfully")

    def all_info(self):
        self.lines_dict = {}
        for i in range(len(self.lines_listt)):
            key_ = self.lines_listt[i][0]
            self.lines_dict[key_] = self.lines_listt[i]

    def update_lines_info(self, lines_name=None):
        while True:
            if not lines_name:
                lines_name = input("enter line name (or type 'back' to return): ").strip()
                if lines_name.lower() == "back":
                    return
            record = None
            for key in self.lines_dict:
                if key.lower() == lines_name.lower():
                    record = self.lines_dict[key]
                    lines_name = key
                    break
            if not record:
                print("Line name not found.")
                lines_name = None
                continue
            while True:
                print(f"1) name: {record[0]}")
                print(f"2) origin: {record[1]}")
                print(f"3) destination: {record[2]}")
                print(f"4) stations: {', '.join(record[3])}")
                choice = input("which one do you want to update? (1/2/3/4 or b): ").strip().lower()
                if choice in ("b"):
                    return
                if choice == "1":
                    new_name = input("enter new name: ").strip()
                    if new_name == "":
                        print("name cannot be empty")
                        continue
                    if any(k.lower() == new_name.lower() and k.lower() != lines_name.lower() for k in self.lines_dict):
                        print("this name exists")
                        continue
                    record[0] = new_name
                    self.all_info()
                    lines_name = new_name
                    print("name updated")
                elif choice == "2":
                    new_origin = input("enter new origin: or back ").strip()
                    if new_origin.lower() == "back":
                        return
                    if new_origin == "":
                        print("origin cannot be empty")
                        continue
                    record[1] = new_origin
                    self.all_info()
                    print("origin updated")
                elif choice == "3":
                    new_destination = input("enter new destination: or back ").strip()
                    if new_destination.lower() == "back":
                        return
                    if new_destination == "":
                        print("destination cannot be empty")
                        continue
                    record[2] = new_destination
                    self.all_info()
                    print("destination updated")
                elif choice == "4":
                    new_stations =[ s.strip() for s in  input("enter stations separated by commas: ").split(",") if s.strip()]
                    if not new_stations:
                        print("stations cannot be empty")
                        continue
                    record[3] = new_stations
                    self.all_info()
                    print("stations updated")
                else:
                    print("invalid choice")


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
panel = empoloyee_panel()
while True:
    lines_name = input("inter line name :").strip()
    if lines_name.lower() == "back":
        break
    origin = input("enter origin: ").strip()
    if origin.lower() == "back":
        break
    destination = input("enter destination: ").strip()
    if destination.lower() == "back":
        break
    stations = input("enter stations separated by cammas: ").strip().split(",")
    panel.add_line(lines_name, origin, destination, stations)
    continue_ = input("do you want to add another line? (y/n): ").strip().lower()
    if continue_ not in ("yes","y"):
        break
while True:
    lines_name=input("enter line name :").strip()
    if lines_name.lower()=="back":
        break
    panel.update_lines_info(lines_name)
    continue_=input("do want to update another line ? (y/yes): ").strip().lower()
    if continue_ not in("yes","y"):
        break
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

