#!/bin/bash

ifconfig $1 down
macchanger -m $2 $1
ifconfig $1 up