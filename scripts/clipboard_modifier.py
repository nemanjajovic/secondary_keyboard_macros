import re

import pyperclip


def modify_copied_content(target_variable, replacement_value):
    content = (
        pyperclip.paste()
    )  # Content must already be copied to clipboard for tis to work
    modified_lines = []

    # Regular expression to find and replace the entire value
    pattern = rf"^{target_variable}\s*=\s*'.*'"  # Matches: local keyboardIdentifier = 'old_value'

    for line in content.split("\n"):
        if re.match(pattern, line):
            line = f"{target_variable} = {replacement_value}"
        modified_lines.append(line)

    modified_content = "\n".join(modified_lines)
    pyperclip.copy(modified_content)
    print("Modified content copied to clipboard!")
