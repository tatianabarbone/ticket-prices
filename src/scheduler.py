import schedule
import time
from workingfile import append_row

schedule.every(30).minutes.do(append_row("3day")) # adjust for frequency needed
schedule.every(30).minutes.do(append_row("friday"))
schedule.every(30).minutes.do(append_row("saturday"))
schedule.every(30).minutes.do(append_row("sunday"))


while True:
    schedule.run_pending()
    time.sleep(1)