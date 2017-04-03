#!/usr/bin/env python

HELP = """
This is my help text.
"""

import datetime
import yaml
import sys

def render_confluence(cfg, data):
  print '||' + '||'.join(data['header']) + '||'
  for row in data['rows']:
    for shift in row:
      sys.stdout.write('|')
      start_date = shift['start_date'].strftime(cfg['date_format'])
      end_date = shift['end_date'].strftime(cfg['date_format'])
      sys.stdout.write("%s - %s" % (start_date, end_date))
    sys.stdout.write('|')
    sys.stdout.write("\n")

renderers = {}
renderers['confluence'] = render_confluence

def main():
  input = sys.stdin.read().strip()
  if not input:
    print HELP
    sys.exit(0)
  cfg = yaml.load(input)
  start_date = datetime.datetime.strptime(cfg['start_date'], '%Y-%m-%d %H:%M:%S')
  shift_delta = datetime.timedelta(days=cfg['shift_days'])
  data = {'header': cfg['team'], 'rows': []}
  for i in range(cfg['iterations']):
    row = []
    for person in cfg['team']:
      end_date = start_date + shift_delta - datetime.timedelta(seconds=1)
      row.append({'person': person, 'start_date': start_date, 'end_date': end_date})
      start_date += shift_delta
    data['rows'].append(row)
  renderers[cfg['output_format']](cfg, data)
  
if __name__ == '__main__':
  main()
