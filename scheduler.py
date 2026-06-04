from apscheduler.schedulers.background import BackgroundScheduler
from modules.job_engine import get_jobs

def send_daily_jobs():
    jobs = get_jobs("Python Developer")
    print("Daily Jobs:")
    for j in jobs:
        print(j)

scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_jobs, "interval", hours=24)
scheduler.start()