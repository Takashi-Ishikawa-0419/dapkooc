#!/bin/sh

python get_image.py "data_json/json5" "data_image/image5" & \
python get_image.py "data_json/json6" "data_image/image6" & \
python get_image.py "data_json/json7" "data_image/image7" & \
python get_image.py "data_json/json8" "data_image/image8" & \
python get_image.py "data_json/json9" "data_image/image9" & \
python get_image.py "data_json/json10" "data_image/image10"
wait
echo done!
