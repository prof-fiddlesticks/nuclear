import requests

def get_flights_by_airline(airline_prefixes):
    """Retrieves and displays flights for a specific airline."""
    url = "https://opensky-network.org/api/states/all"

    try:
        response = requests.get(url)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        if "states" not in data:
            print("No flight data available right now.")
            return

        print(f"\nFlights for airline prefixes: {airline_prefixes}")
        print("-" * 50)

        found = False
        for state in data["states"]:
            callsign = state[1]  # Flight identifier

            if callsign and any(callsign.startswith(prefix) for prefix in airline_prefixes):
                longitude = state[5]  # Current longitude
                latitude = state[6]  # Current latitude
                altitude = state[7]  # Altitude in meters

                if longitude is None or latitude is None:
                    continue

                print(f"Flight: {callsign}")
                print(f"Position: Lat {latitude:.4f}, Lon {longitude:.4f}")
                print(f"Altitude: {altitude if altitude else 'Unknown'} meters")
                print("-" * 50)
                found = True

        if not found:
            print(f"No active flights found for airline prefixes: {airline_prefixes} right now.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {str(e)}")
    except ValueError as e: # Catch json decode errors.
        print(f"Error decoding JSON response: {str(e)}")

if __name__ == "__main__":
    airline_prefixes_input = input("Enter airline prefixes (e.g., AAL,DAL,UAL): ").upper()
    airline_prefixes = airline_prefixes_input.split(",")
    get_flights_by_airline(airline_prefixes)

print("""Dear user,

Keep in mind that some flights might be left out because we are using the OpenSky Network API which 
relies on ADS-B signals which not all planes have. We are sorry for the inconvenience. We are working
on switching to a new API which is accurate

The developement team""")