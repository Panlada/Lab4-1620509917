from cmath import pi


class cylinders():
    def __init__(self,Radius,Height) -> None:
        self.Radius = Radius
        self.Height = Height

cylinders1 = cylinders(Radius=5,Height=10)

volumofc = pi*cylinders1.Radius*cylinders1.Height
print("Volum of cylinder1 =:",volumofc)

cylinders2 = cylinders(Radius=7,Height=13)

volumofc2 = pi*cylinders2.Radius*cylinders2.Height
print("Volum of cylinder2 = :",volumofc2)

    