import sys,time
N=-10;S=10
D={'N':(21,19,12,8,-8,-12,-19,-21),'B':(11,9,-9,-11),'R':(10,1,-1,-10)}
D['Q']=D['K']=D['R']+D['B']
V=dict(zip('PNBRQK',(100,320,330,500,900,0)))
h=b"05555550566666656777777677888877"
P={'P':b"0"*8+b"9"*8+b"8"*8+b"7778877766676666"+b"5"*8+b"4"*8+b"0"*8,'N':h+h[::-1],'R':b"5"*8+b"7"*8+b"5"*40+b"4"*8,'K':b"0"*48+b"3"*8+b"78777787"}
P['B']=P['Q']=P['N']
R={95:'KQ',25:'kq',91:'Q',98:'K',21:'q',28:'k'}
T=0;n=0;CR='';M=10**9
def C(c,i,j):
 for x in(i,j):
  for y in R.get(x,''):c=c.replace(y,'')
 return c
def atk(b,s,w):
 v=not w;d=S if w else N;p='Pp'[v]
 if b[s+d-1]==p or b[s+d+1]==p:return 1
 for o in D['N']:
  if b[s+o]=='Nn'[v]:return 1
 for o in D['K']:
  if b[s+o]=='Kk'[v]:return 1
 for o in D['Q']:
  j=s+o
  while b[j]=='.':j+=o
  if b[j]=='Qq'[v] or b[j]==('Bb' if o in D['B'] else 'Rr')[v]:return 1
 return 0
def ev(b):
 t=0
 for s,c in enumerate(b):
  u=c.upper()
  if u in V:
   r=s//10-2 if c<'a' else 9-s//10;x=(P[u][r*8+s%10-1]-53)*10
   t+=(V[u]+x)*(2*(c<'a')-1)
 return t
def cs(b,k,r,x,y,t,w,z):
 v=not w
 return z in CR and b[k]=='Kk'[v] and b[r]=='Rr'[v] and b[x]==b[y]==b[t]=='.' and not(atk(b,k,v)or atk(b,x,v)or atk(b,y,v))
def A(m,v,i,j):
 for k in (800,600,400,200)if j//10 in(2,9)else(0,):m.append((v,i,j+k))
def gen(b,wt,ep,cap=False):
 m=[]
 for i,c in enumerate(b):
  if c<'0' or (c<'a')!=wt:continue
  u=c.upper()
  if u=='P':
   d=N if wt else S;j=i+d
   if b[j]<'0':
    if not cap:A(m,0,i,j)
    if i//10==3+5*wt and b[i+d+d]<'0' and not cap:m.append((0,i,i+d+d))
   for k in (d-1,d+1):
    j=i+k
    if b[j]>'/' and (b[j]<'a')!=wt:A(m,V[b[j].upper()],i,j)
    elif j==ep:m.append((100,i,j))
  else:
   for d in D[u]:
    j=i+d
    while 1:
     if b[j]==' ':break
     if b[j]<'0':
      if not cap:m.append((0,i,j))
     else:
      if (b[j]<'a')!=wt:m.append((V[b[j].upper()],i,j))
      break
     if u in'NK':break
     j+=d
 if not cap:
  for k,d,z in ((95,1,'K'),(95,-1,'Q')) if wt else ((25,1,'k'),(25,-1,'q')):
   if cs(b,k,k+3*d-(d<0),k+d,k+2*d,k+2*d-(d<0),wt,z):m.append((0,k,k+2*d))
 return sorted(m,reverse=1)
def mk(b,i,j):
 c=b[:];p=c[i];c[i]='.'
 k=j//200
 if k:c[j%200]='NBRQnbrq'[k-1+4*(p>'Z')];j%=200
 else:c[j]=p
 if p in'Pp' and abs(j-i) in(9,11) and b[j]<'0':c[j-10+20*(p<'a')]='.'
 elif p in'Kk'and abs(j-i)==2:
  if j>i:c[j-1]=c[j+1];c[j+1]='.'
  else:c[j+1]=c[j-2];c[j-2]='.'
 return c
def lm(b,wt,ep):
 m=[]
 for _,i,j in gen(b,wt,ep):
  c=mk(b,i,j)
  if b[j%200]not in'Kk'and not atk(c,c.index('Kk'[not wt]),not wt):m.append((i,j,c))
 return m
def qs(b,wt,al,be):
 s=ev(b)*(2*wt-1)
 if s>=be:return be
 if s>al:al=s
 for _,i,j in gen(b,wt,0,1):
  c=mk(b,i,j)
  if atk(c,c.index('Kk'[not wt]),not wt):continue
  s=-qs(c,not wt,-be,-al)
  if s>=be:return be
  if s>al:al=s
 return al
def G(b,i,j):
 return (i+j)//2 if b[i] in'Pp' and abs(j-i)==20 else 0
def sr(b,wt,ep,d,al,be,pl):
 global n,CR;n+=1
 if n%1024==0 and time.time()>T:raise TimeoutError
 if d==0:return qs(b,wt,al,be)
 ms=lm(b,wt,ep)
 if not ms:return -99999+pl if atk(b,b.index('Kk'[not wt]),not wt) else 0
 for i,j,c in ms:
  o=CR;CR=C(CR,i,j%200)
  s=-sr(c,not wt,G(b,i,j),d-1,-be,-al,pl+1)
  CR=o
  if s>=be:return be
  if s>al:al=s
 return al
def parse(f):
 p=f.split();b=list(' '*20+(' '+'.'*8+' ')*8+' '*20)
 s=p[0]
 for d in'12345678':s=s.replace(d,'.'*int(d))
 for i,ch in enumerate(s.replace('/','')):b[(i//8+2)*10+i%8+1]=ch
 wt=len(p)<2 or p[1]=='w';ep=0;cr=p[2]if len(p)>2 else''
 if len(p)>3 and p[3]!='-':ep=(10-int(p[3][1]))*10+ord(p[3][0])-96
 return b,wt,ep,cr
def sq(s):return chr(s%10+96)+str(10-s//10)
def main():
 global T,CR
 a=sys.argv[1:]or sys.stdin.read().strip().split('\n')
 f=a[0];tl=float(a[1])if len(a)>1 else 2
 b,wt,ep,cr=parse(f);CR=cr
 ms=lm(b,wt,ep)
 if not ms:print('0000');return
 T=time.time()+tl;bm=ms[0];d=1
 try:
  while 1:
   bs=-M;bm2=ms[0]
   for i,j,c in ms:
    o=CR;CR=C(CR,i,j%200)
    s=-sr(c,not wt,G(b,i,j),d-1,-M,M,1)
    CR=o
    if s>bs:bs=s;bm2=(i,j)
   bm=bm2;d+=1
 except TimeoutError:pass
 print(sq(bm[0])+sq(bm[1]%200)+'nbrq'[bm[1]//200-1:bm[1]//200])
main()
