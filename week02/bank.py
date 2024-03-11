#weekly task 2
#Applying the input function and arithmetic operators
#Author: ebelechukwu Igwagu
item1 = input ("Enter cost for item 1 in cent: ")
item2 = input ("Enter cost for item 2 in cent: ")
total = int(item1) + int(item2)
euro =  (total/100)
#{:.2f} formats the amount to 2 decimal places
print ("€{:.2f}".format(euro))
#using the locale function to set the currency used in a region
import locale
print(locale.setlocale(locale.LC_ALL, ''))
print(locale.setlocale(locale.LC_ALL, 'en_150'))
item1 = int (input ("Enter cost for item 1 in cent: "))
item2 = int (input ("Enter cost for item 2 in cent: "))
total = item1 + item2
euro = (total/100)
print ("€{:.2f}".format(euro))








#References
#https://docs.python.org/3/library/locale.html
#https://stackabuse.com/format-number-as-currency-string-in-python/
#https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/70feba9f-294e-491e-b6eb-56532684c37f