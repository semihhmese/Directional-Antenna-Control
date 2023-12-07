# Directional Antenna Control

This Python project utilizes the SGP4 module to calculate the orientation of an antenna with respect to a satellite specified by Two-Line Element (TLE) parameters. The project provides a simple example for determining the position of a satellite and the location of an antenna.

## Usage

1. Download or clone the project files.
2. Install the necessary libraries by running the following command in the terminal or command prompt:

    ```bash
    pip install sgp4
    ```

3. Edit the `main.py` file to set the TLE parameters and the observer's location.
4. Navigate to the project directory in the terminal or command prompt and start the program by running:

    ```bash
    python main.py
    ```

## Example

```python
# TLE parameters
line1 = "ISS (ZARYA)"
line2 = "1 25544U 98067A   21292.47037037  .00000725  00000+0  24610-4 0  9992"
line3 = "2 25544  51.6416 289.5233 0007985   5.6366  82.6783 15.48811595504709"

# Observer's location (e.g., for Istanbul)
observer_lat = 41.0082
observer_lon = 28.9784
observer_alt = 100  # Observer's altitude (in meters)

# Orientation calculations
azimuth, elevation = calculate_azimuth_elevation(observer_lat, observer_lon, observer_alt, line1, line2)

print(f"Satellite Orientation: Azimuth={azimuth}, Elevation={elevation}")
