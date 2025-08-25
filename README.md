# nasa-power-api
Download meteorological data records from Nasa Power.

You will receive hourly data on:

- Temperature (Temperature at 2 Meters, Wet Bulb Temperature at 2 Meters, etc.)
- Humidity/Precipitation (Specific Humidity at 2 Meters, Relative Humidity at 2 Meters, Precipitation)
- Wind/Pressure (Surface Pressure, Wind Speed at 10 meters, etc.)

You can find a detailed list of all available parameters at: https://power.larc.nasa.gov/data-access-viewer/

### Usage Instructions

Simply edit the config.yaml by specifying your latitude, longitude, start time, and end time values.

    # Location
    lat: 53.524960
    lon: -1.627447

    # Format: YYYYMMDDHH
    # Earliest is 1981010100
    start_time: 2010030100

    # Format: YYYYMMDDHH
    end_time: 2010030123

Hit run to save the respective .csv file in the project's data directory.
