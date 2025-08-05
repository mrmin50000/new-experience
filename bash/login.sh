#!/bin/bash

case ${1,,} in 
	mrmin50000 | administrator)
		echo "Hello, u're the boss here!"
		;;
	help)
		echo "Just enter ur username!"
		;;
	*)
		echo "suck, u're not the boss!"
esac
