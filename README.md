# Analysing climate data from the Netherlands using only basic Python

## Project Overview 

This goal of the project is to perform data analysis using only basic Python in order to utilize inbuild methods.

We write a Python program that will read in the file, parse it (i.e. interpret the data in the file into useful variables in the code) and then use the data to output a set summary plots of averaged quantities for a selected weather station. More specifically the monthly averages of maximum temperature (in Celsius), minimum temperature (in Celsius), daily sum of precipitation (in mm/hour), duration of sunshine (in hours). Normally we would do a lot of this fairly easily using libraries such as `Numpy` or `Pandas`, but the catch here is that our program may not use any dedicated data-analysis libraries such as `Numpy` or `Pandas`, besides using the matplotlib library for plotting!

## Data Description

[Data](https://drive.google.com/file/d/1v4jgewMpPDP6uyrhcGw9U3Qw7XA8Xi83/view?usp=sharing)

The file associated with this project contains meteorological data taken from a number of weather stations in the Netherlands and dating back as far as 1901. The file is a text file consisting of a header (with ‘#’ marking the start of each header line) followed by the data itself, in the form of comma-separated values (CSV) with each line corresponding to a single day at a single station. Note that the days are not necessarily continuous: there may be gaps in the data, and different stations do not record the same days over the entire period covered by the data. The header includes information on the weather stations, each classified with a station (STN) number, coordinates and name, and the list of measured variables (given as uppercase letter codes) and their descriptions. Note that the descriptions are given in Dutch but for non-Dutch-speakers, can be easily translated by pasting into Google translate!

Note that some stations may not be suitable (e.g. with too short a time period, or with the physical quantities themselves missing). In that case the code will print an appropriate message
