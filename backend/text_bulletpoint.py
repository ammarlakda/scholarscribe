import pyperclip
   

def bullet(summarized_text): 
    # saves text copied to clipboard
    # in variable text
    text = pyperclip.copy(summarized_text)
    text = pyperclip.paste()
    
    # stores different lines of text
    # in a list named lines
    lines = text.split(".")
    
    # adds * to every line stored
    # in list
    for i in range(len(lines)):
        lines[i] = "." + lines[i]
    
    # converts the list of different
    # lines to single text
    text = "\n".join(lines)
    
    # copies new modified text
    # to the clipboard
    pyperclip.copy(text) 
    return pyperclip.paste()
