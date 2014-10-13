"""
this is the main file for the program.
it just runs the program...the fun is happening in nytscraper.py
"""
import ntyscraper

"""main while loop"""
print_time="07:40:00"
while True:
    if time.strftime('%X')==print_time:
        nytscraper.create_file()
        time.sleep(60)

