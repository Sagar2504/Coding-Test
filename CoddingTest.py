def getuserin():
    intin = int(input(""))
    list1 = []
    if intin >= 1 and intin <= 100:
        while intin != 0:
            str1 = input("")
            str2 = input("")

            if len(str1) <= 1000 and len(str2) <= 100000:
                varlen = 0
                for j in str1:
                    if j in str2:
                        varlen += 1
                if varlen == len(str1):
                    list1.append("yes")
                    intin -= 1
                else:
                    list1.append("NO")
                    intin -= 1
            else:
                pass


        for i in list1:
            print(i)
    else:
        pass

getuserin()
