made with Python 3.11.3

If you don't have Python, install it from: https://www.python.org/downloads/

Create virtual environment
- in VSCode, Command Pallette (Ctrl+Shift+P) -> white Python: Create Environment -> select Venv -> Select Python installation
Activate venv, VSCode activates automatically after install.

Open new terminal, make sure you have venv activated.
Install FastAPI:
write to terminal: pip install fastapi
Install Uvicorn:
write to terminal: pip install uvicorn
uvicorn main:app --reload

You can test the program here: http://127.0.0.1:8000/docs 