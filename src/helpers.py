from datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%d"

def load_config(filepath):
    """Load parameters from a text file into a dictionary."""
    params = {}
    
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#') or line.startswith(';'):
                    continue
                
                if '=' in line:
                    key, value = line.split('=', 1)
                    params[key.strip()] = value.strip()
                
                elif ':' in line:
                    key, value = line.split(':', 1)
                    params[key.strip()] = value.strip()
    
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
    
    return params

def increment_date(date_str):
    d = datetime.strptime(date_str, DATE_FORMAT)
    d += timedelta(days=1)
    return d.strftime(DATE_FORMAT)

