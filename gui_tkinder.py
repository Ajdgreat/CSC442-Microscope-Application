import tkinter as tk
from backend_folder.database import SessionLocal
from backend_folder.db_model import Measurement
from backend_folder.utility import calculate_real_size

def submit():
    username = entry_user.get()
    size = float(entry_size.get())
    magnification = float(entry_magnification.get())
    actual = calculate_real_size(size, magnification)
    
    db = SessionLocal()
    db.add(Measurement(username=username, microscope_size=size, actual_size=actual))
    db.commit()
    db.close()

    result_label.config(text=f"Actual size: {actual:.2f} units")

root = tk.Tk()
root.title("Microscope Size Calculator")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Microscope Size").pack()
entry_size = tk.Entry(root)
entry_size.pack()

tk.Label(root, text="Magnification").pack()
entry_magnification = tk.Entry(root)
entry_magnification.pack()

tk.Button(root, text="Calculate", command=submit).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
