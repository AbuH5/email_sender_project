import json

class FileLoader:
    @staticmethod
    def load_json(filepath):
        try:
            with open(filepath, "r") as file:
                return json.load(file)
        except Exception as e:
            raise Exception(f"Error loading JSON file {filepath}: {e}")

    @staticmethod
    def load_txt(filepath):
        try:
            with open(filepath, "r") as file:
                return [line.strip() for line in file if line.strip()]
        except Exception as e:
            raise Exception(f"Error loading TXT file {filepath}: {e}")
