#!/usr/bin/env python3
"""
get_school_info.py

A self-contained script to fetch school metadata (School ID 994) from the Aeries demo API.
Replace the placeholder values below with your actual Aeries instance URL and API certificate.
"""

import requests

# ─── CONFIGURATION ──────────────────────────────────────────────────────────────

# Base URL for your Aeries instance (no trailing slash)
AERIES_BASE = "https://demo.aeries.net/aeries"

# Your 32-character Aeries API certificate (case-sensitive)
API_KEY = "477abe9e7d27439681d62f4e0de1f5e1"

# The school ID you wish to fetch
SCHOOL_ID = "994"

# ─── END CONFIGURATION ──────────────────────────────────────────────────────────

def get_school_info(base_url: str, cert: str, school_id: str) -> None:
    """
    Fetches and prints metadata for the given school ID.
    """
    url = f"{base_url}/api/v5/schools/{school_id}/gpas"
    headers = {
        "AERIES-CERT": cert,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        school_data_list = response.json()
        if isinstance(school_data_list, list) and school_data_list:
            school_data = school_data_list[0]  # Take the first item as a dictionary
            print("School Information:")
            for key, value in school_data.items():
                print(f"  {key}: {value}")
        else:
            print("No school data found.")
        print("Number of Students found:", len(school_data_list))
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    get_school_info(AERIES_BASE, API_KEY, SCHOOL_ID)
