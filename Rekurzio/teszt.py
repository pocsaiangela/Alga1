from feladat import create_palindrome_recursive

def test(expected, s):
    result = create_palindrome_recursive(s)

    correct = result != "NO SOLUTION"
    print(correct == expected)


test(True, "tacocat")
test(False, "AAAACACBAD")
test(True, "AAAACACBA")
test(True, "HANNAH")
test(True, "TACOCATOtacocat")
test(True, "indulagorogaludni")
test(False, "algabeadando")
test(False, "iloverecursion")
test(True, "eAAAACACBAe")
test(True, "")
test(True, "neveroddoreven")
test(True, "dogeeseseegod")

