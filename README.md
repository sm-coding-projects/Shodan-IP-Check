# Shodan IP Check Script

This Python script uses the Shodan API to generate detailed PDF reports for specified IP addresses. The reports include information such as IP details, open ports and services, vendor information, recent scans, and known vulnerabilities.

## Features

- Generates a comprehensive PDF report for each IP address
- Includes detailed sections on IP information, open ports, services, and vulnerabilities
- Uses the Shodan API to fetch up-to-date information
- Supports multiple IP addresses in a single run

## Requirements

- Python 3.6+
- Shodan API key

## Installation

1. Clone this repository or download the script.
2. Install the required packages:

```
pip install -r requirements.txt
```

3. Replace `YOUR_API_KEY_HERE` in the script with your actual Shodan API key.

## Usage

Run the script from the command line:

```
python shodan_IP_chk.py
```

When prompted, enter one or more IP addresses separated by commas.

The script will generate a PDF report for each IP address in the current directory.

## Note

This script is for educational and informational purposes only. Ensure you have the right to scan and report on the IP addresses you input.

## License

This project is open source and available under the [MIT License](LICENSE).
