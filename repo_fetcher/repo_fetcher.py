import json
import requests as rq
import utils as _utils
import filters as _filters
import syms as _syms
import datetime

API_BASE_URL = 'https://api.github.com/users/'
TOKEN = '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'
headers = {'Authorization': f'token {TOKEN}' }

def _parse_date(date): 
  date = date.strip('Z')
  ddate = datetime.datetime.fromisoformat(date)
  unixtime = int(ddate.timestamp())
  return unixtime

class RepoFetcher():

  uname = None
  repos = None

  def search_user(self, uname): 
    url = API_BASE_URL + uname
    res = rq.get(url, headers=headers)
    if res.status_code == 200: 
      self.uname = uname
      return True
    print('No such user found on Github.com')

  def fetch_repos(self):
    if not self.uname: return
    endpoint = API_BASE_URL + self.uname + '/' + 'repos'
    rdata = []
    page = 1
    while(True):
      res  = rq.get(endpoint, headers=headers)
      res  = json.loads(res.content)
      rdata = rdata + res
      if len(res) == 30: 
        page = page + 1
        endpoint = API_BASE_URL + self.uname + '/' + 'repos?page=' + str(page)
      else: break
    self.repos = rdata

  def get_rep(self): 
    return self.repos

  def set_rep(self, rep):
    self.repos = rep


  def filter_by(self, option): 
    filters = option.split(',') 
    if 'n' in filters: return
    rep = self.get_rep()
    for f in filters: 
      try: opt = _syms.FILTER_MAP[f]
      except:
        msg = _utils.FILTER_MSG
        print(msg)
        return msg
      if opt == _syms.OPEN_ISSUES : rep = _filters.filter_by_open_issue(rep)
      if opt == _syms.WATCHERS    : rep = _filters.filter_by_watchers(rep)
      if opt == _syms.STARS       : rep = _filters.filter_by_stars(rep)

    self.set_rep(rep)

  def sort_by(self, option):
    print('\n\n\n-------------')
    print('Sorting')
    rep = self.get_rep()
    for elem in rep: 
      creation = elem['created_at']
      push     = elem['pushed_at']
      creation = _parse_date(creation)
      push     = _parse_date(push)
      elem['created_at_u'] = creation
      elem['pushed_at_u'] = push
    
    try: opt = _syms.SORTING_MAP[option]
    except: pass

    if opt == _syms.SIZE : rep = _filters.sort_by_size(rep)
    if opt == _syms.PUSHED : rep = _filters.sort_by_push_date(rep)
    if opt == _syms.CREATED : rep = _filters.sort_by_creation_date(rep)
    
    self.set_rep(rep)

  def explore(self): 
    print('\n\n\n-------------')
    print('Exploring results')
    rep = self.get_rep()
    _filters.explore_languages(rep)



















