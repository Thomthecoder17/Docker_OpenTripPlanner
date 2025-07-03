import os, json

directory = "/var/opentripplanner"

# Creates the lists of files to use in build-config.json
gtfsFiles = [
    {
        "type": "gtfs",
        "source": f"file://{directory}/gtfs/{file}"    
    }
    for file in os.listdir(f"{directory}/gtfs")
]
osmFiles = [
    {
        "source": f"file://{directory}/osm/{file}"
    }
    for file in os.listdir(f"{directory}/osm")
]

# Compiles the data to write to build-config.json
buildConfig = {
    # ADD ANY OTHER FIELDS FOR build-config.json HERE

    "transitModelTimeZone": "America/New_York",
    "transitFeeds": gtfsFiles,
    "osm": osmFiles,
    "streetGraph": f"file://{directory}/graphs/streetGraph.obj",
    "graph": f"file://{directory}/graphs/graph.obj"
}

# Overwrites build-config.json with updated data
with open(f"{directory}/build-config.json", "w") as file:
    json.dump(buildConfig, file, indent=2)