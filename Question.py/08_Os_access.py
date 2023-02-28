import os 
ret =os.access(r"C:\Users\Lenovo\OneDrive\Desktop\backend",os.F_OK)
print ("F_OK - return value %s", ret)

ret1 =os.access(r"C:\Users\Lenovo\OneDrive\Desktop\python_lab",os.R_OK)
print ("R_OK - return value %s", ret1)

ret2 =os.access(r"C:\Users\Lenovo\OneDrive\Desktop\doremon",os.W_OK)
print ("W_OK - return value %s", ret2)

ret3 =os.access(r"C:\Users\Lenovo\OneDrive\Desktop\python_lab\Chapter_01\01_hello.py",os.X_OK)
print ("X_OK - return value %s", ret3)
