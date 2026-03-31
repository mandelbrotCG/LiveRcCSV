# LiveRcCSV

Grabs LiveRC race data and exports lap times into CSV files organized by date and racer name.

## Prerequisites

### Installing Python on Windows

1. **Download Python**
   - Visit [python.org](https://www.python.org/downloads/)
   - Click the **"Download Python"** button (default is the latest version)

2. **Run the Installer**
   - Open the downloaded `.exe` file
   - **IMPORTANT**: Check the box **"Add Python to PATH"** at the bottom of the installer
   - Click **"Install Now"** or customize installation as needed

3. **Verify Installation**
   - Open PowerShell or Command Prompt
   - Run:
     ```powershell
     python --version
     ```
   - You should see the Python version (e.g., `Python 3.11.0`)

## Setup Instructions

### 1. Configure the Project

Create a `config.txt` file in the project root directory with the following format:

```
baseURL=https://your-livrc-url.com
userName=John Doe
```

Replace:
- `https://your-livrc-url.com` with the actual LiveRC website URL, the URL should point to the home page for the site.
- `John Doe` with your name, exactly as it appears on the website. 

### 2. Install Python Dependencies

Open PowerShell in the project directory and run:

```powershell
pip install -r requirements.txt
```

This installs:
- `beautifulsoup4` - HTML parsing
- `requests` - HTTP requests

**Note**: If `pip` is not recognized, ensure Python was added to PATH during installation. Restart PowerShell after adding Python to PATH.

## Running the Project

1. Open PowerShell in the project root directory

2. Run the scraper:
   ```powershell
   python main.py
   ```

3. The script will:
   - Fetch race data between the specified dates (in `main.py`)
   - Create a folder structure: `race_times/{racer_name}/{year}/{month}/{day}/`
   - Save lap time data as CSV files in the respective date folders

## Output Structure

CSV files are organized as:
```
race_times/
└── {racer_name}/
    └── {year}/
        └── {month}/
            └── {day}/
                └── {time}.csv
```

Each CSV contains:
```
Lap Number,Lap Time
1,45.23
2,45.67
...
```

## Troubleshooting

**"python: command not found"**
- Python is not in your PATH
- Reinstall Python and check "Add Python to PATH" during installation
- Restart PowerShell after reinstalling

**"ModuleNotFoundError"**
- Dependencies are not installed
- Run `pip install -r requirements.txt` again

**Connection errors when running**
- Check your internet connection
- Verify the `baseURL` in `config.txt` is correct
