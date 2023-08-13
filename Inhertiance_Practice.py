class MobilePhone:
     def __init__(self):
         self.ScreenType = "TouchScreen"
         self.NetworkType = "4G/5G"
         self.DualSim = True
         self.FrontCamera = "5MP"

     def make_call(self):
         print(f"Your are calling to ashok from,{self.PhoneType}")
     def receive_call(self):
         print("you have received spam call")

     def take_a_picture(self):
         pass

class ApplePhone(MobilePhone):
     def __init__(self,PhoneType):
         self.PhoneType = PhoneType
         super().__init__()
     def make_call(self):
         print("This is child class")
     def info(self):
         print(self.PhoneType,self.ScreenType)
Iphone_12 = ApplePhone("Apple12Pro")
ApplePhone.info(Iphone_12)
ApplePhone.make_call(Iphone_12)


class SamsungPhone(MobilePhone):
    def __init__(self,PhoneType):
        self.PhoneType = PhoneType
        super().__init__()

    def info(self):
        print(self.PhoneType, self.FrontCamera)
samsung = SamsungPhone("A50")
SamsungPhone.info(samsung)
SamsungPhone.receive_call(samsung)
print(samsung)




