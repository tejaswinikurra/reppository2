class India:
    def capital(self):
        print("delhi is the captial of india")
    def language(self):
        print("hindi is the most widely spoken language in india")
    def position(self):
        print("india is a developing country")

class America:
    def capital(self):
        print("washington dc is the capital of america")
    def language(self):
        print("english is the official language of america")
    def position(self):
        print("america is a developed country")

ob_ind=India()
ob_ame=America()

for coun in(ob_ind, ob_ame):
    coun.capital()
    coun.language()
    coun.position()
    