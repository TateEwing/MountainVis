import os
from gpx_converter import Converter

gpx_directory = 'data\\as_gpx'
csv_directory = 'data\\as_csv'

# convert each .gpx file to .csv for easy consumption
for filename in os.listdir(gpx_directory):
    f = os.path.join(gpx_directory, filename)

    # Skip non-gpx files. Data collected from Strava comes in inconsistent file types--only want to include .gpx
    if os.path.isfile(f) and '.gpx' in f:
        out_filename = filename.replace('.gpx', '.csv')
        out_path = os.path.join(csv_directory, out_filename)
        print("attempting to convert file", f, " to ",out_path)
        print("Saving file to: ", out_path)
        Converter(input_file=f).gpx_to_csv(output_file=out_path)
