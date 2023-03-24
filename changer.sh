# !/bin/bash

ifconfig $1 down
ifconfig $1 hw ether $2
ifconfig $1 up