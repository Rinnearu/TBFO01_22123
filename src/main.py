import argparse
from PDA import PDA
from HTML import HTML

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Process HTML file.')

# Add an argument for the filename
parser.add_argument('filename', help='HTML file to process')

# Parse the command-line arguments
args = parser.parse_args()

# Retrieve the filename from the parsed arguments
filename = args.filename

# Your main code here using the 'filename' variable
pda = PDA()
pda.read_pda('PDA.txt')

html_reader = HTML(filename)
html_reader.read_and_process_file()
content = html_reader.get_content()

if (pda.simulate(content)):
    print("Accepted")
else :
    print("Syntax error")
# Use 'filename' to work with the provided HTML file