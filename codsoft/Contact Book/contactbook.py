import tkinter as tk
from tkinter import messagebox, Listbox, END, SINGLE

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        # Define colors
        self.bg_color = "#D3E3F4"
        self.button_color = "#F1948A"
        self.entry_color = "#E6E6E6"

        # Configure root window
        self.root.configure(bg=self.bg_color)

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Name Label and Entry
        self.label_name = tk.Label(self.root, text="Name", bg=self.bg_color)
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self.root, bg=self.entry_color)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        # Contact Number Label and Entry
        self.label_contact = tk.Label(self.root, text="Contact No.", bg=self.bg_color)
        self.label_contact.grid(row=1, column=0, padx=10, pady=5)
        self.entry_contact = tk.Entry(self.root, bg=self.entry_color)
        self.entry_contact.grid(row=1, column=1, padx=10, pady=5)

        # Email Label and Entry
        self.label_email = tk.Label(self.root, text="Email", bg=self.bg_color)
        self.label_email.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email = tk.Entry(self.root, bg=self.entry_color)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        # Address Label and Entry
        self.label_address = tk.Label(self.root, text="Address", bg=self.bg_color)
        self.label_address.grid(row=3, column=0, padx=10, pady=5)
        self.entry_address = tk.Entry(self.root, bg=self.entry_color)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        self.button_add = tk.Button(self.root, text="ADD", command=self.add_contact, bg=self.button_color)
        self.button_add.grid(row=4, column=0, padx=10, pady=5)
        self.button_edit = tk.Button(self.root, text="EDIT", command=self.edit_contact, bg=self.button_color)
        self.button_edit.grid(row=4, column=1, padx=10, pady=5)
        self.button_delete = tk.Button(self.root, text="DELETE", command=self.delete_contact, bg=self.button_color)
        self.button_delete.grid(row=5, column=0, padx=10, pady=5)
        self.button_view = tk.Button(self.root, text="VIEW", command=self.view_contacts, bg=self.button_color)
        self.button_view.grid(row=5, column=1, padx=10, pady=5)
        self.button_search = tk.Button(self.root, text="SEARCH", command=self.search_contact, bg=self.button_color)
        self.button_search.grid(row=6, column=0, padx=10, pady=5)
        self.button_reset = tk.Button(self.root, text="RESET", command=self.reset_fields, bg=self.button_color)
        self.button_reset.grid(row=6, column=1, padx=10, pady=5)
        self.button_exit = tk.Button(self.root, text="EXIT", command=self.root.quit, bg="red")
        self.button_exit.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        # Listbox for displaying contacts
        self.listbox_contacts = Listbox(self.root, selectmode=SINGLE, bg=self.entry_color)
        self.listbox_contacts.grid(row=0, column=2, rowspan=8, padx=10, pady=5)

    def add_contact(self):
        name = self.entry_name.get()
        contact = self.entry_contact.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        if name and contact:
            self.contacts.append({"name": name, "contact": contact, "email": email, "address": address})
            messagebox.showinfo("Success", "Contact added successfully")
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Please fill in Name and Contact No.")

    def edit_contact(self):
        selected_index = self.listbox_contacts.curselection()
        if selected_index:
            name = self.entry_name.get()
            contact = self.entry_contact.get()
            email = self.entry_email.get()
            address = self.entry_address.get()
            if name and contact:
                self.contacts[selected_index[0]] = {"name": name, "contact": contact, "email": email, "address": address}
                messagebox.showinfo("Success", "Contact updated successfully")
                self.view_contacts()
            else:
                messagebox.showerror("Error", "Please fill in Name and Contact No.")
        else:
            messagebox.showerror("Error", "Please select a contact to edit")

    def delete_contact(self):
        selected_index = self.listbox_contacts.curselection()
        if selected_index:
            self.contacts.pop(selected_index[0])
            messagebox.showinfo("Success", "Contact deleted successfully")
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Please select a contact to delete")

    def view_contacts(self):
        self.listbox_contacts.delete(0, END)
        for contact in self.contacts:
            self.listbox_contacts.insert(END, f"{contact['name']} - {contact['contact']}")

    def search_contact(self):
        query = self.entry_name.get()
        self.listbox_contacts.delete(0, END)
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['contact']:
                self.listbox_contacts.insert(END, f"{contact['name']} - {contact['contact']}")

    def reset_fields(self):
        self.entry_name.delete(0, END)
        self.entry_contact.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_address.delete(0, END)
        self.listbox_contacts.selection_clear(0, END)

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
