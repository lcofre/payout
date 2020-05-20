# payout
Calculates payout for students (Exercise challenge)

## Docker
To build locally:
```
docker build -t payout .
docker run --rm payout
```
After printing all allowances this docker container will exit.

To add other input files run the image mounting those files:
```
docker run -v /full/path/to/my-attendance.csv:/usr/src/payout/attendance.csv -v /full/path/to/my-workplaces.csv:/usr/src/payout/workplaces.csv --rm payout
```

Alternatively you can use the image that is automatically built and uploaded to docker hub:
```
docker run --rm lcofre/payout
```

You can also try the following tags:
```
docker run --rm lcofre/payout:alpine # For a smaller size image
docker run --rm lcofre/payout:pypy # For an arguable faster execution
```