from flask import Flask
from redis import Redis

app = Flask(__name__)
redisDb = Redis(host = '127.0.0.1', port = 6379)

visitCount = 0

@app.route('/')
def welcomeToKodeKloud():
    redisDb.incr('wisitroCount')
    visitCount = str(redisDb.get('visitorCount'), 'utf-8')
    visitCount += 1
    return "Welcome to KODECLOUD! Visitor count:!"+str(visitCount)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = True)