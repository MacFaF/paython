with open (r"jash.txt") as fh:
    with open (r"bash.txt","w") as fh1:
        i=0
        for ln in fh:
            fh1.write(str(i)+ln)
            i=i+1
