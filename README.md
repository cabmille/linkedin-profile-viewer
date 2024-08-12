# linkedin-profile-viewer
Python script that, given a LinkedIn search, automatically visits all profiles from that list.
This Python project uses Selenium to automate the process of scraping LinkedIn profiles based on a search query. The script navigates through multiple pages of search results, clicks on each profile to gather information, and then returns to the results list to process the next profile. The script is designed to handle up to 100 pages of search results.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Automated LinkedIn Login**: Automatically logs into LinkedIn using provided credentials.
- **Profile Scraping**: Iterates through LinkedIn search results, clicking on each profile to gather data.
- **Pagination Handling**: Navigates through up to 100 pages of search results using URL manipulation.
- **Error Handling**: Catches and handles exceptions such as stale elements and missing profile links.
- **Return Navigation**: Returns to the search results page after processing each profile.

## Requirements

- Python 3.x
- Google Chrome browser
- ChromeDriver compatible with your Chrome version

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/linkedin-profile-scraper.git
   cd linkedin-profile-scraper
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download ChromeDriver**:
   - Ensure you have the correct version of ChromeDriver for your installed version of Google Chrome. [Download ChromeDriver](https://sites.google.com/chromium.org/driver/) and place it in a directory included in your system's PATH, or specify its path in the script.

## Usage

1. **Set your LinkedIn credentials**:
   - Open the `linkedin_scraper.py` file and replace the placeholders in the script with your LinkedIn username and password:
     ```python
     username.send_keys('your-email@example.com')
     password.send_keys('your-password')
     ```

2. **Run the script**:
   ```bash
   python linkedin_scraper.py
   ```

   The script will automatically log in to LinkedIn, navigate to the specified search results page, and begin processing profiles.

3. **Monitor the output**:
   - The script will print the number of profiles found on each page and any errors encountered.

## Configuration

- **Search URL**:
  - The script currently uses a hardcoded URL for the LinkedIn search results. You can modify the `URL` variable in the script to use your custom search query.
  
- **Sleep Time**:
  - Adjust the `time.sleep()` intervals in the script to better suit your internet speed and LinkedIn's page load times.

## Error Handling

- **Stale Element Reference**: 
  - The script is designed to catch and handle `StaleElementReferenceException`, which occurs when the page is reloaded and the previously referenced elements become invalid.
  
- **No Such Element**:
  - The script also handles `NoSuchElementException` for cases where expected elements are not found on the page.

- **General Exceptions**:
  - Any other exceptions are caught and logged, allowing the script to continue processing subsequent profiles.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any bugs, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes

- Replace `your-username` with your GitHub username in the repository URL.
- Update the paths, links, and any other project-specific details as needed.
- If your project requires more specific instructions, such as configuring a `.env` file for credentials, be sure to add those to the README as well.
