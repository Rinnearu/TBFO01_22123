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
print(f"Processing HTML file: {filename}")
# Use 'filename' to work with the provided HTML file