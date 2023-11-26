class HTML:
    def __init__(self):
        self.file_name = input("Masukkan nama file HTML: ")
        self.content = []

    def read_and_process_file(self):
        try:
            with open(self.file_name, 'r') as file:
                data = file.read()
                #contoh isi data adalah "<html> <head> <title> Ini adalah judul </title> </head> <body> <p> Ini adalah paragraf </p> </body> </html>"

            temp = ""
            in_comment = False
            flag_close = False
            for char in data:
                #contoh isi char adalah "<"
                if char == '<':
                    # Menangani teks sebelum tag
                    if temp and not flag_close:
                        self.content.extend(temp.split())
                        flag_close = False
                    temp = char
                elif char == '>':
                    temp += char
                    # Memeriksa apakah 4 char pertama adalah <!--
                    if temp.startswith('<!--') and temp.endswith('-->'):
                        self.content.append('<!--')
                        self.content.append('-->')
                        temp = ""
                    else:
                        # Memproses tag biasa
                        self.content.append(temp[:-1])
                        # temp = "<html>"
                        # maka temp[:-1] = "<html"
                        self.content.append(temp[-1])
                        temp = ""
                    flag_close = True
                else:
                    temp += char

            # Menangani teks yang tersisa
            if temp and not in_comment:
                self.content.extend(temp.split())

        except FileNotFoundError:
            print("File tidak ditemukan. Pastikan path file sudah benar.")

    def get_content(self):
        return self.content

# Menggunakan class
html_reader = HTML()
html_reader.read_and_process_file()
content = html_reader.get_content()
print(content)