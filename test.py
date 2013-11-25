#Import the humansTxt library
import humans

#Setup our Github urls to feed to the HumansTxt generator.
#GitHub urls need to point to the github contributors api.  Support for local git repositorys will be added soon
#We only have one right now, but we could add more.
gitHub = []
gitHub.append(humans.URL('https://api.github.com/repos/mozilla/kuma/contributors','Contributors on Github','Developer'))

#Same with the SVN repos.
svn = []
svn.append(humans.URL('http://svn.mozilla.org/projects/mdn/trunk/locale/','Localization Contributors','Localizer'))

#Open our target file.  Normaly this would be wherever our root web host is, but for demo we'll put it in the same folder
target = open("humans.txt", 'w')

#Create an instance of the HumansTXT generator
TXT = humans.HumansTXT()

#Generate the file using our github and svn repos
TXT.generate_file(target,gitHub,svn)

#close the file now that we are done.
target.close()
