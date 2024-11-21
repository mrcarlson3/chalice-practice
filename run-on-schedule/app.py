from chalice import Chalice
import boto3

app = Chalice(app_name='run-on-schedule')



@app.schedule('cron(0 0 * * *)')
def daily_task():
	print('Running midnight errand')
