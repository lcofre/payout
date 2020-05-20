# payout
Calculates payout for students (Exercise challenge)

## Docker
To build and run locally:
```
docker build -t payout .
docker run --rm payout
```
After printing all allowances this docker container will exit.

To add other input files run the image mounting those files:
```
docker run -v /full/path/to/my-attendance.csv:/usr/src/payout/attendance.csv -v /full/path/to/my-workplaces.csv:/usr/src/payout/workplaces.csv --rm payout
```