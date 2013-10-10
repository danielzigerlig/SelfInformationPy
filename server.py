import os
import psutil
from flask import Flask, render_template

app = Flask(__name__)


def get_memory_info():
    memory = psutil.virtual_memory()
    total = round(float(memory.total) / 1024 / 1024, 2)
    available = round(float(memory.available) / 1024 / 1024, 2)
    stats = []
    stats.append('Total memory: %s MB' % total)
    stats.append('Available memory: %s MB' % available)
    stats.append('Percent used: %s%%' % memory.percent)
    return stats

@app.route("/")
def stats():
    stats = get_memory_info()
    return render_template('stats.html', stats=stats)

if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    app.run(port=int(port))
