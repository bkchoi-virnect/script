from github import Github
import pygit2
import requests
import os
import sys
import tqdm
import time

if len(sys.argv) < 2:
    print("ERR: Origin Repository Name is Empty")
    exit(0)

if len(sys.argv) < 3:
    print("ERR: Company Code is Empty")
    exit(0)

ORGANIZATION = "virnect-corp"
ORG_REPOSITORY = sys.argv[1]
CORP_CODE = sys.argv[2]
ORG_REPOSITORY_URL=""
NEW_REPOSITORY_URL=""

headers = {
  'Accept': 'application/vnd.github.v3+json',
  'Authorization': 'token c150dbd55d93f6be437d27b643b3f6d39bf2b310'
}
payload = {}

## Exist repository
url = "https://api.github.com/repos/"+ORGANIZATION+"/"+ORG_REPOSITORY
getRepository = requests.request("GET", url, headers=headers, data = payload)


for i in tqdm.tqdm(range(50)):
    time.sleep(0.01)

print(getRepository.json()['ssh_url'])

if getRepository.status_code == 200:
    print("Repository Exist")
    ORG_REPOSITORY_URL= getRepository.json()['ssh_url']
    NEW_REPOSITORY_URL=CORP_CODE+"-"+ORG_REPOSITORY
else :
    print("-> "+getRepository.json()['message'])
    exit(0)

## Clone Repository
repoClone=""
keypair=""
if os.path.isdir(NEW_REPOSITORY_URL):
    print("ERR: Directory is exist")
    exit(0)

try :
    keypair = pygit2.Keypair("git", "/home/bkchoi/.ssh/id_rsa.pub", "/home/bkchoi/.ssh/id_rsa", "")
    callbacks = pygit2.RemoteCallbacks(credentials=keypair)
    repoClone=pygit2.clone_repository(ORG_REPOSITORY_URL, NEW_REPOSITORY_URL,callbacks=callbacks)
except Exception as ex:
    print('ERR: ',ex)
    exit(0)

## Delete Repository
url = "https://api.github.com/repos/bkchoi-virnect/"+NEW_REPOSITORY_URL
payload ={}
deleteRepository = requests.request("DELETE", url, headers=headers, data = payload)

if deleteRepository.status_code == 204:
    print("Repository Deleted")
else :
    print(deleteRepository.json()['message'])    

## Create Repository
url = "https://api.github.com/user/repos"
payload ="{\"name\" : \""+NEW_REPOSITORY_URL+"\"}"
postRepository = requests.request("POST", url, headers=headers, data = payload)

if postRepository.status_code == 201:
    print("Repository Created")
else :
    print("-> "+postRepository.json()['message'])
    for msg in postRepository.json()['errors']:
        print("--> "+msg['message'])
    exit(0)

## Push
try :
    repoClone.remotes.set_url("origin",'git@github.com:bkchoi-virnect/'+NEW_REPOSITORY_URL+'.git')
    # repoClone.remotes.set_url("origin",'git@github.com:'+ORGANIZATION+'/'+NEW_REPOSITORY_URL+'.git')
    remote=repoClone.remotes["origin"]
    credentials = keypair
    remote.credentials =credentials
    callbacks=pygit2.RemoteCallbacks(credentials=credentials)
    remote.push(['refs/heads/master'],callbacks=callbacks)
    print("Repository Push")
except Exception as ex:
    print('ERR: ',ex)
    exit(0)

print("finish")