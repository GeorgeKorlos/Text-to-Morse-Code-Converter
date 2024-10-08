# Text-to-Morse Code Converter

This project is part of Angela Yu's 100 Days of Python course. The goal of this project is to create a simple program that converts text to Morse code and vice versa.

## Features

- Encode text into Morse code
- Decode Morse code back into text
- Interactive command-line interface for user input
- Handles letters (A-Z), numbers (0-9), and spaces

## How It Works

The program uses a dictionary to map each letter and number to its corresponding Morse code representation. Users can choose to either encode or decode their messages. The program then processes the input and outputs the result.

### Example

- **Encode**: 
    - Input: `HELLO`
    - Output: `.... . .-.. .-.. ---`

- **Decode**: 
    - Input: `.... . .-.. .-.. ---`
    - Output: `HELLO`

## Usage

1. Clone this repository to your local machine.
2. Run the script in your Python environment.
3. Follow the prompts to either encode or decode a message.

```bash
python text_to_morse.py
```

## Requirements

Python 3.x

## License

This project is open source and available under the MIT License.
