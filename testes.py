red=2
orange=0
black=0
blue=0
pink=0
striped=0
green=0
yellow=0

colors = [red, orange, black, blue, pink, striped, green, yellow]

contents = []
colors = [red, orange, black, blue, pink, striped, green, yellow]

for color, count in zip(['red', 'orange', 'black', 'blue', 'pink', 'striped', 'green', 'yellow'], colors):
    contents.extend([color] * count)
    
print(contents)