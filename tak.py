##biblioteka do rysowania wykresów##
## import  nazwa biblioteki  as alias
import matplotlib.pyplot as plt
##odwołując się do biblioteki piszemy plt.funkcja


##czytanie danych##
##zadeklarowanie tablic##
x = []
y = []
c = []

##otwarcie pliku
##plik = open(sciezka* + nazwa_pliku)
f = open('train')

##iterowanie po liniach
for line in f:
    ##dzielimy według spacji i zapisujemy w odpowiednich tablicach
    ##pamiętamy o tym, że w pliku są zapisane litery, a my potrzebujemy liczby
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))
    c.append(float(line.split()[2]))

print(x)
print(y)

##ustawienie pola widzenia na diagramie
##plt.axis([-10, 10, -10, 10])
##stworzenie diagramu wszystkich punktów
##plt.plot(xy, ygreki, kształt, color = kolor)
##for i in range(len(c)):
  ##  if c[i] == 1.0:
    ##    plt.plot(x[i], y[i], 'ro', color='red')
  ##  elif c[i] == 0:
    ##    plt.plot(x[i], y[i], 'ro', color='blue')
  ##  else:
    ##    plt.plot(x[i], y[i], 'ro', color='green')

##plt.plot(x, y, 'ro', color='red')

def load_data(filename):
    X = []
    for line in open(filename):
        tokens = line.split()
        X.append([float(tokens[0]),float(tokens[1]),float(tokens[2])])
    return(X)

# def classify(X):
#     Xs = []
#     ys = []
#     for [x,y,c] in X:
#         if c == 1 or c == 0:
#             Xs.append([x,y])
#             ys.append(c)
#     clf = svm.SVC()
#     clf.fit(Xs,ys)
#     for i in range(len(X)):
#         if X[i][2] == -1:
#             X[i][2] = clf.predict([X[i][0],X[i][1]])
#     return (X, clf.support_vectors_)


def draw_data(X):
    xs1 = []
    ys1 = []
    xs0 = []
    ys0 = []
    xsn = []
    ysn = []
    for [x,y,c] in X:
        if c == 1:
            xs1.append(x)
            ys1.append(y)
        if c == 0:
            xs0.append(x)
            ys0.append(y)
        if c == -1:
            xsn.append(x)
            ysn.append(y)
    plt.axis([-5, 15, -5, 15])
    plt.plot(xs0, ys0, 'ro', color='red')
    plt.plot(xs1, ys1, 'ro', color='blue')
    plt.plot(xsn, ysn, 'ro', color='green')

    # wyświetlanie diagramu
    plt.show()



# draw_data(load_data('train'))
# classify(load_data('train'))


