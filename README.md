# huggingface_cronjob

# Python Script:
Python Script is written to retrieve list of the top 10 downloaded models data from huggingface and keep it in a textfile.

# Dockerfile
The Dockerfile creates the image of the python script and the image is pushed to dockerhub.
docker build -t bhimkumar/report_cronjob:latest .

# Containerization
docker run --rm -v /home/ubuntu/huggingface_report/report.txt:/app/report.txt bhimkumar/report_cronjob:latest

# Cron job
write the command in the crontab editor and schedule the job accordingly.
* * * * * docker run --rm -v /home/ubuntu/huggingface_report/report.txt:/app/report.txt bhimkumar/report_cronjob:latest

Our job report is retrieved in the reprt.txt file. using docker bind mount.
          
