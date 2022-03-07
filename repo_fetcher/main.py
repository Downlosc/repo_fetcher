import argparse 
import repo_fetcher as _rf

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', help='Name of the user')
parser.add_argument('-f', '--filter', help='filter the research')
parser.add_argument('-s', '--sort', help='sort the research')
args = parser.parse_args()

def main():
  r = _rf.RepoFetcher()
  usr  = args.user
  fil  = args.filter
  sort = args.sort
  # expl = args.explore

  isusr = r.search_user(usr)
  if not isusr: return
  r.fetch_repos()
  if fil: 
    err = r.filter_by(fil)
    if err: return 
  rep = r.get_rep()
  if sort: r.sort_by(sort)
  r.explore()

  # rep = _parse_rep(rep)
  # return rep


if __name__=="__main__":
  main()

