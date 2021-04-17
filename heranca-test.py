class Back:
    def __init__(self, command, user_name):
        self.name       = "Haru"
        self.id         = "id"
        self.cmd        = command
        self.user_name  = user_name


    def req(self):
        info = {
            "name":self.name, 
            "id":self.id, 
            "command":self.cmd, 
            "userName":self.user_name 
        }
        return info


class Front(Back):
    def __init__(self, command, user_name):
        super().__init__(command, user_name)
        

if __name__ == "__main__":

    while True:
        u_name = input("Into your name: ")
        cmd    = input("Use any command: ")

        obj = Front(cmd, u_name)
        info = obj.req()
        print(info)
