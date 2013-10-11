import os
import psutil
from flask import Flask, render_template

app = Flask(__name__)


def get_virtual_memory_info():
    virtual_memory = psutil.virtual_memory()
    total = round(float(virtual_memory.total) / 1024 / 1024, 2)
    available = round(float(virtual_memory.available) / 1024 / 1024, 2)
    stats = []
    stats.append('virtual memory')
    stats.append('Total memory: %s MB' % total)
    stats.append('Available memory: %s MB' % available)
    stats.append('Percent used: %s%%' % virtual_memory.percent)
    return stats


def get_swap_memory_info():
    memory = psutil.swap_memory()
    total = round(float(memory.total) / 1024 / 1024, 2)
    used = round(float(memory.used) / 1024 / 1024, 2)
    free = round(float(memory.free) / 1024 / 1024, 2)
    sin = round(float(memory.sin) / 1024 / 1024, 2)
    sout = round(float(memory.sout) / 1024 / 1024, 2)

    stats = []
    stats.append('swap memory')
    stats.append('Total memory: %s MB' % total)
    stats.append('Used memory: %s MB' % used)
    stats.append('Free memory: %s MB' % free)
    stats.append('Percent used: %s%%' % memory.percent)
    stats.append('Sin: %s MB' % sin)
    stats.append('Sout: %s MB' % sout)

    return stats


def get_memory_info():
    return get_virtual_memory_info() + get_swap_memory_info()


def get_cpu_time_info():
    cpu_time = psutil.cpu_times()
    stats = []
    stats.append('num cpus: %s' % psutil.NUM_CPUS)
    stats.append('Cpu time info')
    stats.append('user: %s' % cpu_time.user)
    stats.append('nice: %s' % cpu_time.nice)
    stats.append('system: %s' % cpu_time.system)
    stats.append('idle: %s' % cpu_time.idle)
    #stats.append('iowait: %s' % cpu_time.iowait)
    #stats.append('irq: %s' % cpu_time.irq)
    #stats.append('softirq: %s' % cpu_time.softirq)
    return stats


def get_cpu_percent_info():
    cpu_percent = psutil.cpu_times_percent(interval=1)
    stats = []
    stats.append('Cpu percent info')
    stats.append('user: %s' % cpu_percent.user)
    stats.append('nice: %s' % cpu_percent.user)
    stats.append('system: %s' % cpu_percent.user)
    stats.append('idle: %s' % cpu_percent.user)
    stats.append('iowait: %s' % cpu_percent.user)
    stats.append('irq: %s' % cpu_percent.user)
    stats.append('softirq: %s' % cpu_percent.user)
    stats.append('steal: %s' % cpu_percent.user)
    stats.append('guest: %s' % cpu_percent.user)
    stats.append('guest_nice: %s' % cpu_percent.user)
    return stats

def get_cpu_info():
    return get_cpu_time_info() + get_cpu_percent_info()


@app.route("/")
def stats():
    memorystats = get_memory_info()
    cpustats = get_cpu_info()
    myContext = [memorystats, cpustats]
    return render_template('stats.html', myContext=myContext)


if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    app.run(port=int(port))
