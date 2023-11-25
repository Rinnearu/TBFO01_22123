import re

def extract_tags_separately(html_input):
    # Define a regular expression pattern to match opening, closing, and self-closing HTML tags
    pattern = r'<[^/>]+>|</[^>]+>|<[^>]+/>'

    # Find all matches of HTML tags in the input
    tags = re.findall(pattern, html_input)

    return tags

# Example HTML input
html_input = """
<html> 
  <head> 
    <title>Simple Webpage</title> 
  </head> 
  <body> 
    <h1>Hello, World!</h1> 
    <p>This is a simple webpage.</p> 
  </body> 
</html>
"""

# Extract tags separately from the HTML input
extracted_tags = extract_tags_separately(html_input)
print(extracted_tags)