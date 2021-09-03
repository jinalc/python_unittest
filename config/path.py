import os

current_folder = os.path.dirname(os.path.abspath(__file__))
init_file = os.path.join(current_folder, "config.ini")
print(init_file)