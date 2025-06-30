from google.cloud import storage
import functions_framework, json

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def buildConfig_updater(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")

    if bucket == "ma-otp":
        client = storage.Client()
        otpBucket = client.bucket("ma-otp")

        # Generate lists of URIs from GCS blobs
        gtfsFiles = [
            f"gs://ma-otp/{blob.name}"
            for blob in otpBucket.list_blobs(prefix="gtfs/")
            if not blob.name.endswith("/")
        ]

        osmFiles = [
            f"gs://ma-otp/{blob.name}"
            for blob in otpBucket.list_blobs(prefix="osm/")
            if not blob.name.endswith("/")
        ]

        buildConfig = {
            "transitModelTimeZone": "America/New_York",
            "storage": {
                "gtfs": gtfsFiles,
                "osm": osmFiles,
                "streetGraph": "gs://ma-otp/graphs/streetGraph.obj",
                "graph": "gs://ma-otp/graphs/graph.obj"
            }
        }

        # Upload build-config.json directly to the bucket
        otpBucket.blob("build-config.json").upload_from_string(
            json.dumps(buildConfig, indent=2), content_type="application/json"
        )