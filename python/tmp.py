import numpy as np
import matplotlib.pyplot as plt

def generate_dataset():
    mu1 = [4,5]
    si1 = [[1, 2.5],[2.5, 1]]

    mu2 = [6,5];
    si2 = [[0.25, 0],[0, 0.25]]
    
    x1, y1 = np.random.multivariate_normal(np.asarray(mu1), np.asarray(si1), 150).T
    x2, y2 = np.random.multivariate_normal(np.asarray(mu2), np.asarray(si2), 15).T

    write_dataset(x1, y1, x2, y2)

    plt.plot(x1, y1, 'bo', x2, y2, 'rs')
    plt.axis([0, 10, 0, 10])
    plt.title('Original Dataset')
    plt.savefig('tmp.png')
    plt.clf()



def write_dataset(x1, y1, x2, y2):
    f = open('OUTPUT.txt', 'w')
    m = np.asmatrix([np.asarray(x1), np.asarray(y1)]).T
    for t in np.asarray(m):
        f.write(', '.join(str(i) for i in t) + ', negative\n')

    m = np.asmatrix([np.asarray(x2), np.asarray(y2)]).T
    for t in np.asarray(m):
        f.write(', '.join(str(i) for i in t) + ', positive\n')

    f.close()

generate_dataset()

