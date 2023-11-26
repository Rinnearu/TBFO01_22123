import re

class HTML:
    def __init__(self):
        self.file_name = input("Masukkan nama file HTML: ")
        self.content = []

    def read_and_process_file(self):
        try:
            with open(self.file_name, 'r') as file:
                data = file.read()

            temp = ""
            outside_text = ""
            for char in data:
                if char == '<':
                    if outside_text.strip():  # Jika ada teks di luar tag
                        self.content.append('T')
                        outside_text = ""
                    temp = char
                elif char == '>':
                    temp += char
                    self._process_tag(temp)
                    temp = ""
                else:
                    if temp:
                        temp += char
                    else:
                        outside_text += char

            if outside_text.strip():  # Menangani teks yang tersisa
                self.content.append('T')

        except FileNotFoundError:
            print("File tidak ditemukan. Pastikan path file sudah benar.")

    def _process_tag(self, tag):
        if tag.startswith('<!--') and tag.endswith('-->'):
            self.content.append('<!--')
            self.content.append('-->')
        else:
            parts = tag[:-1].split(' ', 1)
            self.content.append(parts[0])
            if len(parts) > 1:
                attributes = re.findall(r'(\w+)="([^"]*)"', parts[1])
                for attr, value in attributes:
                    self.content.append(attr + '="')
                    self.content.append('T ')  # Mengosongkan nilai atribut
                    self.content.append('"')
            self.content.append('>')

    def get_content(self):
        return self.content

# Menggunakan class
html_reader = HTML()
html_reader.read_and_process_file()
content = html_reader.get_content()
print(content)