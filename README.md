# Intermediate

Training material on behalf of Brights.

## Setup

In a terminal in this directory, run the following commands:

1. `python -m venv venv`

2. Run ONE of the following commands depending on what terminal you are using.
    a. `venv\Scripts\activate.bat`      (if using cmd.exe) 
    b. `venv\Scripts\Activate.ps1`      (if using Powershell)
    c.  `source venv/Scripts/activate` 	(if using git-bash)	

**NB:** If this does _not_ work, you most likely do not have local admin rights on your computer.
Ignore the error message and follow the rest of the instructions.

3. `python -m pip install -r requirements.txt`

4. In the terminal, go to the `exercises` directory and run `pytest setup_test.py` to verify that your setup is complete.
