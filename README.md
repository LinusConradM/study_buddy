# Study Buddy

Study Buddy is a CLI tool that parses course syllabus files (PDF or DOCX),
extracts assignment and exam deadlines, and syncs them to your Google Calendar
with reminders.

## Features

- Extract deadlines from PDF and DOCX syllabus files
- Automatically create full-day events in Google Calendar
- Set popup reminders at 7 days, 3 days, and 1 day before each deadline
- Optional dashboard view of upcoming deadlines

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd study-buddy
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Google Calendar API Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the Google Calendar API for your project.
4. Create OAuth 2.0 credentials (Desktop application) and download the
   `credentials.json` file into the project directory.
5. On first run, you will be prompted to authorize access; a `token.json` file
   will be generated to store your access tokens.

## Usage

```bash
python agent.py path/to/syllabus.pdf
```

Sync deadlines found in the syllabus to your primary Google Calendar.

To specify a different calendar ID or view upcoming deadlines:

```bash
python agent.py path/to/syllabus.docx --calendar-id your_calendar_id --dashboard
```

## License
This project is distributed under an MIT-style license.
