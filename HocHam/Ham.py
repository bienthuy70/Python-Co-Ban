def(a,b):
    if a is 0 and b is 0:
        return "Phương trình có vô số nghiệm"
    elif a is 0 and b !=0:
        return "Phương trình vô nghiệm"
    else:
        return "Phương trình có một nghiệm duy nhất x = {0}".format(-b/a)
