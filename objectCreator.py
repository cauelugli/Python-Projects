class Instance:
    def __init__(self, xx, yy, zz):
        self.x = xx
        self.y = yy
        self.z = zz

    def printfunc(self):
        print("Result:\n",
              "\nX: ", self.x,
              "\nY: ", self.y,
              "\nZ: ", self.z)


xxx = 1.0 // 2 + 0
yyy = "Y"
zzz = True

call = Instance(xxx, yyy, zzz)

call.printfunc()
