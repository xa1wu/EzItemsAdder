# app.py
from customtkinter import *
from tkinter import filedialog
from generator.font_generator import FontImageGenerator
from generator.item_generator import ItemGenerator
from generator.categories_generator import CategoriesGenerator  # Import CategoriesGenerator
from generator.utils import get_image_files

class App(CTk):

    def __init__(self):
        super().__init__()
        self.folder_label = None
        self.title("ItemsAdder Code Generator")
        self.geometry("700x700")

        # ค่าเริ่มต้น
        self.selected_folder = ""
        self.generator_type = StringVar(value="Font Image")

        self.init_ui()

    def init_ui(self):
        # Dropdown เลือกประเภท
        CTkLabel(self, text="Select Generator Type:").pack(pady=10)
        CTkOptionMenu(self, values=["Font Image", "Item", "Category"], variable=self.generator_type, command=self.on_type_change).pack() # เพิ่ม "Category"

        # ปุ่มเลือกโฟลเดอร์
        CTkButton(self, text="Select Folder", command=self.select_folder,corner_radius=32, hover_color="#C850C0").pack(pady=10)
        self.folder_label = CTkLabel(self, text="No folder selected")
        self.folder_label.pack()

        # เฟรมที่เปลี่ยน UI ตามประเภท
        self.dynamic_frame = CTkFrame(self)
        self.dynamic_frame.pack(pady=10, fill="x", padx=20)
        self.input_fields = {}

        # ปุ่ม Generate
        CTkButton(self, text="Generate", command=self.generate_code).pack(pady=10)
        self.output_box = CTkTextbox(self, width=600, height=300)
        self.output_box.pack(padx=20, pady=10)

        self.render_font_ui()  # ค่าเริ่มต้นคือ Font

    def on_type_change(self, value):
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()
        self.input_fields.clear()

        if value == "Font Image":
            self.render_font_ui()
        elif value == "Item":
            self.render_item_ui()
        elif value == "Category":  # เพิ่มเงื่อนไขสำหรับ Category
            self.render_category_ui()

    def render_font_ui(self):
        self.input_fields['namespace'] = self.create_input("Namespace")
        self.input_fields['permission'] = self.create_input("Permission")
        self.input_fields['scale'] = self.create_input("Scale Ratio", default="10")
        self.input_fields['ypos'] = self.create_input("Y Position", default="8")
        self.input_fields['show_gui'] = self.create_input("Show in GUI (true/false)", default="true")

    def render_item_ui(self):
        self.input_fields['namespace'] = self.create_input("Namespace")
        self.input_fields['material'] = self.create_input("Material", default="PAPER")
        self.input_fields['model_id_start'] = self.create_input("Start Model ID", default="10000")
        self.input_fields['model_path_prefix'] = self.create_input("Model Path Prefix (e.g. folder1/item_)")

    def render_category_ui(self):
        self.input_fields['namespace'] = self.create_input("Namespace")
        self.input_fields['category_name'] = self.create_input("Category Name", default="&eNew Category")
        self.input_fields['category_title'] = self.create_input("Category Title")
        self.input_fields['category_icon'] = self.create_input("Category Icon (namespace:item_id)", default="namespace:icon")
    def create_input(self, label, default=""):
        CTkLabel(self.dynamic_frame, text=label).pack(anchor="w", padx=10)
        entry = CTkEntry(self.dynamic_frame)
        entry.insert(0, default)
        entry.pack(fill="x", padx=10, pady=5)
        return entry

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder = folder
            self.folder_label.configure(text=folder)

    def generate_code(self):
        if not self.selected_folder:
            self.output_box.delete("1.0", "end")
            self.output_box.insert("end", "Please select a folder first.")
            return

        files = get_image_files(self.selected_folder)
        if not files:
            self.output_box.delete("1.0", "end")
            self.output_box.insert("end", "No .png files found in the selected folder.")
            return

        generator_type = self.generator_type.get()

        try:
            if generator_type == "Font Image":
                gen = FontImageGenerator(
                    files=files,
                    namespace=self.input_fields['namespace'].get(),
                    permission=self.input_fields['permission'].get(),
                    scale=self.input_fields['scale'].get(),
                    ypos=self.input_fields['ypos'].get(),
                    show_gui=self.input_fields['show_gui'].get()
                )
                code = gen.generate()
            elif generator_type == "Item":
                gen = ItemGenerator(
                    files=files,
                    namespace=self.input_fields['namespace'].get(),
                    model_id_start=self.input_fields['model_id_start'].get(),
                    model_path_prefix=self.input_fields['model_path_prefix'].get(),
                    material=self.input_fields['material'].get()
                )
                code = gen.generate()
            elif generator_type == "Category": # เพิ่มเงื่อนไขสำหรับ Category
                gen = CategoriesGenerator(
                    files=files,
                    namespace=self.input_fields['namespace'].get(),
                    category_name=self.input_fields['category_name'].get(),
                    category_title=self.input_fields['category_title'].get(),
                    category_icon=self.input_fields['category_icon'].get()
                )
                code = gen.generate()

            self.output_box.delete("1.0", "end")
            self.output_box.insert("end", code)

        except Exception as e:
            self.output_box.delete("1.0", "end")
            self.output_box.insert("end", f"Error: {e}")


if __name__ == "__main__":
    set_appearance_mode("Dark")  # หรือ "Light"
    set_default_color_theme("blue")  # เปลี่ยนได้ตามต้องการ
    app = App()
    app.mainloop()