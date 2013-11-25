import json
import urllib
import subprocess

class Human:
    def __init__(self):
        self.name = None
        self.website = None

class URL:
    def __init__(self,url,header=None,prepend=None):
        self.header = header
        self.prepend = prepend
        self.url = url

class HumansTXT:
    def generate_file(self,target,githubURLs,svnURLs):

        for github in githubURLs:
            githubbers = self.get_github(github.url)
        self.write_to_file(githubbers, target, github.header, 
            github.prepend)

        for svn in svnURLs:
            svners = self.get_svn(svn.url)
        self.write_to_file(svners, target, svn.header, 
            svn.prepend)

    def write_to_file(self, humans, target, message, role):
        target.write("%s \n" % message)
        for h in humans:
            target.write("%s: %s \n" % (role, h.name.encode('ascii', 'ignore')))
            if(h.website != None):
                target.write("Website: %s \n" % h.website)
                target.write('\n')
        target.write('\n')

    def get_github(self, url):
        data = json.load(urllib.urlopen(url))

        humans = []
        for contributor in data:
            human = Human()
            try:
                human.name = contributor['name']
            except:  # Github doesn't have a name if profile isn't filled out
                human.name = contributor['login']

            try:
                human.website = contributor['blog']
            except:
                human.website = None

            humans.append(human)

        return humans

    def get_svn(self, url):
        p = subprocess.Popen("svn log --quiet "+url+" | grep '^r' | awk '{print $3}' | sort | uniq",
            shell=True, stdout=subprocess.PIPE)
        contributers_list = p.communicate()[0].rstrip().split('\n', -1)

        humans = []
        for contributer in contributers_list:
            human = Human()
            human.name = contributer
            humans.append(human)

        return humans
