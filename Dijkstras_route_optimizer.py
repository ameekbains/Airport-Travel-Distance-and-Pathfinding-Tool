import requests
import heapq
from math import radians, sin, cos, sqrt, atan2
import folium

# Fetch real-world travel distances from AviationAPI
def fetch_travel_distances(api_key, airport_code):
    url = f"https://aviationapi.com/v1/airports/{airport_code}/distances"
    try:
        response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

# Fetch airport coordinates from AviationAPI
def fetch_airport_info(api_key, airport_code):
    url = f"https://aviationapi.com/v1/airports/{airport_code}"
    try:
        response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching airport info: {e}")
        return {}

# Calculate geographical distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Dijkstra's algorithm for shortest path
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def build_graph(api_key, start_airport):
    distances = fetch_travel_distances(api_key, start_airport)
    if not distances:
        return {}
    
    graph = {start_airport: {}}
    for airport in distances:
        graph[start_airport][airport] = distances[airport]['distance']
        graph[airport] = {}  # Initialize empty adjacency list for each airport
    return graph

def plot_map(start_airport, end_airport, start_coords, end_coords, distance):
    m = folium.Map(location=start_coords, zoom_start=5)
    folium.Marker(start_coords, tooltip=start_airport).add_to(m)
    folium.Marker(end_coords, tooltip=end_airport).add_to(m)
    folium.PolyLine([start_coords, end_coords], color="blue", weight=2.5, opacity=1).add_to(m)
    folium.Popup(f"Distance: {distance:.2f} km").add_to(folium.Marker(end_coords))
    m.save("map.html")

def main():
    api_key = "your_api_key_here"
    start_airport = input("Enter the start airport code: ").upper()
    end_airport = input("Enter the destination airport code: ").upper()
    
    if start_airport == end_airport:
        print("Start and destination airports cannot be the same.")
        return
    
    # Get coordinates for the start and end airports
    start_info = fetch_airport_info(api_key, start_airport)
    end_info = fetch_airport_info(api_key, end_airport)
    
    if not start_info or not end_info:
        print(f"Error fetching information for one or both airports.")
        return
    
    start_coords = (start_info['latitude'], start_info['longitude'])
    end_coords = (end_info['latitude'], end_info['longitude'])
    
    graph = build_graph(api_key, start_airport)
    if end_airport not in graph:
        print(f"No data available for destination airport {end_airport}.")
        return
    
    shortest_paths = dijkstra(graph, start_airport)
    if shortest_paths[end_airport] == float('infinity'):
        print(f"No path found from {start_airport} to {end_airport}.")
    else:
        print(f"Shortest distance from {start_airport} to {end_airport} is {shortest_paths[end_airport]} km")
        
        # Plot map with distances
        plot_map(start_airport, end_airport, start_coords, end_coords, shortest_paths[end_airport])

if __name__ == "__main__":
    main()
