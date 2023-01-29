# AutoExitValidator

These scripts will auto email you when your Consensus version has been out of date for a while. If your software is out of date for more than 60 days, then it will auto exit your validator(s).

Make sure to read the comments in each file to make the appropriate updates as necessary.

If you want to automate this, you can configure a cronjob to run. An exmaple of that would be the following

```
#This will run once per day at 6AM. Update paths as necessary
0 6 * * * /usr/bin/python3.10 ~/shouldExitValidatorsConsensus.py
```
