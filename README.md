# Information

The foundation for this project was made by coe posted on Geeks For Geeks by Shaurya Uppal, demonstrating
a working example of a CRC generator, and then modified to show the needed steps for our project.
Website Credit: https://www.geeksforgeeks.org/cyclic-redundancy-check-python/
The posted code generates the CRC from an input data word and divisor. This project modifies the code to
print the intermediate steps in the CRC calculation to show the generation process. It also adds a UI to 
allow the user to specify the data word and checksum, and control the stepping process themself.

### Authors
Through Cal Poly EE470 class, written by Andrew McGuan and Denis Pyryev. 
CRC generator code based off the work of Shaurya Uppal

## Requirements
The UI is dependent on the Python library Tkinter. Tkinter (TK INTERface) is a Python library that helps
create easy user interfaces. It comes standard on most Python installations, but if you do not have a copy,
it can be installed [here](https://tkdocs.com/tutorial/install.html).


This project also requires a version of Python3.


This has only been tested on computers running Windows 10. Python and tkinter easily cross platforms so it should
be runnable on any machine in theory.


## Installation
Clone the git repo, or get ahold of crc.py. No other source files are needed apart from crc.py.
[Git Repo](https://github.com/amcguan/crc_calculation)


## How to Use

1. Open up a command prompt window (or terminal, for Mac/Linux users)
2. Run the script:

    `python3 crc.py`
3. A window will appear with two entry windows. Under 'Data', enter the string that is to be sent as a code word. ASCII characters only.
4. Under 'Divisor', enter the generator polynomial to be used to make the CRC. Only binary will work correctly.
5. Click 'Submit'. The resulting window will show the data word in binary. 
6. A variety of buttons are available to control the program.
	* Start - Begin the crc conversion, automatically step through at 1s intervals
	* Stop - Pause the program from stepping through the conversion
	* Step - Advance one more conversion step and pause after
	* Finish - Run through to the end with no delay
7. After the program finishes, the calculated remainder and new codeword will be shown on the screen. You can restart the conversion by pressing "Start", "Finish", or "Step".