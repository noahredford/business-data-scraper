import requests
import pandas as pd
import re

# API Key placeholder - use your own API key
API_KEY = 'your_google_places_api_key'

# Function to fetch businesses from Google Places API
def get_places_data(queries, location, radius=24140):  # 15 miles ≈ 24,140 meters
    businesses = []
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    
    # Loop through each query to fetch data
    for query in queries:
        params = {
            'query': query,
            'location': location,
            'radius': radius,  # The radius is set to 15 miles (24,140 meters)
            'key': API_KEY
        }
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print(f"Error fetching data for {query} at {location}: {response.status_code}")
            continue

        data = response.json()
        
        # Process results
        if data.get('results'):
            for result in data['results']:
                business_info = {
                    'Business Name': result.get('name'),
                    'Address': result.get('formatted_address', 'N/A'),
                    'Phone': result.get('formatted_phone_number', 'N/A'),
                    'Rating': result.get('rating', 'N/A'),
                    'Total Ratings': result.get('user_ratings_total', 'N/A'),
                    'Business Type': ', '.join(result.get('types', [])),
                }
                businesses.append(business_info)

    return businesses

# Function to save business data to Excel
def save_to_excel(businesses, filename='businesses_output.xlsx'):
    # Create DataFrame from the businesses list
    df = pd.DataFrame(businesses)
    # Save to Excel
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

# Main function to collect businesses for a specific location
def main():
    # Example list of queries (you can modify this to suit your needs)
    queries = [
        "restaurant",
        "doctor's office",
        "store",
        "school",
        "church",
        "fast food",
        "industrial",
        "retail"
    ]
    
    # Location for Bessemer, AL (latitude, longitude) - use your own coordinates
    location = "33.4018, -86.9544"
    
    # Fetch data from Google Places API
    businesses = get_places_data(queries, location)
    
    # Save data to Excel if any businesses are found
    if businesses:
        save_to_excel(businesses, filename='bessemer_businesses.xlsx')
    else:
        print("No data returned.")

if __name__ == "__main__":
    main()
