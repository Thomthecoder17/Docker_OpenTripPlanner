import os, json

gtfsFiles = [
    f"file:///otp-data/gtfs/{file}"
    for file in os.listdir("/otp-data/gtfs")
]

osmFiles = [
    f"file:///otp-data/{file}"
    for file in os.listdir("/otp-data/osm")
]

buildConfig = {
    "transitModelTimeZone": "America/New_York",
    "storage": {
        "gtfs": gtfsFiles,
        "osm": osmFiles,
        "streetGraph": "file:///otp-data/graphs/streetGraph.obj",
        "graph": "file:///otp-data/graphs/graph.obj"
    }
}

with open("/otp-data/build-config.json", "w") as file:
    json.dump(buildConfig, file, indent=2)