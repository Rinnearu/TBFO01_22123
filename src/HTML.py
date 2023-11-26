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
            in_comment = False
            flag_close = False  # Menginisialisasi flag_close
            for char in data:
                if char == '<':
                    if temp and not in_comment and not flag_close:
                        self.content.extend(temp.split())
                    temp = char
                    flag_close = False  # Reset flag ketika menemui '<'
                elif char == '>':
                    temp += char
                    if temp.startswith('<!--') and temp.endswith('-->'):
                        self.content.append('<!--')
                        self.content.append('-->')
                        temp = ""
                    else:
                        if temp.startswith('<link'):
                            self._process_link_tag(temp)
                        else:
                            self.content.append(temp[:-1])
                            self.content.append(temp[-1])
                        temp = ""
                    flag_close = True  # Set flag ketika menemui '>'
                else:
                    temp += char

            if temp and not in_comment and not flag_close:
                self.content.extend(temp.split())

        except FileNotFoundError:
            print("File tidak ditemukan. Pastikan path file sudah benar.")

    def _process_link_tag(self, tag):
        # Ekstrak atribut dari tag <link>
        attributes = re.findall(r'(\w+)="([^"]*)"', tag)
        link_data = ['<link']
        for attr, value in attributes:
            link_data.append(attr + '="')
            link_data.append('"')
            # link_data.append(value + '"')
        link_data.append('>')
        self.content.extend(link_data)

    def get_content(self):
        return self.content

# Menggunakan class
html_reader = HTML()
html_reader.read_and_process_file()
content = html_reader.get_content()
print(content)
