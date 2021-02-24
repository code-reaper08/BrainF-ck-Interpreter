# BrainF-ck Interpreter
[![GitHub issues](https://img.shields.io/github/issues/code-reaper08/BrainF-ck-Interpreter?style=for-the-badge)](https://github.com/code-reaper08/BrainF-ck-Interpreter/issues) [![GitHub stars](https://img.shields.io/github/stars/code-reaper08/BrainF-ck-Interpreter?style=for-the-badge)](https://github.com/code-reaper08/BrainF-ck-Interpreter/stargazers) ![GitHub last commit](https://img.shields.io/github/last-commit/code-reaper08/BrainF-ck-Interpreter?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/code-reaper08/BrainF-ck-Interpreter?style=for-the-badge) [![GitHub license](https://img.shields.io/github/license/code-reaper08/BrainF-ck-Interpreter?style=for-the-badge)](https://github.com/code-reaper08/BrainF-ck-Interpreter/blob/main/LICENSE) ![GitHub repo size](https://img.shields.io/github/repo-size/code-reaper08/BrainF-ck-Interpreter?style=for-the-badge) ![GitHub branch checks state](https://img.shields.io/github/checks-status/code-reaper08/BrainF-ck-Interpreter/main?style=for-the-badge) ![GitHub top language](https://img.shields.io/github/languages/top/code-reaper08/BrainF-ck-Interpreter?style=for-the-badge)
### This is a simple interpreter which interprets .bf codes using python.

## What is Brainf-ck ?
  Brainfuck is an esoteric programming language created in 1993 by Urban Müller Notable for its extreme minimalism, the language consists of only eight simple commands and an instruction pointer. While it is fully Turing complete, it is not intended for practical use, but to challenge and amuse programmers. Brainfuck simply requires one to break commands into microscopic steps.

The language's name is a reference to the slang term brainfuck, which refers to things so complicated or unusual that they exceed the limits of one's understanding.

for more info head [here](https://en.wikipedia.org/wiki/Brainfuck).

## What are the commands Brainf-ck use ?

Brainf-ck uses only 8 commands !
| Command      | Functionality           |
| ------------- |:-------------:|
| >      | Increment the data pointer to the right of the current cell |
| <      | Increment the data pointer to the left of the current cell |
| +      | Increment the byte at the current data pointer |
| +      | Decrement the byte at the current data pointer |
| .      | Output the byte at the current data pointer |
| ,      | Accept input of one byte and storing it at the current data pointer |
| [      | if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command. |
| ]      | if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command. |


## How this interpreter works ?

This interpreter mimics the memory tape with python's array and simulates the bit/byte properties,So that it could perform the relevant operations for all the **8** operations the **Brainf-ck** has.

## How to use this interpreter ?

1. Navigate to [this repository](https://github.com/code-reaper08/BrainF-ck-Interpreter).

2. Click on the **Download ZIP**.

      ![downloadzip](https://user-images.githubusercontent.com/64256342/108976679-c61ad880-76ad-11eb-9892-a47038b788db.png)


3. Place your .bf (Brainf-ck code) in the same folder containing the [interpreter](https://github.com/code-reaper08/BrainF-ck-Interpreter/blob/main/BF.py).

4. Use your terminal/bash to run the command in the below specified manner.

    + ` python BF.py sample.bf `
    
    where **BF.py** is the interpreter and **sample.bf** is the brainf-ck code you want to execute. The python in beginning instructs the system to run it using python.

5. On pressing `Enter` the brain-fck program executes.




# Deal with BRAINF-CK !
