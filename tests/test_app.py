from neg import make_negation

def test_index():
    truth=[False,False,True]
    s=make_negation()
    for i in range(0,len(truth)):
        assert truth[i]==s[i]
