str = ' X -DSPAM-Confidence:0.8475 ' 
colonpos = str. find(':' )
data=str[ colonpos+1:]
print(float(data))
