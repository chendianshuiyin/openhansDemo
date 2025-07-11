# PyQt Hello World Examples

This repository contains simple PyQt5 examples that demonstrate how to create a "Hello World" application.

## Requirements

- Python 3.x
- PyQt5

To install PyQt5:

```bash
pip install PyQt5
```

## Files

1. `hello_world_console.py` - A simple PyQt application that prints "Hello World" to the console and then exits.
2. `hello_world_gui.py` - A GUI application with a window displaying "Hello World" and buttons to print to console or quit.
3. `hello_world.py` - An alternative version that uses the offscreen platform (useful for headless environments).

## Running the Examples

### Console Example

```bash
python hello_world_console.py
```

This will print "Hello World" to the console and exit.

### GUI Example

```bash
python hello_world_gui.py
```

This will open a window with "Hello World" text and two buttons:
- "Print to Console" - Prints "Hello World" to the console
- "Quit" - Closes the application

## Notes

- If you're running in a headless environment (like a server without a display), the GUI examples may not work unless you use a virtual framebuffer like Xvfb.
- The `hello_world.py` script uses the "offscreen" platform which can work in headless environments but won't display a visible window.

## Learning More About PyQt

To learn more about PyQt, check out these resources:

- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Qt Documentation](https://doc.qt.io/)
- [PyQt5 Tutorial](https://www.pythonguis.com/pyqt5-tutorial/)