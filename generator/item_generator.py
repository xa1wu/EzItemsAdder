import os

class ItemGenerator:
    def __init__(self, files, namespace, model_id_start, model_path_prefix, material):
        self.files = files
        self.namespace = namespace
        self.model_id_start = model_id_start
        self.model_path_prefix = model_path_prefix
        self.material = material

    def generate(self):
        output = f"info:\n  namespace: \"{self.namespace}\"\nitems:\n"
        for idx, file in enumerate(self.files):
            name = os.path.splitext(file)[0]
            model_id = self.model_id_start + idx
            output += f"  {name}:\n"
            output += f"    display_name: {name}\n"
            output += f"    resource:\n"
            output += f"      material: {self.material}\n"
            output += f"      model_id: {str(model_id)}\n"
            output += f"      generate: false\n"
            output += f"      model_path: {self.model_path_prefix}{name}\n"
        return output
