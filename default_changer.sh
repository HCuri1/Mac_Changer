#!/bin/bash

ifconfig $1 down
macchanger -p $1
ifconfig $1 up