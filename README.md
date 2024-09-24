# Google API Business Data Scraping

This Python script uses the Google Places API to collect business data, including business names, addresses, phone numbers, and more. It supports querying based on location and business types, making it a valuable tool for efficiently gathering business information.

## Features:
- Pulls data from the Google Places API
- Handles multiple query types (e.g., business type, location)
- Exports data to Excel or CSV for easy access and review
- Can be adapted for custom fields like emails, websites, etc.

## Use Case:
This project has been instrumental in helping multiple fire departments find business data within their jurisdiction, particularly during the onboarding process with fire safety software companies. By pulling accurate business information, fire departments can streamline inspections and enhance data accuracy for their fire safety management systems.

## How to Use
1. Get a Google Places API key.
2. Replace `'your_google_places_api_key'` in the script with your actual API key.
3. Update the `location` coordinates to your desired location.
4. Modify the `queries` list to search for the types of businesses you want.
5. Run the script, and the results will be saved to `businesses_output.xlsx`.

## Requirements
- `requests` library
- `pandas` library
