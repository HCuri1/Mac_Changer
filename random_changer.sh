#!/bin/bash

ifconfig $1 down
macchanger -r $1
ifconfig $1 up