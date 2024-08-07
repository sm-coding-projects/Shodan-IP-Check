import shodan
import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable
from reportlab.lib.styles import getSampleStyleSheet

# Shodan API key
API_KEY = "YOUR_API_KEY_HERE"

# Function to generate the detailed report
def generate_report(ip_address):
    try:
        # Create a Shodan API client
        api = shodan.Shodan(API_KEY)

        # Retrieve information about the IP address
        host = api.host(ip_address)

        # Create a PDF document
        pdf_filename = f"report_{ip_address}.pdf"
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

        # Create a list to store the PDF elements
        elements = []

        # Add report sections (title, table of contents, etc.)
        # ... [rest of the code remains the same]

        # Build the PDF document
        doc.build(elements)

        print(f"PDF report generated: {pdf_filename}")

    except shodan.APIError as e:
        print(f"Error: {str(e)}")

# Example usage
if __name__ == "__main__":
    ip_addresses = input("Enter the IP addresses (separated by comma): ")
    ip_list = [ip.strip() for ip in ip_addresses.split(",")]

    for ip_address in ip_list:
        generate_report(ip_address)
