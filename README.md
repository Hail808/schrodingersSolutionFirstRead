# README.md

# My Python Project

This is a Python project that demonstrates how to set up a basic application and make it installable using PyInstaller.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```
python src/main.py
```

## Building with PyInstaller

To create an executable for this project using PyInstaller, follow these steps:

1. Install PyInstaller if you haven't already:

   ```
   pip install pyinstaller
   ```

2. Navigate to the project directory:

   ```
   cd my-python-project
   ```

3. Build the executable:

   ```
   pyinstaller --onefile src/main.py
   ```

4. After the build process is complete, you can find the executable in the `dist` directory.

## License

This project is licensed under the MIT License.