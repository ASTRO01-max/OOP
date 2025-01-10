class Pupil:
    def __init__(self, name, fam, year, room, hobby):
        self.name = name
        self.fam = fam
        self.year = year
        self.room = room
        self.hobby = hobby
 
    def save_student(self):
        file_path = "student.txt"
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(self.full_name())
            file.write(self.get_age())
            file.write(self.class_room())
            file.write(self.join_subject())
            file.write("\n")

    def full_name(self):
        return f"O'quvchi: {self.fam} {self.name}\n"

    def get_age(self):
        return f"Tug'ilgan yili va yoshi: {self.year}, {2025 - self.year} yosh\n"

    def ClassRoom(self):
        return f"Sinf: {self.room}\n"

    def join_subject(self):
        return f"Qiziqadigan fani: {self.hobby}\n"

student = Pupil("MuhammadYusuf", "G'aybullayev", 2008, "10-B 2024", "Python")

print(student.full_name())
print(student.get_age())
print(student.ClassRoom())
print(student.join_subject())

file_path = "student.txt"
with open(file_path, "a") as file:
    file.write(student.full_name())
    file.write(student.get_age())
    file.write(student.ClassRoom())
    file.write(student.join_subject())
    # file.write("-" * 30 + "\n")  # Ajratish chizig'i

