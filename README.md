# Openhab Configuration

This configuration is for an Openhab 3 installation running on a Raspberry 2.

Goal of this Project is primarily to connect and visualize my PV Production with the Energy Consumption by connection the Power Meter.
Later i want to be able to switch devices on or off tooptimize solarpower usage.

## PV Connection
PV Production is collected from envertec cloud by REST API query.
Queries and Data conversions are implemented as executed as rules located in the "rules" folder
There is not reallygood resource on how to query the API.

A very bad documentation can be found here:
https://www.envertecportal.com/TmpFiles/APIdocoument/%E6%81%A9%E6%B2%83%E5%85%AC%E5%85%B1%E6%8E%A5%E5%8F%A3%E6%96%87%E6%A1%A3.docx

There are mistakes in it; the queries seem the be updated in the meantime.

## Energy Consumption
A tasmota sensor is placed on the energy monitor and theoptical access is evaluated every 30 secondsby mqtt. mqtt broker is installed on the openhab Raspberry Py system.

Information onother sensors and how to connect my ebz emh bidirectional powermeter can be found here:
https://tasmota.github.io/

a good videresource to connect the sensor is available here:
https://www.youtube.com/watch?v=VuXpzKetOhc

### Implementation status
waiting for the PIN to release the full date export from the powermeter 