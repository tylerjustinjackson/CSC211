import sqlite3
import webbrowser


# Function to generate the HTML report
def generate_report(output_file: str = "phonebook_report.html") -> None:
    # Connect to the SQLite database
    conn = sqlite3.connect("phonebook.db")
    cursor = conn.cursor()

    # Fetch all contacts from the database
    cursor.execute("SELECT rowid, name, phonenumber FROM contacts")
    rows = cursor.fetchall()

    # Create an HTML structure
    html_content = """
    <html>
    <head>
        <title>Phonebook Report</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>Phonebook Report</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Phone Number</th>
            </tr>
    """

    # Add data rows to the HTML
    for row in rows:
        html_content += f"""
            <tr>
                <td>{row[0]}</td>
                <td>{row[1]}</td>
                <td>{row[2]}</td>
            </tr>
        """

    # Closing HTML tags
    html_content += """
        </table>
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open(output_file, "w") as file:
        file.write(html_content)

    # Close the database connection
    conn.close()

    print(f"HTML report generated: {output_file}")


# Function to open the generated HTML report in a web browser
def printreport(output_file: str = "phonebook_report.html") -> None:
    # Open the HTML file in the default web browser
    webbrowser.open(output_file)
