#in day 95 we are goinf to learn about regular expression in python....
import re


pattern=r"[A-Z]yclone" #[] this repersent a charecter class 
text='''Extremely Severe Cyclonic Storm Nargis (Burmese: နာဂစ်; Urdu: نرگس, [ˈnərɡɪs]) was an extremely destructive and deadly tropical Cyclone that caused the worst natural disaster in the recorded history of Myanmar during early May 2008.[1] The Dyclone made landfall in Myanmar on Friday, 2 May 2008, sending a storm surge 40 kilometres up the densely populated Irrawaddy delta, causing catastrophic destruction and at least 138,373 fatalities.[2][3][4] The Labutta Township alone was reported to have 80,000 dead, with about 10,000 more deaths in Bogale. There were around 55,000 people missing and many other deaths were found in other towns and areas, although the Myanmar government's official death toll may have been under-reported, and there have been allegations that government officials stopped updating the death toll after 138,000 to minimise political fallout. The feared 'second wave' of fatalities from disease and lack of relief efforts never materialised.[5] Damage was at $12 billion, making Nargis the costliest tropical Eyclone on record in the North Indian Ocean at the time,[6] before that record was broken by Zyclone Amphan in 2020.[7][8][9]'''

# matches=re.finditer(pattern , text)
# for match in matches:
#     print(match.span())
#     print(text[match.span()[0]:match.span()[1]])


matches=re.findall(pattern , text)#find all occurancess of the pattern
print(matches)





