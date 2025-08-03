#!/usr/bin/env python3
"""
export_grade11_enrollment.py

Fetches all 11th grade students from Aeries, saves raw JSON, exports a filtered CSV,
and builds a dictionary of student records keyed by StudentID.
"""

import json
import requests
import pandas as pd

# ─── CONFIGURATION ──────────────────────────────────────────────────────────────

BASE_URL    = "https://demo.aeries.net/aeries"
SCHOOL_ID   = "994"
GRADE_LEVEL = "11"
API_CERT    = "477abe9e7d27439681d62f4e0de1f5e1"  # <-- Replace with your 32-char cert

# Fields to include in CSV and dictionary
COLUMNS = [
    'StudentID','OldStudentID','CorrespondenceLanguageCode','CounselorNumber',
    'StudentPersonalEmailAddress','SchoolCode','StudentNumber','StateStudentID',
    'LastName','FirstName','MiddleName','Gender','Grade',
    'GradeLevelShortDescription','GradeLevelLongDescription','Birthdate',
    'ParentGuardianName','HomePhone','StudentMobilePhone','MailingAddress',
    'MailingAddressCity','MailingAddressState','MailingAddressZipCode',
    'ResidenceAddress','ResidenceAddressCity','ResidenceAddressState',
    'ResidenceAddressZipCode','AddressVerified','EthnicityCode','RaceCode1',
    'SchoolEnterDate','SchoolLeaveDate','DistrictEnterDate',
    'AttendanceProgramCodePrimary','LockerNumber','LowSchedulingPeriod',
    'HighSchedulingPeriod','FamilyKey','LanguageFluencyCode','HomeLanguageCode',
    'ParentEdLevelCode','ParentEmailAddress','StudentEmailAddress',
    'NetworkLoginID','EarlyWarningPoints','HomeRoomTeacherNumber',
    'NotificationPreferenceCode','NextSchoolCode','NextGrade',
    'NextGradeLevelShortDescription','NextGradeLevelLongDescription'
]
# ─── END CONFIGURATION ──────────────────────────────────────────────────────────

HEADERS = {
    'AERIES-CERT': API_CERT,
    'Accept':     'application/json'
}

def fetch_grade_students():
    """
    Fetches a list of students for a specific grade level from the school's API.

    Returns:
        dict: The JSON response containing student data.

    Raises:
        requests.HTTPError: If the HTTP request returned an unsuccessful status code.
    """
    url = f"{BASE_URL}/api/v5/schools/{SCHOOL_ID}/students/grade/{GRADE_LEVEL}"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    print(f"[FETCH] {url} → Status {resp.status_code}")
    resp.raise_for_status()
    return resp.json()

def save_json(data, filename='enrollment.json'):
    """
    Saves the provided data as a JSON file.

    Args:
        data (any): The data to be serialized and saved as JSON.
        filename (str, optional): The name of the file to save the JSON data to. Defaults to 'enrollment.json'.

    Returns:
        None

    Side Effects:
        Writes the serialized JSON data to the specified file.
        Prints a confirmation message indicating the file location.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"[SAVE] Raw data written to {filename}")

def json_to_csv(data, filename='enrollment.csv'):
    """
    Converts a list of JSON objects to a CSV file with specified columns.

    Parameters:
        data (list or dict): The JSON data to convert, typically a list of dictionaries.
        filename (str, optional): The name of the output CSV file. Defaults to 'enrollment.csv'.

    Notes:
        - The function normalizes nested JSON data into a flat table.
        - Only columns specified in the global COLUMNS variable are included in the output.
        - Missing columns are filled with empty strings.
        - Requires pandas to be imported as pd.

    Outputs:
        Writes the filtered CSV file to disk and prints a confirmation message.
    """
    # Normalize JSON into a flat table
    df = pd.json_normalize(data)
    # Filter to the desired columns, ignoring missing ones
    df = df.reindex(columns=COLUMNS, fill_value='')
    df.to_csv(filename, index=False)
    print(f"[SAVE] Filtered CSV written to {filename}")

def create_student_dict(data):
    """
    Create a dict of student records keyed by StudentID,
    including only the fields in COLUMNS.
    """
    student_dict = {}
    for record in data:
        sid = record.get('StudentID')
        if sid is None:
            continue
        filtered = {col: record.get(col) for col in COLUMNS}
        student_dict[sid] = filtered
    return student_dict

def main():
    """
    Main function to orchestrate the student data workflow.
    Steps performed:
    1. Fetches student data using `fetch_grade_students()`.
    2. Saves the raw JSON data to 'enrollment.json' via `save_json()`.
    3. Converts the JSON data to CSV format and saves as 'enrollment.csv' using `json_to_csv()`.
    4. Builds a dictionary of students with `create_student_dict()` and prints a summary.
    Returns:
        dict: Dictionary mapping student IDs to their records.
    Handles:
        - requests.RequestException: If data fetching fails.
        - Exception: For any other unexpected errors.
    """
    try:
        # 1. Fetch data
        students = fetch_grade_students()

        # 2. Save raw JSON
        save_json(students, 'enrollment.json')

        # 3. Export CSV
        json_to_csv(students, 'enrollment.csv')

        # 4. Build and return dict
        student_dict = create_student_dict(students)
        print(f"[DICT] Created dictionary for {len(student_dict)} students.")
        # Example: print first 3 entries
        for sid, rec in list(student_dict.items())[:3]:
            print(f"  {sid} → {rec}")

        return student_dict

    except requests.RequestException as e:
        print("[ERROR] Request failed:", e)
    except Exception as e:
        print("[ERROR] Unexpected error:", e)

if __name__ == "__main__":
    main()
