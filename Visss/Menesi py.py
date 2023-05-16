vieni = {
    0:'ais', 1:" pirmais", 2:" otrais", 3:" trešais", 4:" ceturtais", 5:" piektais", 6:" sestais", 7:" septītais", 8:" astotais", 9:" devītais"
}
padsmiti = {
    0:"desmitais", 1:"vienpadsmitais", 2:"divpadsmitais", 3:"trīspadsmitais", 4:"četrpadsmitais", 5:"piecpadsmitais", 6:"sešpadsmitais", 7:"septiņpadsmitais", 8:"astoņpadsmitais", 9:"deviņpadsmitais"
}
menesi = {
  1:"janvāris", 2:"februāris", 3:"marts", 4:"aprīlis", 5:"maijs", 6:"jūnijs", 7:"jūlijs", 8:"augusts", 9:"septembris", 10:"oktobris", 11:"novembris", 12:"decembris"
}
desmiti={
0:"",1:"desmit", 2:"divdesmit",3:"trisdesmit"
}
date = input("Input date (format-03.04) ")
skaitli=date.split(".")
month=int(skaitli[1])

day=(skaitli[0])
day1=int(day[0])
day2=int(day[1])


if day1==1:
    print(padsmiti[day2],menesi[month])
else:
    print(desmiti[day1]+vieni[day2],menesi[month])