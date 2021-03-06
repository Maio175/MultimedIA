import torch
import torchvision
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
import math



def show_scatterplot(X, colors, title=''):
    colors = colors.cpu().numpy()
    X = X.cpu().numpy()
    plt.figure()
    plt.axis('equal')
    plt.scatter(X[:, 0], X[:, 1], c=colors, s=30)
    plt.title(title)
    plt.axis('off')

def plot_data(X, y, d=0, auto=False, zoom=1):
    X = X.cpu()
    y = y.cpu()
    plt.figure(figsize=(8,8))
    plt.scatter(X.numpy()[:, 0], X.numpy()[:, 1], c=y, s=10, cmap=plt.cm.Spectral)
    plt.axis('square')
    plt.axis(np.array((-1.1, 1.1, -1.1, 1.1)) * zoom)
    if auto is True: plt.axis('equal')
    plt.axis('off')

    _m, _c = 0, '.15'
    plt.axvline(0, ymin=_m, color=_c, lw=1, zorder=0)
    plt.axhline(0, xmin=_m, color=_c, lw=1, zorder=0)


def create_spiral(n_data, n_dim, n_class):
  X = torch.zeros(n_data * n_class, n_dim)
  y = torch.zeros(n_data * n_class, dtype=torch.long)
  for c in range(n_class):
      index = 0
      t = torch.linspace(0, 1, n_data)
      inner_var = torch.linspace(
          (2 * math.pi / n_class) * (c),
          (2 * math.pi / n_class) * (2 + c),
          n_data
      ) + torch.randn(n_data) * 0.2
      
      for ix in range(n_data * c, n_data * (c + 1)):
          X[ix] = t[index] * torch.FloatTensor((
              math.sin(inner_var[index]), math.cos(inner_var[index])
          ))
          y[ix] = c
          index += 1
  return X,y