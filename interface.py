import json
import tkinter as tk
from tkinter import ttk
from webbrowser import open as open_url
from utils import search
from tkinter import messagebox


# Load the JSON data
with open('articleBD.json') as json_file:
    data = json.load(json_file)

# Declare the sorted_results variable globally
sorted_results = []

# Function to execute when the search button is pressed
def on_search():
    global sorted_results
    query = search_entry.get()
    results = search(query, data)
    if not results:
        results_list.insert(tk.END, "No results found.")
        return
    sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
    results_list.delete(0, tk.END)
    for idx, result in enumerate(sorted_results):
        results_list.insert(tk.END, f"{idx+1}. {result['title']} (Score: {result['score']})  (Date : {result['date']})")

# Function to open the URL when a list item is double-clicked
def on_result_click(event):
    global sorted_results
    selection = results_list.curselection()
    if selection:
        selected_index = selection[0]
        url = sorted_results[selected_index]['url']
        open_url(url)
# Create the main window
root = tk.Tk()
root.title("The WORST Article Search made by the WORST programmer")

# Create and pack the search frame
search_frame = ttk.Frame(root, padding="10")
search_frame.pack(fill="x")

# Create and pack the search entry and button
search_entry = ttk.Entry(search_frame, width=55)
search_entry.pack(side="left")
search_button = ttk.Button(search_frame, text="Search", command=on_search)
search_button.pack(side="left", padx=(10, 0))

# Create and pack the results listbox
results_list = tk.Listbox(root, width=100, height=20, font=('Arial', 12), selectmode='none', highlightcolor='blue')
results_list.pack(fill="both", expand=True, padx=(10, 10), pady=(10, 0))

# Add a scrollbar to the listbox
scrollbar = ttk.Scrollbar(root, orient="vertical", command=results_list.yview)
scrollbar.pack(side="right", fill="y")
results_list.configure(yscrollcommand=scrollbar.set)

# Bind the double-click event to the results listbox
results_list.bind("<Double-1>", on_result_click)

# Start the main event loop
root.mainloop()

