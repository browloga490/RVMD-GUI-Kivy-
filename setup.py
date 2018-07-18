import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\Logoswego\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Logoswego\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("TestingGround.py")]

cx_Freeze.setup(
    name="Kivy GUI",
    options={"build_exe":{"packages":["pygame","kivy","matplotlib"],"include_files":["main.kv","image1.jpg","image2.jpg","image3.jpg","image4.jpg"]}},
    description = "Template GUI for Vibration Analysis Project",
    executables = executables
    )
