def conf(ip, /, porta, *,
         modo=True):
    print(ip, porta, modo)
conf("10.0.0.1", 8080,
     modo=False)