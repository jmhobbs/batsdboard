from time import time
import json
from batsd import Connection
from flask import g, Blueprint, current_app, render_template


dashboard = Blueprint('batsdboard', __name__, template_folder='templates', static_folder='static')


@dashboard.before_request
def setup_batsd_connection():
    g.batsd = Connection(host=current_app.config.get('BATSD_HOST', 'localhost'),
                         port=current_app.config.get('BATSD_PORT', 8127))


@dashboard.route('/')
def index():
    return render_template('index.html', page="index", counters=g.batsd.counters(), timers=g.batsd.timers(), gauges=g.batsd.gauges())


@dashboard.route('/counters/')
def counters():
    return render_template('counters.html', page='counters', counters=g.batsd.counters())


@dashboard.route('/timers/')
def timers():
    return render_template('timers.html', page='timers', timers=g.batsd.timers())


@dashboard.route('/gauges/')
def gauges():
    return render_template('gauges.html', page='gauges', gauges=g.batsd.gauges())


@dashboard.route('/counters/<name>')
def counter(name):
    parts = name.split('.')
    name = parts[0]
    subname = '.'.join(parts[1:]) if len(parts) > 1 else None
    return render_template('graph.html', page='counters', dataset=g.batsd.counter(name).get(int(time()) - 60, int(time()), subname), json=json)


@dashboard.route('/timers/<name>')
@dashboard.route('/timers/<name>/<measure>')
def timer(name, measure="mean"):
    parts = name.split('.')
    name = parts[0]
    subname = '.'.join(parts[1:]) if len(parts) > 1 else None
    return render_template('graph.html', page='timers', dataset=g.batsd.timer(name).get(int(time()) - 60, int(time()), subname, measure), json=json)


@dashboard.route('/gauges/<name>')
def gauge(name):
    parts = name.split('.')
    name = parts[0]
    subname = '.'.join(parts[1:]) if len(parts) > 1 else None
    return render_template('graph.html', page='gauges', dataset=g.batsd.gauge(name).get(int(time()) - 60, int(time()), subname), json=json)
