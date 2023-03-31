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


def BadgeWorkFlow(reponame, platform, compiler):
    compiler_percent20 = compiler.replace(" ", "%20")
    compiler_plus = compiler.replace(" ", "+")
    return f'[![{platform} {compiler}](https://github.com/sintef-ocean/{reponame}/workflows/{platform}%20{compiler_percent20}/badge.svg)](https://github.com/sintef-ocean/{0}/actions?query=workflow%3A"{platform}{compiler_plus}")'


def TableHeader():
    return "Software | Recipe | Configurations\n---|---|---\n"


def TransitiveHeader():
    return "## Status for 3rd-party Conan recipes\n\nSoftware | Recipe\n---|---\n"


def WriteRow(libname, homepage, repo, reponame, inTable):
    if not inTable:
        return "{}\n{}\n{}\n{}\n{}\n".format(
            BadgeWorkFlow(reponame, 'Linux', 'GCC'),
            BadgeWorkFlow(reponame, 'Linux', 'Clang'),
            BadgeWorkFlow(reponame, 'Windows', 'MSVC'),
            BadgeWorkFlow(reponame, 'Windows', 'MSVC Clang'),
            BadgeWorkFlow(reponame, 'Macos', 'Apple-Clang')
            )
    else:
        return "{}|{}|{}{}{}{}{}\n".format(
            SoftwareLink(libname, homepage),
            RecipeLink(repo, reponame),
            BadgeWorkFlow(reponame, 'Linux', 'GCC'),
            BadgeWorkFlow(reponame, 'Linux', 'Clang'),
            BadgeWorkFlow(reponame, 'Windows', 'MSVC'),
            BadgeWorkFlow(reponame, 'Windows', 'MSVC Clang'),
            BadgeWorkFlow(reponame, 'Macos', 'Apple-Clang'))

def WriteTransitiveRow(libname, homepage, repo, reponame):
    return "{}|{}\n".format(
        SoftwareLink(libname, homepage),
        Repo3rdParty(repo, reponame))


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

        fil.write("# Status for own Conan recipes\n\n")
        fil.write("\nTo setup this remote:\n")
        fil.write("`conan remote add [REMOTE] https://artifactory.smd.sintef.no/artifactory/api/conan/conan-local`\n\n")
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
                aLine = WriteTransitiveRow(row['library'], row['homepage'], row['repo'], row['reponame'])
                fil.write(aLine)
            fil.write("\n\nAdd new row to table: See [scripts/README.md](scripts/README.md)\n")
        fil.write("\n----\n")

        fil.write("## Build matrix configuration for recipes\n")
        with open('BuildMatrix.md', 'rt') as footer:
            data = footer.read()
            fil.write(data)
