import os

class FontImageGenerator:
    def __init__(self, files, namespace, permission, scale, ypos, show_gui):
        self.files = files
        self.namespace = namespace
        self.permission = permission
        self.scale = scale
        self.ypos = ypos
        self.show_gui = show_gui

    def generate(self):
        output = f"info:\n  namespace: \"{self.namespace}\"\nfont_images:\n"
        for file in self.files:
            name = os.path.splitext(file)[0]
            output += f"  {name}:\n"
            output += f"    permission: {self.permission}\n"
            output += f"    path: \"{name}\"\n"
            output += f"    scale_ratio: {self.scale}\n"
            output += f"    y_position: {self.ypos}\n"
            output += f"    show_in_gui: {str(self.show_gui).lower()}\n"
        return output
