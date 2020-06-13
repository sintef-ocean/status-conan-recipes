import csv


def SoftwareLink(libname, homepage):
    return "[{}]({})".format(libname, homepage)


def RecipeLink(repo, reponame):
    if repo == "bitbucket":
        s = "bitbucket.org"
    elif repo == "github":
        s = "github.com"
    else:
        raise NameError("Unknown repo: {}".format(repo))

    return '[<img src="https://{0}/favicon.ico" height="28">](https://{0}/sintef-ocean/{1})'.format(s, reponame)


def Repo3rdParty(repo, reponame):
    if repo == "github":
        s = "github.com"
    else:
        raise NameError("Unknown repo: {}".format(repo))

    return '[<img src="https://{0}/favicon.ico" height="28">](https://{0}/{1})'.format(s, reponame)


def BadgeBintray(libname, user='sintef'):
    return "[![Download](https://api.bintray.com/packages/sintef-ocean/conan/{libname}%3A{user}/images/download.svg)](https://bintray.com/sintef-ocean/conan/{libname}%3A{user}/_latestVersion)".format(libname=libname, user=user)


def BadgeWorkFlow(reponame, compiler):
    return '[![{1} Conan](https://github.com/sintef-ocean/{0}/workflows/{1}%20Conan/badge.svg)](https://github.com/sintef-ocean/{0}/actions?query=workflow%3A"{1}+Conan")'.format(reponame, compiler)


def TableHeader():
    return "# Status for own Conan recipes\n\nSoftware | Recipe | GCC | Clang | MSVC | Bintray\n---|---|---|---|---|---\n"

def TransitiveHeader():
    return "## Status for 3rd-party Conan recipes\n\nSoftware | Recipe | Bintray\n---|---|---\n"

def WriteRow(libname, homepage, repo, reponame, inTable):
    if not inTable:
        return "{}\n{}\n{}\n{}\n".format(
            BadgeWorkFlow(reponame, 'GCC'),
            BadgeWorkFlow(reponame, 'Clang'),
            BadgeWorkFlow(reponame, 'MSVC'),
            BadgeBintray(libname))
    else:
        return "{}|{}|{}|{}|{}|{}\n".format(
            SoftwareLink(libname, homepage),
            RecipeLink(repo, reponame),
            BadgeWorkFlow(reponame, 'GCC'),
            BadgeWorkFlow(reponame, 'Clang'),
            BadgeWorkFlow(reponame, 'MSVC'),
            BadgeBintray(libname))

def WriteTransitiveRow(libname, homepage, repo, reponame, user):
    return "{}|{}|{}".format(
        SoftwareLink(libname, homepage),
        Repo3rdParty(repo, reponame),
        BadgeBintray(libname, user))

def GetStatusFor(library):
    with open('list.csv', 'rt') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if library == row['library']:
                print(WriteRow(row['library'], row['homepage'], row['repo'],
                               row['reponame'], False))


def WriteLibReadmeFor(library):
    with open('list.csv', 'rt') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if library == 'ALL' or library == row['library']:
                with open('TemplateReadme.md', 'rt') as mdfile:
                    temp = mdfile.read()
                with open('README_{}.md'.format(row['library']), 'w') as fil:
                    fil.write(temp.format(WriteRow(row['library'],
                                                   row['homepage'],
                                                   row['repo'],
                                                   row['reponame'],
                                                   False),
                                          row['library'],
                                          row['homepage'],
                                          row['version'],
                                          row['opt_example']))


def WriteLibReadme(libname, homepage, repo, reponame, version, opt_ex):
    with open('TemplateReadme.md', 'rt') as mdfile:
        temp = mdfile.read()


def WriteStatusFile():
    with open('Out.md', 'w') as fil:
        fil.write(TableHeader())
        with open('list.csv', 'rt') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                aLine = WriteRow(row['library'], row['homepage'], row['repo'],
                                 row['reponame'], True)
                fil.write(aLine)
        fil.write("\n----\n")
        fil.write(TransitiveHeader())
        with open('transitive.csv', 'rt') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                aLine = WriteTransitiveRow(row['library'], row['homepage'], row['repo'],
                                 row['reponame'], row['bintray-user'])
                fil.write(aLine)
            fil.write("\n\nAdd new row to table: See [scripts/README.md](scripts/README.md)")
