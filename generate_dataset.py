import random


def generate_dataset(file_name: str, number_of_entries: int):
    with open(file_name, "w") as arquivo:
        for _ in range(number_of_entries):
            valor = random.randint(1, 100)
            arquivo.write(f"{valor}\n")


generate_dataset(file_name="example3.txt", number_of_entries=1000)
