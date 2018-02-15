#! /bin/sh

echo "Hello, World!"
python cookpad_get.py 0 100 &  \
python cookpad_get.py 100 200 &  \
python cookpad_get.py 200 300 &  \
python cookpad_get.py 300 400 &  \
python cookpad_get.py 400 500 &  \
python cookpad_get.py 500 600 &  \
python cookpad_get.py 600 700 &  \
python cookpad_get.py 700 800 &  \
python cookpad_get.py 800 900 &  \
python cookpad_get.py 900 1000
