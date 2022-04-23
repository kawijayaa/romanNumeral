while True:
    arabic_number = input("Enter number: ")
    final = []
    if int(arabic_number) > 3999:
        print("Number too big!")
    else:
        for i in range(1,5):
            try:
                if i == 1:
                    match arabic_number[i*-1]:
                        case "0":
                            final.append("")
                        case "1":
                            final.append("I")
                        case "2":
                            final.append("II")
                        case "3":
                            final.append("III")
                        case "4":
                            final.append("IV")
                        case "5":
                            final.append("V")
                        case "6":
                            final.append("VI")
                        case "7":
                            final.append("VII")
                        case "8":
                            final.append("VIII")
                        case "9":
                            final.append("IX")
                elif i == 2:
                    match arabic_number[i*-1]:
                        case "0":
                            final.append("")
                        case "1":
                            final.append("X")
                        case "2":
                            final.append("XX")
                        case "3":
                            final.append("XXX")
                        case "4":
                            final.append("XL")
                        case "5":
                            final.append("L")
                        case "6":
                            final.append("LX")
                        case "7":
                            final.append("LXX")
                        case "8":
                            final.append("LXXX")
                        case "9":
                            final.append("XC")
                elif i == 3:
                    match arabic_number[i*-1]:
                        case "0":
                            final.append("")
                        case "1":
                            final.append("C")
                        case "2":
                            final.append("CC")
                        case "3":
                            final.append("CCC")
                        case "4":
                            final.append("CD")
                        case "5":
                            final.append("D")
                        case "6":
                            final.append("DC")
                        case "7":
                            final.append("DCC")
                        case "8":
                            final.append("DCCC")
                        case "9":
                            final.append("CM")
                elif i == 4:
                    match arabic_number[i*-1]:
                        case "0":
                            final.append("")
                        case "1":
                            final.append("M")
                        case "2":
                            final.append("MM")
                        case "3":
                            final.append("MMM")
            except:
                continue
        print("".join(final[::-1]))