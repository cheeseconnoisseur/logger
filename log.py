from time import gmtime, strftime

showtime = strftime("%H:%M:%S %Y-%m-%d", gmtime())
with open("your path","a") as f:
    f.write(showtime)
    f.write("\n")
    f.close()
