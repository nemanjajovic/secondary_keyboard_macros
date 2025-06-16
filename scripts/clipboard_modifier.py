import re

import pyperclip

# Make sure the print() gets run only once
is_printed = False


# Create a dictionary of command actions based on predefined screen positions
def modify_copied_content(target_variable, replacement_value):
    global is_printed
    # Get the current clipboard content (assumes it's already been copied)
    content = pyperclip.paste()
    modified_lines = []

    # Regex pattern to match a line like: local keyboardIdentifier = 'old_value'
    pattern = rf"^{target_variable}\s*=\s*'.*'"

    for line in content.split("\n"):
        # If the line matches the target pattern, replace its value
        if re.match(pattern, line):
            line = f"{target_variable} = {replacement_value}"
        modified_lines.append(line)

    # Combine modified lines and update the clipboard with the new content
    modified_content = "\n".join(modified_lines)
    pyperclip.copy(modified_content)

    # Make sure this gets printed only once
    if not is_printed:
        print("Modified content copied to clipboard!")
        is_printed = True
