# TuringOJ
### An Online Judge written in Django and Python

**Project Setup (for development)**
* Copy the whole project to a directory.
* Open `/turingoj/settings.py` and update the database variables.
* Here PostgreSQL is used, update the Database Engine accordingly.
* Setup the `SECRET_KEY` file and the `DB_PASS` file.
* Setup the `ALLOWED_HOSTS` variable.
* Setup the virtual environment according to the requirements.txt.
* Set `DEBUG=True` for development purposes.

**Judge Setup** `(scripts/judge.py)`
* Create a jail for secure execution of the judge and ensure that the compilers to be used are installed and available.
* Update the `CHROOTPATH` var to be equal to the path of the jail root.
* Change `TIME_QUANTUM` in accordance with the speed of the judge you want, keep in mind that decreasing it to a very low value will result in thrashing and poor performance.
* Run `scripts/judge.py` as `sudo python3 judge.py` to start judging submissions.
* To judge a range of submissions type `sudo python3 judge.py A B` , where A and B are the start and end submission IDs of the solutions.
* Also run `scripts/updateLeaderBoard.sh` for the leaderboard to be updated regularly, to avoid inconsistency for the users who haven't submitted any solution.


**Created by: Pranav Raj (WDragon)**
