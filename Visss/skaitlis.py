import webbrowser

url = 'https://weed.com/'

x = input('Enter 3 diggit number:')
while len(x) != 3:
    x = input('Enter 3 diggit number:')
vieni = {'1':'viens','1':'divi','3':'tris','4':'cetri','5':'pieci','6':'sesi','7':'septini','8':'astoni','9':'devini','0':''}
desmiti={'1':'desmit','2':'divdesmit','3':'trisdesmit','4':'cetrdesmit','5':'piecdesmit','6':'sesdesmit','7':'septini','8':'astondesmit','9':'devindesmit','0':''}
simti={'1':'simts','2':'divsimts','3':'trissimts','4':'cetrsimts','5':'piecsimts','6':'sessimts','7':'septinsimts','8':'astonsimts','9':'devinsimts','0':''}
padsmiti={'1':'vienpadsmit','2':'divpadsmit','3':'trispadsmit','4':'cetrpadsmit','5':'piecpadsmit','6':'sespadsmit','7':'septinpadsmit','8':'astonpadsmit','9':'devinpadsmit','0':'desmit'}

if x=='420':
    webbrowser.open(url)
elif x[1] == '1':
    print(simti[x[0]],padsmiti[x[2]])
else:
    print(simti[x[0]],desmiti[x[1]],vieni[x[2]])





















# vieni = {
#     0:'ais', 1:"pirmais", 2:"otrais", 3:"trešais", 4:"ceturtais", 5:"piektais", 6:"sestais", 7:"septītais", 8:"astotais", 9:"devītais"
# }

# padsmiti = {
#     0:"desmitais", 1:"vienpadsmitais", 2:"divpadsmitais", 3:"trīspadsmitais", 4:"četrpadsmitais", 5:"piecpadsmitais", 6:"sešpadsmitais", 7:"septiņpadsmitais", 8:"astoņpadsmitais", 9:"deviņpadsmitais"
# }

# desmiti = {
#     0: ' ', 1:' ', 2:"divdesmit", 3:"trīsdesmit"
# }

# menesi = {
#     1:"janvāris", 2:"februāris", 3:"marts", 4:"aprīlis", 5:"maijs", 6:"jūnijs", 7:"jūlijs", 8:"augusts", 9:"septembris", 10:"oktobris", 11:"novembris", 12:"decembris"
# }

# date = input("ievadi datumu: ")
# datums = date.split(".")
    # d = int(datums[0])
    # m = int(datums[1])

# diena = []

# while d > 0:
#     p = d % 10
#     diena.insert(0, p)
#     d = d//10

# print(diena)
# print(menesi[m])