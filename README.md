# XSSGen

**XSSGen** is a Python tool designed to generate random XSS (Cross-Site Scripting) payloads. The tool can create a variety of payloads with random HTML tags, JavaScript events, and JavaScript code snippets to help security testers identify vulnerabilities in web applications.

## Features

- **Random Payload Generation:** Generates XSS payloads with random combinations of HTML tags, JavaScript events, and JavaScript code.
- **Customizable Output:** Allows customization of payload styles, including the use of different HTML attributes and CSS styles.
- **Colorful Banners:** Displays a colorful banner using ASCII art to enhance the user experience.

## Usage

1. **Install the required packages:**
   ```sh
   pip install pyfiglet
   pip install termcolor
 ```

python xssgen.py

Enter the number of payloads you want to generate: 3


   ____  _________  _________
  / __ \/ ___/ __ \/ ___/ __ \
 / /_/ / /  / /_/ / /  / /_/ /
/ ____/ /__/ ____/ /__/ _, _/
/_/    \___/_/    \___/_/ |_|

Payload 1: <script onerror="alert('XSS')" a="bcdefghijk">
Payload 2: <img onload="alert('XSS')" style="color:75px;">
Payload 3: <div onmouseover="document.cookie" z="abcdefghij">



## Section Explanation:

    Title: Displays the tool's name prominently.
    Description: Describes the tool and its primary function.
    Features: Lists the key features of the tool.
    Usage: Explains how to install and run the tool.
    Example: Provides a practical example of how to use the tool and what to expect.
    License: Specifies the license type used for the project.
    Contributing: Invites users to contribute to the project.
    Disclaimer: Clarifies the legal and ethical use of the tool.






