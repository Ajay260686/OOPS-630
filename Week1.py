class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, word):
        return word in self.__myTeam

    def __iter__(self):
        return iter(self.__myTeam)


def main():
    """Creating object of Teams Class """
    classmates = Teams(['John', 'Steve', 'Tim'])
    """Printing Length of values available in classmates Object """
    print("Teams Length::", len(classmates))
    """Checking Whether Tim is available in classmates Object """
    print("Is Tim Available in Team::", "Tim" in classmates)
    """Checking Whether Sam is available in classmates Object """
    print("Is Sam Available in Team::", "Sam" in classmates)
    print('<------------Printing Team Members---------->')
    """Iterating values of __myTeams attribute from Object """
    for words in classmates:
        print(words)
    """Checking whether __Len__ Method is available in Teams class or not"""
    if hasattr(classmates, '__len__'):
        print('__len__ Exist')


main()
