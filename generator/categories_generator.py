import os

class CategoriesGenerator:
    def __init__(self, files, namespace, category_name, category_title, category_icon):
        self.files = files
        self.namespace = namespace
        self.category_name = category_name
        self.category_title = category_title
        self.category_icon = category_icon

    def generate(self):
        output = f"info:\n  namespace: \"{self.namespace}\"\ncategories:\n"
        output += f"  {self.namespace}:\n"
        output += f"    enabled: true\n"
        output += f"    name: \"{self.category_name}\"\n"
        output += f"    title: \"{self.category_title}\"\n"
        output += f"    icon: \"{self.category_icon}\"\n"
        output += "    items:\n"
        for file in self.files:
            name = os.path.splitext(file)[0]
            output += f"      - \"{self.namespace}:{name}\"\n"
        return output