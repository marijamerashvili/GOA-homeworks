'''1) შეამოწმე არის თუ არა ორი ცვლადიდან ერთი მაინც მართალი
2) შეამოწმე ორივე ცვლადი  მართალია თუ არა
3) შეამოწმე არის თუ არა ორი რიცხვი თანაბარი  ან პირველი რიცხვი მეტი მეორეზე.
4) შეამოწმე არის თუ არა ბავშვის ასაკი 6-დან 12 წლამდე.
5) bonus (მოცემურია ორი ლოგიკური ცვლადი. მათი საწინააღმდეგო მმნიშვნელობა გამოთვალე მხოლოდ and და or ოპერატორების გამოყენებით)'''

#დავალება 1

goashi_chartva = True
clasworkis_dawera = False
print(goashi_chartva or clasworkis_dawera)

#დავალება 2 

x = True
y =True
print(x and y)

#დავალება 3 

x = 5 
y = 10
print(5 == 10)
print(5>10)

#დავალება 4 

bavshvi = 10
print(6< bavshvi <12)

#დავალება 5

otaxis_milageba = False
garet_gasvla =False
print(otaxis_milageba or garet_gasvla)
print(otaxis_milageba and garet_gasvla)
