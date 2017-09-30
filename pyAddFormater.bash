#!/bin/bash
# Name: Frank Lewis
# NSID: fbl773
# Student #: 11194945
# Lecture: __
# Lab: __
# Synopsis: Formats , lists to \n lists;



echo $1 | tr ',' '\n' | tr -d ' ' > formated.txt



