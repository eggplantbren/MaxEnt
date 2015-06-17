from pylab import *

seed(123)
rc("font", size=16, family="serif", serif="Computer Sans")
rc("text", usetex=True)

x = 1 + arange(0, 10)

# Make a prior
p = exp(0.5*randn(x.size))
p /= p.sum()

bar(x-0.5*0.35, p, width=0.35, alpha=0.3)
xlabel("$x$", fontsize=20)
ylabel("Probability")
xlim([0.5, 10.5])
gca().set_xticks(x)
title("A Probability Distribution")
savefig("distribution.pdf", bbox_inches="tight")
show()

