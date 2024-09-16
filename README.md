
## Airport Travel Distance and Pathfinding Tool

This repository provides a Python-based tool for calculating and visualizing the shortest travel distance between two airports using real-world data. It integrates with the AviationAPI to fetch airport information and travel distances, employs Dijkstra's algorithm for pathfinding, and utilizes `folium` for map visualization.

### Features

- **Fetch Travel Distances**: Retrieve distances between airports using the AviationAPI.
- **Fetch Airport Information**: Get geographical coordinates of airports from the AviationAPI.
- **Distance Calculation**: Compute the geographical distance between two points using the Haversine formula.
- **Pathfinding**: Use Dijkstra's algorithm to find the shortest path between airports based on distance.
- **Map Visualization**: Display the route on an interactive map using `folium`, including markers for start and end points and a polyline for the path.

### Requirements

- `requests`: For making API requests to AviationAPI.
- `heapq`: For implementing priority queues in Dijkstra's algorithm.
- `math`: For mathematical functions like radians, sin, and cos.
- `folium`: For creating interactive maps.

### Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/your-username/airport-pathfinding.git
cd airport-pathfinding
pip install requests folium
```

### Usage

1. **Set Up API Key**: Replace `"your_api_key_here"` in the `main()` function with your actual AviationAPI key.
2. **Run the Script**: Execute the script to enter airport codes and view the results.

```bash
python main.py
```

3. **Input Airport Codes**: Enter the ICAO codes for the start and destination airports when prompted.

4. **View Results**:
   - The script will print the shortest distance between the airports.
   - An interactive HTML map (`map.html`) will be generated showing the route.

### Example

Here’s how you can use the tool to find the shortest distance and visualize the route:

```bash
Enter the start airport code: JFK
Enter the destination airport code: LAX
```

The script will fetch the required data, calculate the shortest path, and generate a map with the route displayed.

### Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests. For major changes or feature requests, please open an issue to discuss your ideas.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
