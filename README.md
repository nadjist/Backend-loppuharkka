made with Python 3.11.3


Create virtual environment
- in VSCode, Command Pallette (Ctrl+Shift+P) -> white Python: Create Environment -> select Venv -> Select Python installation
Activate venv, VSCode activates automatically.

Open Terminal, make sure you have venv activated.
Install Uvicorn:
write to terminal:
pip install uvicorn
uvicorn main:app --reload
