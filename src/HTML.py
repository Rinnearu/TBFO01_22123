import re

class HTML:
    def __init__(self):
        self.content = []

    def ask_for_file(self):
        # Meminta pengguna memasukkan path file
        filename = input("Masukkan path file HTML: ")
        self.input(filename)

    def input(self, filename):
        try:
            with open(filename, 'r') as file:
                data = file.read()

            # Menghapus newline
            data = data.replace('\n', '')

            # Membuat ekspresi reguler untuk tag yang spesifik
            tags_pattern = re.compile(
                r"(<html|</html|<head|</head|<title|</title|<link|<script|</script|"
                r"rel=\"|href=\"|src=\"|id=\"|class=\"|style=\"|<body|</body)"
            )

            # Memisahkan data menggunakan ekspresi reguler
            parts = tags_pattern.split(data)
            cleaned_parts = [part.strip() for part in parts if part.strip()]

            # Memasukkan hasil split ke dalam list content
            for part in cleaned_parts:
              self.content.append(part)

        except FileNotFoundError:
            print("File tidak ditemukan. Silakan masukkan path yang valid.")

    def get_content(self):
        return self.content

# Contoh penggunaan
html_parser = HTML()
html_parser.ask_for_file()
print(html_parser.get_content())
