import syms as _syms

def filter_by_open_issue(repos): 
  l = []
  n = input('Choose the open issues filter threshold: ')
  for r in repos: 
    open_issues = r.get('open_issues') or None 
    if not open_issues: continue
    if open_issues >= int(n): l.append( r )

  return l

def filter_by_watchers(repos): 
  l = []
  n = input('Choose the watcher filter threshold: ')
  for r in repos: 
    watchers = r['watchers_count']
    if watchers >= int(n): l.append( r )
  return l

def filter_by_stars(repos): 
  l = []
  n = input('Choose the stars filter threshold: ')
  for r in repos: 
    fcount = r['stargazers_count']
    if fcount >= int(n): l.append( r )

  return l
  
def sort_by_push_date(repos, reverse = None): 
  sorted_repos = sorted(repos, key=lambda item: item.get('pushed_at_u')) 
  for r in sorted_repos:
    rname = r['name']
    rpush = r['pushed_at']
    print('Name: %s -- Date: %s' % (rname, rpush))
  return sorted_repos

def sort_by_creation_date(repos, reverse = None):
  sorted_repos = sorted(repos, key=lambda item: item.get('created_at_u')) 
  for r in sorted_repos:
    rname = r['name']
    rcreate = r['created_at']
    print('Name: %s -- Date: %s' % (rname, rcreate))
  return sorted_repos

def sort_by_size(repos, reverse = None): 
  sorted_repos = sorted(repos, key=lambda item: item.get("size"))
  for r in sorted_repos:
    rname = r['name']
    rsize = r['size']
    print('Name: %s -- Size: %s' % (rname, rsize))
  return sorted_repos

def explore_languages(repos):
  d = _syms.LANGS
  for r in repos:
    lang = r['language']
    try: d[lang] = d[lang] + 1
    except: pass

  total = len(repos)
  for key, value in d.items(): 
    if value <= 0: continue
    print("%s: %d repositories out of %d" % (key, value, total))

def explore_stars(repos): 
  for r in repos: 
    stars = r['stars']
    try: d[stars] += 1
    except: pass
  
  total_stars = len(repos)
  for key, value in d.item():
    if value <= 0: continue
    print("%s: %d repositories out of %d" % (key, value, total))

  
    
    

    

    







