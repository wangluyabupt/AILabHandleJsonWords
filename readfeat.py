def redis_nil():
    f=open("feat",'r')
    lines=f.readlines()

    for line in lines:
        # j=json.dumps(line)
        # vid=json.load(line)
        # print(vid["vid"])

        l=line.split("\"feat\": [")
        for item in l[1:]:
            try:
                feats = item.split(']')[0]
                # print(feats)
                newfeats=feats.split(',')
                print(len(newfeats))


            except:
                pass
    f.close()
if __name__ == '__main__':
    redis_nil()