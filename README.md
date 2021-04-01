<h1 align="center">Clue</h1>
<p align="center">Python implimentation of cluedo</p>

# Development

If you are on windows, install python from https://www.python.org/, be sure to click add to path before clicking install

1. Clone the repo
2. Open up powershell / terminal
3. Navigate to the folder, e.g. `cd F:\Repositories\Clue`
4. If on windows, run powershell as admin and run `Set-ExecutionPolicy unrestricted` and exit ( there may be a potentially better way, please change if found )
6. Create the venv: `python -m venv venv`
7. Activate the venv: `./venv/bin/activate` (Linux) or `./venv/Scripts/activate` (Win)
8. Run `pip install -r requirements.txt` to install the requirements
9. In the root directory, run `pip install -e .`

Tah-dah, now you can develop code. 
Your IDE should automatically switch to using the venv, or show a prompt to switch to it, do that and it should run well.
PyCharm automatically switches to it, while in VS Code you need to accept it from a prompt.

<!--
    At the top, maybe a logo centered?
    After the title and subtitle, maybe put an image here of the final product.
    And then info and how to install and set it up.
-->
