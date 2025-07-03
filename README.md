# Docker_OpenTripPlanner
## Description:
Some Dockerfiles to set up and deploy an OpenTripPlanner instance.
## Image Descriptions:
build_serve_transit builds and saves a transit graph before actually serving the OpenTripPlanner instance. A street graph must be built beforehand.  
build_street builds and saves a street graph
write_build-config helps set up a build-config.json file for the filesystem these images use.
## Filesystem: (only if using write_build-config, otherwise everything goes in /var/opentripplanner)
/var/opentripplanner  
├── gtfs  
│   └── example.gtfs.zip  
├── graphs  
│   ├── streetGraph.obj  
│   └── graph.obj  
├── osm  
│   └── map.osm.pbf  
└── build-config.json  
## How To Use:
Use any of the folders here to create Docker images to deploy to the cloud. Make sure to mount the directory containing your OTP data to /var/opentripplanner and make sure to use either put all OTP-related files directly in var/opentripplanner or use the filesystem above for the data.
## License:
No license, use this however you want!
