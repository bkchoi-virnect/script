import jenkins
import sys

server = jenkins.Jenkins('http://121.162.3.204:18080/', username='virnect', password='virnect0!')
user = server.get_whoami()
version = server.get_version()
count = server.jobs_count()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

if len(sys.argv) < 2:
    print("ERR: Origin Repository Name is Empty")
    exit(0)

if len(sys.argv) < 3:
    print("ERR: Company Code is Empty")
    exit(0)

orgRepo = server.job_exists(sys.argv[1])
'''
if orgRepo:
    print("ERR: Duplicated Job")
    sys.exit()
'''
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[1]+'-'+sys.argv[2])
getJob = server.get_job_config(sys.argv[1])
#newJob = getJob.replace(sys.argv[1],sys.argv[2]+'-'+sys.argv[1])
newJob = getJob.replace(sys.argv[1],sys.argv[2])
print(getJob)
print("==============================================================")
print(newJob)

server.create_job(sys.argv[2],newJob)
