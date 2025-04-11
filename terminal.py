from backend_folder.db_model import insert_measurement,init_db
from backend_folder.utility import calculate_real_size

init_db()

username = input("Enter username: ")
microscope_size = float(input("Enter microscope size: "))
magnification = float(input("Enter magnification: "))
actual_size = calculate_real_size(microscope_size, magnification)

insert_measurement(username, microscope_size, actual_size)

print(f"Actual size: {actual_size:.2f} units")
