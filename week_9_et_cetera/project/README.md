# Greek Language Learning Flashcards

Welcome to the Greek Language Learning Flashcards program! This program is designed to help you practice and learn new words in Greek and English. It is executed in the terminal window as a sequence of interactive questions and answers.

## Files

The project folder contains the following files:
- `requirements.txt`: This file lists the modules used in the program.
- `test_project.py`: This file contains tests for the program.
- `project.py`: This is the main file for the program.
- `greek.csv`: This file contains all the foreign words used in the program.
- `README.md`: This is the file you are currently reading.

## How to Use

To use this program, first make sure you have all the required modules installed by running `pip install -r requirements.txt` in your terminal. Then, navigate to the project folder and run `python project.py` to start the program.

When you start the program, you will be prompted to choose whether you want to practice English or Greek translation. Type 'english' or 'greek' and press enter to make your selection.

Next, you will be asked to choose which file you want to study from. Enter the name of the file (e.g. 'greek.csv') and press enter.

You will then be asked how many rounds of language learning you can handle. Enter a number and press enter to begin your language adventure!

## Functionality

The program contains several functions that work together to help you learn new words. Here is a brief description of what each function does:

- `main()`: This is the main function that runs when you start the program. It prompts you to choose which language you want to practice and calls the appropriate function (`study_english()` or `study_greek()`) based on your selection.

- `bordered(text)`: This function takes a string as an argument and returns a new string with a border added around it. It is used to make the text displayed in the terminal more visually appealing.

- `percentage(numerator, denominator)`: This function takes two numbers as arguments and returns the percentage of the first number relative to the second number. It is used to calculate your success rate when practicing words.

- `end()`: This function is called when you want to exit the program. It prints a goodbye message and exits the program.

- `study_english()`: This function is called when you choose to practice English translation. It prompts you to choose which file you want to study from and how many rounds of language learning you can handle. Then, it reads in the words from the specified file and begins a series of interactive questions and answers where you are shown a word in Greek and asked to translate it into English.

- `study_greek()`: This function is similar to `study_english()`, but it is called when you choose to practice Greek translation. It prompts you to choose which file you want to study from and how many rounds of language learning you can handle. Then, it reads in the words from the specified file and begins a series of interactive questions and answers where you are shown a word in English and asked to translate it into Greek.

I hope this program helps you on your language learning journey! Happy studying!