# Dota 2 Deleter Program

Welcome to the Dota 2 Deleter program! This program is designed to be included in the system's autostart and automatically removes the Dota 2 game folder if it exists. The program comes with two executables—`Doka2_deleter.exe` for adding the program to autostart and `Doka2_enabler.exe` for removing it from autostart.

## Prerequisites

Ensure you have the required libraries installed by running the following command:

```bash
pip install pyinstaller winreg pytest-shutil winshell pypiwin32
```

## Executable Creation

Use the following commands to create the executable files without showing the console:

- For `Doka2_deleter.exe`:

```bash
pyinstaller.exe -w -F -i ./icon.ico Doka2_deleter.py
```

- For `Doka2_enabler.exe`:

```bash
pyinstaller.exe -w -F -i ./icon.ico Doka2_enabler.py
```

## Usage

1. Run `Doka2_deleter.exe` to add the program to autostart.
2. The program will run in the background and automatically delete the Dota 2 game folder if it exists.
3. To remove the program from autostart, run `Doka2_enabler.exe`.

## Important Notes

- Ensure that you have a backup of your Dota 2 game folder before using this tool.
- These executables are created to work in the background without showing a console window.

## Contribution

Contributions are welcome! If you have suggestions or want to improve the program, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy Dota 2 folder managing! 🎮🚀
