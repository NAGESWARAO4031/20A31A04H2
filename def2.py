def out():
    var=10
    def innf():
        var=20
        print("inner var",var)
    innf()
    print("outer var",var)
out()