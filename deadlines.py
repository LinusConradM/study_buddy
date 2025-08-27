from dateparser.search import search_dates


def extract_deadlines(text: str):
    """
    Extract deadlines from text.
    Returns a list of dicts with 'title' and 'due' datetime objects.
    """
    deadlines = []
    lines = text.splitlines()
    for line in lines:
        if not line.strip():
            continue
        matches = search_dates(line, settings={'PREFER_DATES_FROM': 'future'})
        if not matches:
            continue
        date_str, date_obj = matches[0]
        parts = line.split(date_str, 1)
        title = parts[0].strip(":- ").strip()
        if title:
            deadlines.append({'title': title, 'due': date_obj})
    return deadlines