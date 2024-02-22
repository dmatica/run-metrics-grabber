import sys
import clipboard
data = sys.argv[1]
f = open(data,'r')
x = (f.read().replace(',','').splitlines())
z = 2
tot=''
l1cd=''
l2cd=''
l3cd=''
l4cd=''
l5cd=''
l6cd=''
l7cd=''
l8cd=''
for i in range(0,len(x)-1):
    if(len(x[i])>0):
        if(x[i].split()[0]=="Total"):
            z=i+1
            tot = (x[i].split()[0]+": Q30 = ",x[i].split()[6]+"%, Yield = ",x[i].split()[1]," Gbp, Aligned = ",x[i].split()[3]+"%, Error rate = ",x[i].split()[4]+"%")
y = x[1:z]

lanes=[]
#print(x, type(x))
start=0
end=0
for i in range(5,len(x)-1):
    if x[i]=='' and x[i-1]=='':
        start = i+1
for i in range(start+1,len(x)-1):
    if x[i].split()[0]=="Read" or x[i].split()[0]=="Extracted:":
        end=i
lanes=x[start:end]
#print(start,end,end,end)
for i in range(0,len(lanes)):
    #print(lanes[i])
    #print(lanes[i].split()[0],lanes[i].split()[1])
    if lanes[i].split()[0]=="1" and lanes[i].split()[1]=="-":
        l1cd="Lane 1: RawCD = "+lanes[i].split()[3]," k/mm^2 ",lanes[i].split()[4]," ",lanes[i].split()[5],", PF = "+lanes[i].split()[6],"% ",lanes[i].split()[7]," ",lanes[i].split()[8]
    if lanes[i].split()[0]=="2" and lanes[i].split()[1]=="-":
        l2cd="Lane 2: RawCD = "+lanes[i].split()[3]," k/mm^2 ",lanes[i].split()[4]," ",lanes[i].split()[5],", PF = "+lanes[i].split()[6],"% ",lanes[i].split()[7]," ",lanes[i].split()[8]
    if lanes[i].split()[0]=="3" and lanes[i].split()[1]=="-":
        l3cd="Lane 3: RawCD = "+lanes[i].split()[3]," k/mm^2 ",lanes[i].split()[4]," ",lanes[i].split()[5],", PF = "+lanes[i].split()[6],"% ",lanes[i].split()[7]," ",lanes[i].split()[8]
    if lanes[i].split()[0]=="4" and lanes[i].split()[1]=="-":
        l4cd="Lane 4: RawCD = "+lanes[i].split()[3]," k/mm^2 ",lanes[i].split()[4]," ",lanes[i].split()[5],", PF = "+lanes[i].split()[6],"% ",lanes[i].split()[7]," ",lanes[i].split()[8]
    if lanes[i].split()[0]=="5" and lanes[i].split()[1]=="-":
        l5cd="Lane 5: RawCD = "+lanes[i].split()[3]," k/mm^2 ",lanes[i].split()[4]," ",lanes[i].split()[5],", PF = "+lanes[i].split()[6],"% ",lanes[i].split()[7]," ",lanes[i].split()[8]
    if lanes[i].split()[0]=="6" and lanes[i].split()[1]=="-":
        l6cd="Lane 6: RawCD = "+lanes[i].split()[3]," k/mm^2 ",lanes[i].split()[4]," ",lanes[i].split()[5],", PF = "+lanes[i].split()[6],"% ",lanes[i].split()[7]," ",lanes[i].split()[8]
    if lanes[i].split()[0]=="7" and lanes[i].split()[1]=="-":
        l7cd="Lane 7: RawCD = "+lanes[i].split()[3]," k/mm^2 ",lanes[i].split()[4]," ",lanes[i].split()[5],", PF = "+lanes[i].split()[6],"% ",lanes[i].split()[7]," ",lanes[i].split()[8]
    if lanes[i].split()[0]=="8" and lanes[i].split()[1]=="-":
        l8cd="Lane 8: RawCD = "+lanes[i].split()[3]," k/mm^2 ",lanes[i].split()[4]," ",lanes[i].split()[5],", PF = "+lanes[i].split()[6],"% ",lanes[i].split()[7]," ",lanes[i].split()[8]
#print("\n".join([''.join(l1cd),''.join(l2cd),''.join(l3cd),''.join(l4cd),''.join(l5cd),''.join(l6cd),''.join(l7cd),''.join(l8cd)]))

#print(sys.argv)

if len(sys.argv)>2:
    ##Read by read
    clipboard.copy("\n".join(['\n'.join(y),''.join(x[-1]+" cycles"),'',''.join(l1cd),''.join(l2cd),''.join(l3cd),''.join(l4cd),''.join(l5cd),''.join(l6cd),''.join(l7cd),''.join(l8cd)]).strip())
else:
    ##Total
    clipboard.copy("\n".join([x[1],''.join(tot),''.join(x[-1]+" cycles"),'',''.join(l1cd),''.join(l2cd),''.join(l3cd),''.join(l4cd),''.join(l5cd),''.join(l6cd),''.join(l7cd),''.join(l8cd)]).strip())