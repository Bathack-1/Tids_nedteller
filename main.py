from datetime import datetime
import pytz
import time


def hent_tiden():
    nå = datetime.now(pytz.timezone('Europe/Oslo'))
    tid = [nå.time, nå.minute, nå.second]
    return tid


def tid_til(ønsket_tid, tidsenhet):
    tid_nå = hent_tiden()

    if "time" in tidsenhet:
        return ønsket_tid[0] - tid_nå[0]

    tid_nå_minutter = tid_nå[0] * 60
    ønsket_tid_minutter = ønsket_tid[0] * 60

    if "minutt" in tidsenhet:
        return (ønsket_tid[1] + ønsket_tid_minutter) - (tid_nå[1] + tid_nå_minutter)

    tid_nå_sekunder = (tid_nå[1] + tid_nå_minutter) * 60
    ønsket_tid_sekunder = (ønsket_tid[1] + ønsket_tid_minutter) * 60

    return (ønsket_tid[2] + ønsket_tid_sekunder) - (tid_nå[2] + tid_nå_sekunder)


def tell_ned(tid, tidsenhet):
    tidsenheter = {
        "timer": 60 * 60,
        "minutter": 60,
        "sekunder": 1
    }
    enhets_verdi = tidsenheter[tidsenhet]
    while tid > 0:
        print(f"{tid} {tidsenhet} igjen")
        time.sleep(enhets_verdi)
        tid -= 1


ønsket_tid = [23, 00, 00]   #[time, minutt, sekund]

tid_igjen = tid_til(ønsket_tid, "minutter")
tell_ned(tid_igjen, "minutter")
