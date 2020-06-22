import jenkins
import sys
from replaceall import replaceall

server = jenkins.Jenkins('http://121.162.3.204:18080/', username='virnect', password='virnect0!')
user = server.get_whoami()
version = server.get_version()
count = server.jobs_count()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

jobs = server.get_job_config("PF-demo1")
print(jobs)
print(replaceall(jobs,"<",""))
