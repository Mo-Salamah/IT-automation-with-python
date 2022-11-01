#%%
import re

#%%
def only_listed(text, charachters=r"[^a-zA-Z0-9]"):
    result = re.search(charachters, text)    
    return result 
    
    



# a followed by 3 b
text = "abbbc s fa as f"
result = re.search(r"abbb[^b]", text)
print(result)


# a followed by by two or three b
text1 = "abb "
text2 = "abbb "
text3 = "abbc "
text4 = "asfsaf abb "
text5 = "sfsfgsg adbb"
def what(text):
    result = re.search(r"a[bb|bbb]", text)
    print(result)

what(text1)
what(text2)
what(text3)
what(text4)
what(text5)
# what(text)
# %%
