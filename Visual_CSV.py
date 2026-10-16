import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk


def veiwer(datax):
    data = pd.read_csv(datax)
    data_array = data.to_numpy()

    selected_data = data.to_numpy()

    root = tk.Tk()
    root.title("MP_Toolkit - Data Veiwer")
    root.geometry("900x500")

    table = ttk.Treeview(root, columns=list(data.columns), show="headings")

    for col in data.columns:
        table.heading(col, text=col)
        table.column(col, width=120)

    # Add all rows
    for row in data.itertuples(index=False, name=None):
        table.insert("", "end", values=row)

    # Add scrollbars
    scroll_y = ttk.Scrollbar(root, orient="vertical", command=table.yview)
    scroll_x = ttk.Scrollbar(root, orient="horizontal", command=table.xview)

    table.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    scroll_y.pack(side="right", fill="y")
    scroll_x.pack(side="bottom", fill="x")
    table.pack(fill="both", expand=True)

    root.mainloop()

veiwer("CassyData.csv")