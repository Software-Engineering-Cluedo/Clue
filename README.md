<h1 align="center">Clue</h1>
<p align="center">Python implimentation of cluedo</p>

# Game Configuration
- `map`
    - `dimentions`
        - `x`
            - The size of the x dimension.
            - Minimum: `10`
            - Maximum: `40`
        - `y` : The size of the y dimention.
            - The size of the y dimension.
            - Minimum: `10`
            - Maximum: `40`
    - `tiles`
        - The tile map used for the game
        - Each character has to be referenced once minimum within `simple tiles` or `game tiles`, but not both
        - Weapons should be referenced only once 
        - Players should be referenced only once
        - Secret doors have to be referenced twice
- `simple tiles`
    - Is a list of objects which include `char` and `obj`
    - Has to have a reference for each type of object for `simple tile`
    - `char`
        - The character the object is associated to
        - Can be any `simple tile` character used in tiles, not used again in either `simple tiles` or `game tiles`
    - `obj`
        - Has to be one of the including types 
        - Types:
            - `none`
            - `tile`
            - `door`
            - `secret door`
- `game tiles`
    - Is a list of objects which include `char` and `obj`
    - `char`
        - The character the object is associated to
        - Can be any `game tile` character used in tiles, not used again in either `simple tiles` or `game tiles`
    - `obj`
        - Has to be one of the including types 
        - Types:
            - `room`
            - `weapon`
            - `human`
            - `ai`
    - `name`
        - The name of the object

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
