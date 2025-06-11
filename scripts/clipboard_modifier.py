import re

import pyperclip


# Create a dictionary of command actions based on predefined screen positions
def modify_copied_content(target_variable, replacement_value):
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
    print("Modified content copied to clipboard!")
