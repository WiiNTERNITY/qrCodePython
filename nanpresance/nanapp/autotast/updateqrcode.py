from apscheduler.schedulers.background import BackgroundScheduler
from .generateqrcode import generateqr


def start():
    #intitialise
    scheduler = BackgroundScheduler()
    
    #Create jod
    scheduler.add_job(generateqr, 'interval', minutes=2) #this job is excecute every one minutes
    
    
    #start job
    scheduler.start()
    