class HTML:
    def __init__(self):
        self.content = []

    def ask_for_file(self):
        # Meminta pengguna memasukkan path file
        filename = input("Masukkan path file HTML: ")
        self.input(filename)

    def input(self, filename):
        try:
            # Membaca file
            with open(filename, 'r') as file:
                data = file.read()

            # Daftar tag yang perlu dipisahkan
            tags = ["<html", "</html", "<head", "</head", "<title", "</title", "<link", "<script", "</script", 
                    'rel="', 'href="', 'src="', 'id="', 'class="', 'style="', "<body", "</body"]

            # Memproses isi file
            for tag in tags:
                data = data.replace(tag, f"\n{tag}\n")

            # Memisahkan berdasarkan baris baru dan menghapus string kosong
            lines = [line.strip() for line in data.split("\n") if line.strip()]

            # Memisahkan tag penutup '>'
            for i, line in enumerate(lines):
                if line.endswith('>'):
                    lines[i] = line[:-1]
                    lines.insert(i + 1, '>')

            self.content = lines
        except FileNotFoundError:
            print("File tidak ditemukan. Silakan masukkan path yang valid.")

    def get_content(self):
        return self.content

# Contoh penggunaan
html_parser = HTML()
html_parser.ask_for_file()
print(html_parser.get_content())
