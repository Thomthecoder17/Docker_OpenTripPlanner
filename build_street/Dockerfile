FROM docker.io/opentripplanner/opentripplanner:latest
COPY otp-data/ /var/opentripplanner/

ENV JAVA_OPTIONS="-Xmx4G"
WORKDIR /var/opentripplanner

CMD ["--buildStreet"] 