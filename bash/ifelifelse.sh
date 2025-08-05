#!/bin/bash

if [ ${1,,} = mrmin50000 ]; then
	echo "Oh, u're the boss here. Welcome!"
elif [ ${1,,} = help ]; then
	echo "Just enter ur username, duh!"
else
	echo "Idk who u are."
fi
