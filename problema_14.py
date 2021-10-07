matrice=[[1,2],[2,3],[7,3],[9,1],[4,6],[0,8],[5,1],[4,3],[9,7]]
n=int(input("dimensiunea matricei de la 2 pana la 10: "))
if n>=2 and n>=10:
    for i in range(0,n):
        x=int(input("elementele sunt: "))
        for j in range(0,n):
            matrice.append(x[i][j])
print(matrice)
dp=[]    #dp-diagonala principala
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i==j:
            dp.append(matrice[i][j])
print("suma diagonalei principale este=",sum(dp))
ds=[]    #ds-diagonala secundara
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i+j==n-1:
            ds.append(matrice[i][j])
print("suma diagonalei secundare este=",sum(ds))
msddp=[] #msddp-mai sus de diagonala principala
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i-j<0:
            msddp.append(matrice[i][j])
print("suma diagonalei mai sus de diagonala principala este=",sum(msddp))
mjddp=[] #mjddp-mai jos de diagonala principala
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i-j>0:
            mjddp.append(matrice[i][j])
print("suma diagonalelor mai jos de diagonala principala este=",sum(mjddp))
msdds=[] #msdds-mai sus de diagonala secundara
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i+j<n-1:
            msdds.append(matrice[i][j])
print("suma diagonalelor mai sus de diagonala secundara este=",sum(msdds))
mjdds=[] #mjdds-mai jos de diagonala secundara
for i in range(len(matrice)):
    for j in range(len(matrice[0])):
        if i+j>n-1:
            mjdds.append(matrice[i][j])
print("suma diagonalelor mai jos de diagonala secundara este=",sum(mjdds))