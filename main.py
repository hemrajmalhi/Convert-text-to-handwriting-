import pywhatkit as pw
text = """Parsing means taking a format like HTML and using a programming language to give it structure. For example, transforming data into an object. Now, to start this task of creating a web scraper with Python, you need to install a module named BeautifulSoup."""
pw.text_to_handwriting(text, "demo3.png",[255,0,0])
print("End")


