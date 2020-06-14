# Submission

### Tar
#### Stripping Components
- **Exercise 2**
  - Extract `Movies`: tar -xvf TarDocs.tar --strip-components=1 TarDocs/Movies/
  - Extract `Movies/ZOE_0004.mp4`: tar -xvf TarDocs.tar --strip-components=2 TarDocs/Movies/ZOE_0004.mp4 


#### Modifying Archives
- **Exercise 1**

  ```bash
  # Insert the solution commands for Exercise 1 below
cp TarDocs.tar Update.tar
tar -tvf Update.tar
nano test1.txt test2.txt 
tar -tvf Update.tar --wildcards 'test*'
  ```

- **Exercise 2**

  ```bash
  # Insert the solution commands for Exercise 2 below
nano test2.txt
tar -uvf Update.tar test2.txt
tar -tvf Update.tar --wildcards 'test*'
  ```
To answer the Question: Yes the new test 2 was inside of the Updates.tar. It was 46 blocks vs the 23 the orginial test 2 was.

- **Exercise 3**

  ```bash
  # Insert the solution commands for Exercise 3 below
tar -vf Update.tar --delete test1.txt
tar -tvf Update.tar --wildcards 'test*'
  ```

#### Incremental Backups
- **Exercise 1**
  - A **snapshot file** is a stand alone file that stores the meta data from incremental backups. it is designed to tell the usr what has been changed/ modified since the last backup.
  - A **backup level** is the nubmer of times you have backed up a particular set of data. 0 being the orginial 1 being the second backup 2 being the third and so forth.
  - A **level 0 backup** is the very first backup created when making backups inside of the /var/log/usr.snar file. this can be updated by either overwriting the orginial file or removing the snapshot file.

- **Exercise 2**

  ```bash
  # Insert the solution commands for Exercise 2 below
sudo tar -cvzf archive.tar.gz /home
touch ~/new_file.1 ~/new_file.2
sudo tar -cvzf archive.1.tar.gz --listed-incremental=/var/log/home.snar /home
sudo tar -cvzf archive.2.tar.gz --listed-incremental=/var/log/home.snar-1 /home
tar -tvf archive.1.tar.gz
cat home.snar
To answer the question I did not see what I expected. From my understanding the incremental is only supposed to list the differences that happen after the level 0 and yet the file is bigger.

  ```

### Cron
#### Managing cron
Please paste the contents of `backup-cron-jobs.txt` in the space below.

  ```bash
  
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
#2 * * * 2,4,6 find Documents/ -iname *.pdf | tar -cvf cronjob.tar -T - >/dev/null 2>&1
#2 * * * 2,4,6 tar -xvf cronjob.tar -C exercises/ >/dev/null 2>&1

  ```
