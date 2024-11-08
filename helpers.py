import random

class GenerateCustomData:
    def generate_custom_emale(self):
        base_name = "Dmitrii_Losunov"
        random_number = random.randint(100, 999)
        return f"{base_name}_15_{random_number}@yandex.ru"

    def generate_custom_password(self):
        random_password = random.randint(100000, 999999)
        return str(random_password)