import pandas as pd, re

def find_mention(text):
    m=re.match(r"@(\w+)", str(text))
    return m


def find_hashtag(text):
    h=re.match(r"#(\w+)", str(text))
    return h

df = pd.read_csv("Constraint_Train.csv", encoding = "ISO-8859-1")
df1= pd.read_csv("Constraint_Val.csv", encoding = "ISO-8859-1")

df=(df.append(df1)).sample(frac=1).reset_index(drop=True)

res=[]
labels=[]

mm=0
hh=0

for st, lb in zip(df['text'], df['label']):
    m=find_mention(str(st))
    h=find_hashtag(str(st))

    if m!=None and h!=None:
        print("**************************")
        res.append(st)
        labels.append(lb)

    elif m!=None:
        mm+=1
        print(m)
    elif h!=None:
        print(h)
        hh+=1

print(len(df['text']))
print(mm)
print(hh)

df_out = pd.DataFrame(
    {'text': res,
     'label': labels
    })

df_out.to_csv("text_mention_hashtag.csv", index=False, header=True)