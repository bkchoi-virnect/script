import jenkins
import sys

server = jenkins.Jenkins('http://121.162.3.204:18080/', username='virnect', password='virnect0!')
user = server.get_whoami()
version = server.get_version()
count = server.jobs_count()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

exists = server.job_exists(sys.argv[1])
if exists:
    print("ERR: Duplicated Job")
    sys.exit()

#jobs = server.get_job_config("PF-Admin")
#print(jobs)
#jobs = server.get_job_config("PF-demo1")
#print(jobs)
'''
print("<?xml version='1.1' encoding='UTF-8'?>")
print("<org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject plugin=\"workflow-multibranch@2.21\">")
print("  <actions/>")
print("  <properties>")
print("    <org.jenkinsci.plugins.configfiles.folder.FolderConfigFileProperty plugin=\"config-file-provider@3.6.3\">")
print("      <configs class=\"sorted-set\">")
print("        <comparator class=\"org.jenkinsci.plugins.configfiles.ConfigByIdComparator\"/>")
print("      </configs>")
print("    </org.jenkinsci.plugins.configfiles.folder.FolderConfigFileProperty>")
print("    <io.jenkins.blueocean.rest.impl.pipeline.credential.BlueOceanCredentialsProvider_-FolderPropertyImpl plugin=\"blueocean-pipeline-scm-api@1.22.0\">")
print("      <domain plugin=\"credentials@2.3.1\">")
print("        <name>blueocean-folder-credential-domain</name>")
print("        <description>Blue Ocean Folder Credentials domain</description>")
print("        <specifications/>")
print("      </domain>")
print("      <user>virnect</user>")
print("      <id>github</id>")
print("    </io.jenkins.blueocean.rest.impl.pipeline.credential.BlueOceanCredentialsProvider_-FolderPropertyImpl>")
print("  </properties>")
print("  <folderViews class=\"jenkins.branch.MultiBranchProjectViewHolder\" plugin=\"branch-api@2.5.5\">")
print("    <owner class=\"org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject\" reference=\"../..\"/>")
print("  </folderViews>")
print("  <healthMetrics>")
print("    <com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric plugin=\"cloudbees-folder@6.11\">")
print("      <nonRecursive>false</nonRecursive>")
print("    </com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric>")
print("  </healthMetrics>")
print("  <icon class=\"jenkins.branch.MetadataActionFolderIcon\" plugin=\"branch-api@2.5.5\">")
print("    <owner class=\"org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject\" reference=\"../..\"/>")
print("  </icon>")
print("  <orphanedItemStrategy class=\"com.cloudbees.hudson.plugins.folder.computed.DefaultOrphanedItemStrategy\" plugin=\"cloudbees-folder@6.11\">")
print("    <pruneDeadBranches>true</pruneDeadBranches>")
print("    <daysToKeep>-1</daysToKeep>")
print("    <numToKeep>-1</numToKeep>")
print("  </orphanedItemStrategy>")
print("  <triggers/>")
print("  <disabled>false</disabled>")
print("  <sources class=\"jenkins.branch.MultiBranchProject$BranchSourceList\" plugin=\"branch-api@2.5.5\">")
print("    <data>")
print("      <jenkins.branch.BranchSource>")
print("        <source class=\"org.jenkinsci.plugins.github_branch_source.GitHubSCMSource\" plugin=\"github-branch-source@2.5.8\">")
print("          <id>blueocean</id>")
print("          <apiUri>https://api.github.com</apiUri>")
print("          <credentialsId>github</credentialsId>")
print("          <repoOwner>virnect-corp</repoOwner>")
print("          <repository>PF-demo1</repository>")
print("          <repositoryUrl>https://github.com/virnect-corp/PF-demo1</repositoryUrl>")
print("          <traits>")
print("            <org.jenkinsci.plugins.github__branch__source.BranchDiscoveryTrait>")
print("              <strategyId>3</strategyId>")
print("            </org.jenkinsci.plugins.github__branch__source.BranchDiscoveryTrait>")
print("            <org.jenkinsci.plugins.github__branch__source.ForkPullRequestDiscoveryTrait>")
print("              <strategyId>1</strategyId>")
print("              <trust class=\"org.jenkinsci.plugins.github_branch_source.ForkPullRequestDiscoveryTrait$TrustPermission\"/>")
print("            </org.jenkinsci.plugins.github__branch__source.ForkPullRequestDiscoveryTrait>")
print("            <org.jenkinsci.plugins.github__branch__source.OriginPullRequestDiscoveryTrait>")
print("              <strategyId>1</strategyId>")
print("            </org.jenkinsci.plugins.github__branch__source.OriginPullRequestDiscoveryTrait>")
print("            <jenkins.plugins.git.traits.CleanBeforeCheckoutTrait plugin=\"git@4.0.0\">")
print("              <extension class=\"hudson.plugins.git.extensions.impl.CleanBeforeCheckout\"/>")
print("            </jenkins.plugins.git.traits.CleanBeforeCheckoutTrait>")
print("            <jenkins.plugins.git.traits.CleanAfterCheckoutTrait plugin=\"git@4.0.0\">")
print("              <extension class=\"hudson.plugins.git.extensions.impl.CleanCheckout\"/>")
print("            </jenkins.plugins.git.traits.CleanAfterCheckoutTrait>")
print("            <jenkins.plugins.git.traits.LocalBranchTrait plugin=\"git@4.0.0\">")
print("              <extension class=\"hudson.plugins.git.extensions.impl.LocalBranch\">")
print("                <localBranch>**</localBranch>")
print("              </extension>")
print("            </jenkins.plugins.git.traits.LocalBranchTrait>")
print("          </traits>")
print("        </source>")
print("      </jenkins.branch.BranchSource>")
print("    </data>")
print("    <owner class=\"org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject\" reference=\"../..\"/>")
print("  </sources>")
print("  <factory class=\"org.jenkinsci.plugins.workflow.multibranch.WorkflowBranchProjectFactory\">")
print("    <owner class=\"org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject\" reference=\"../..\"/>")
print("    <scriptPath>Jenkinsfile</scriptPath>")
print("  </factory>")
print("</org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject>")
'''
'''
str ="<?xml version='1.1' encoding='UTF-8'?>\n"
str +="<org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject plugin=\"workflow-multibranch@2.21\">\n"
str +="  <actions/>\n"
str +="  <properties>\n"
str +="    <org.jenkinsci.plugins.configfiles.folder.FolderConfigFileProperty plugin=\"config-file-provider@3.6.3\">\n"
str +="      <configs class=\"sorted-set\">\n"
str +="        <comparator class=\"org.jenkinsci.plugins.configfiles.ConfigByIdComparator\"/>\n"
str +="      </configs>\n"
str +="    </org.jenkinsci.plugins.configfiles.folder.FolderConfigFileProperty>\n"
str +="    <io.jenkins.blueocean.rest.impl.pipeline.credential.BlueOceanCredentialsProvider_-FolderPropertyImpl plugin=\"blueocean-pipeline-scm-api@1.22.0\">\n"
str +="      <domain plugin=\"credentials@2.3.1\">\n"
str +="        <name>blueocean-folder-credential-domain</name>\n"
str +="        <description>Blue Ocean Folder Credentials domain</description>\n"
str +="        <specifications/>\n"
str +="      </domain>\n"
str +="      <user>virnect</user>\n"
str +="      <id>github</id>\n"
str +="    </io.jenkins.blueocean.rest.impl.pipeline.credential.BlueOceanCredentialsProvider_-FolderPropertyImpl>\n"
str +="  </properties>\n"
str +="  <folderViews class=\"jenkins.branch.MultiBranchProjectViewHolder\" plugin=\"branch-api@2.5.5\">\n"
str +="    <owner class=\"org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject\" reference=\"../..\"/>\n"
str +="  </folderViews>\n"
str +="  <healthMetrics>\n"
str +="    <com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric plugin=\"cloudbees-folder@6.11\">\n"
str +="      <nonRecursive>false</nonRecursive>\n"
str +="    </com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric>\n"
str +="  </healthMetrics>\n"
str +="  <icon class=\"jenkins.branch.MetadataActionFolderIcon\" plugin=\"branch-api@2.5.5\">\n"
str +="    <owner class=\"org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject\" reference=\"../..\"/>\n"
str +="  </icon>\n"
str +="  <orphanedItemStrategy class=\"com.cloudbees.hudson.plugins.folder.computed.DefaultOrphanedItemStrategy\" plugin=\"cloudbees-folder@6.11\">\n"
str +="    <pruneDeadBranches>true</pruneDeadBranches>\n"
str +="    <daysToKeep>-1</daysToKeep>\n"
str +="    <numToKeep>-1</numToKeep>\n"
str +="  </orphanedItemStrategy>\n"
str +="  <triggers/>\n"
str +="  <disabled>false</disabled>\n"
str +="  <sources class=\"jenkins.branch.MultiBranchProject$BranchSourceList\" plugin=\"branch-api@2.5.5\">\n"
str +="    <data>\n"
str +="      <jenkins.branch.BranchSource>\n"
str +="        <source class=\"org.jenkinsci.plugins.github_branch_source.GitHubSCMSource\" plugin=\"github-branch-source@2.5.8\">\n"
str +="          <id>blueocean</id>\n"
str +="          <apiUri>https://api.github.com</apiUri>\n"
str +="          <credentialsId>github</credentialsId>\n"
str +="          <repoOwner>virnect-corp</repoOwner>\n"
str +="          <repository>"+sys.argv[1]+"</repository>\n"
str +="          <repositoryUrl>https://github.com/virnect-corp/"+sys.argv[1]+"</repositoryUrl>\n"
str +="          <traits>\n"
str +="            <org.jenkinsci.plugins.github__branch__source.BranchDiscoveryTrait>\n"
str +="              <strategyId>3</strategyId>\n"
str +="            </org.jenkinsci.plugins.github__branch__source.BranchDiscoveryTrait>\n"
str +="            <org.jenkinsci.plugins.github__branch__source.ForkPullRequestDiscoveryTrait>\n"
str +="              <strategyId>1</strategyId>\n"
str +="              <trust class=\"org.jenkinsci.plugins.github_branch_source.ForkPullRequestDiscoveryTrait$TrustPermission\"/>\n"
str +="            </org.jenkinsci.plugins.github__branch__source.ForkPullRequestDiscoveryTrait>\n"
str +="            <org.jenkinsci.plugins.github__branch__source.OriginPullRequestDiscoveryTrait>\n"
str +="              <strategyId>1</strategyId>\n"
str +="            </org.jenkinsci.plugins.github__branch__source.OriginPullRequestDiscoveryTrait>\n"
str +="            <jenkins.plugins.git.traits.CleanBeforeCheckoutTrait plugin=\"git@4.0.0\">\n"
str +="              <extension class=\"hudson.plugins.git.extensions.impl.CleanBeforeCheckout\"/>\n"
str +="            </jenkins.plugins.git.traits.CleanBeforeCheckoutTrait>\n"
str +="            <jenkins.plugins.git.traits.CleanAfterCheckoutTrait plugin=\"git@4.0.0\">\n"
str +="              <extension class=\"hudson.plugins.git.extensions.impl.CleanCheckout\"/>\n"
str +="            </jenkins.plugins.git.traits.CleanAfterCheckoutTrait>\n"
str +="            <jenkins.plugins.git.traits.LocalBranchTrait plugin=\"git@4.0.0\">\n"
str +="              <extension class=\"hudson.plugins.git.extensions.impl.LocalBranch\">\n"
str +="                <localBranch>**</localBranch>\n"
str +="              </extension>\n"
str +="            </jenkins.plugins.git.traits.LocalBranchTrait>\n"
str +="          </traits>\n"
str +="        </source>\n"
str +="      </jenkins.branch.BranchSource>\n"
str +="    </data>\n"
str +="    <owner class=\"org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject\" reference=\"../..\"/>\n"
str +="  </sources>\n"
str +="  <factory class=\"org.jenkinsci.plugins.workflow.multibranch.WorkflowBranchProjectFactory\">\n"
str +="    <owner class=\"org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject\" reference=\"../..\"/>\n"
str +="    <scriptPath>Jenkinsfile</scriptPath>\n"
str +="  </factory>\n"
str +="</org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject>"
print(str)
'''
jobs = server.create_job(sys.argv[1],str)
print(jobs)
