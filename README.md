# NetSpeed Widget for Windows

![NetSpeed Widget Demo](https://i.imgur.com/your-demo-gif.gif)

A clean, modern, and persistent network speed monitor designed to feel like a native widget on Windows 11. It provides real-time upload and download speeds and logs historical data usage, which can be viewed in a simple monthly report.

The widget is lightweight, stays on top of other windows, and remembers its position on your screen—even across multiple displays.

---

## Key Features

-   **Real-Time Monitoring**: See your current upload and download speeds at a glance.
-   **Persistent Data Logging**: Automatically logs data usage for all network interfaces to a local SQLite database.
-   **Monthly Usage Reports**: Right-click the widget to view a clean breakdown of your total data consumption per network card for each month.
-   **Smart Position Memory**: Remembers its last position on the screen. If a display is disconnected, it intelligently moves to your primary monitor.
-   **Multi-Monitor Aware**: Works seamlessly across multiple screens.
-   **Run on Startup**: Easily configured to launch automatically when you log in to Windows.
-   **Lightweight & Unobtrusive**: A borderless, semi-transparent design that integrates cleanly into your desktop.
-   **No Installer Needed**: Packaged as a single `.exe` file that runs out of the box.

---

## Built With

-   [Python](https://www.python.org/)
-   [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI
-   [psutil](https://github.com/giampaolo/psutil) for network statistics
-   [WMI](https://github.com/tjguk/wmi) for identifying the active network interface
-   [screeninfo](https://github.com/rr-/screeninfo) for multi-monitor position validation
-   [SQLite3](https://docs.python.org/3/library/sqlite3.html) for data storage
-   [PyInstaller](https://pyinstaller.org/) for packaging into an executable

---

## Getting Started

You can either download the ready-to-use application or build it from the source code.

### For Users (Easy Installation)

1.  **Download the Executable**: Go to the [Releases](https://github.com/sushil-2803/Net-Speed-Monitor/releases) page and download the latest `NetSpeedWidget.exe` file.
2.  **Run the Widget**: Double-click the `.exe` to start the widget. It will appear in the top-left corner of your primary screen.
3.  **(Optional) Run on Startup**:
    -   Press `Win + R` to open the Run dialog.
    -   Type `shell:startup` and press Enter. This will open the Windows Startup folder.
    -   Create a shortcut to `NetSpeedWidget.exe` inside this folder. The widget will now launch automatically every time you log in.

### For Developers (Running from Source)

If you want to modify or run the script yourself, follow these steps.

1.  **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```
2.  **Create a Virtual Environment** (Recommended):
    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    ```
3.  **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
4.  **Run the Script**:
    ```sh
    python netspeed_widget.pyw
    ```

---

## How to Use

-   **Move the Widget**: Click and drag the widget to place it anywhere on your screen(s).
-   **Access Menu**: **Right-click** the widget to open the context menu.
-   **View Usage**: From the menu, select `Show Monthly Usage` to see your data history.
-   **Exit**: From the menu, select `Exit`. The widget will save its current position and close.

The widget saves its database (`net_usage.db`) and configuration (`config.txt`) in the `%APPDATA%/NetSpeedWidget` folder.

---

## Creating the Executable (`.exe`)

If you've made changes to the source code, you can rebuild the executable using PyInstaller.

1.  **Install PyInstaller**:
    ```sh
    pip install pyinstaller
    ```
2.  **Build the `.exe`**:
    Run the following command from the project's root directory. Using an `.ico` file is optional but recommended.
    ```sh
    pyinstaller --onefile --windowed --icon=assets/icon.ico netspeed_widget.pyw
    ```
3.  Your standalone executable will be located in the `dist` folder.

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## Acknowledgments

-   A big thank you to the creators of the Python libraries that made this project possible.
-   Inspiration from various system utility tools.
