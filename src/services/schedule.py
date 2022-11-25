from apscheduler.schedulers.background import BackgroundScheduler

from src.services.twitter_api_service import TwitterApiService

def job():
  TwitterApiService.get_tweets()

TwitterApiService.get_tweets()
sched = BackgroundScheduler(standalone=True,coalesce=True)
sched.add_job(job, 'interval', minutes=10)
sched.start()