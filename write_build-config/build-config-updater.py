import os, json

# Creates the lists of files to use in build-config.json
gtfsFiles = [
    f"file:///otp-data/gtfs/{file}"
    for file in os.listdir("/otp-data/gtfs")
]
osmFiles = [
    f"file:///otp-data/{file}"
    for file in os.listdir("/otp-data/osm")
]

# Compiles the data to write to build-config.json
buildConfig = {
    # ADD ANY OTHER FIELDS FOR build-config.json HERE

    "transitModelTimeZone": "America/New_York",
    "storage": {
        "gtfs": gtfsFiles,
        "osm": osmFiles,
        "streetGraph": "file:///otp-data/graphs/streetGraph.obj",
        "graph": "file:///otp-data/graphs/graph.obj"
    }
}

# Overwrites build-config.json with updated data
with open("/otp-data/build-config.json", "w") as file:
    json.dump(buildConfig, file, indent=2)