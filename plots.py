from pylab import *

seed(123)
rc("font", size=16, family="serif", serif="Computer Sans")
rc("text", usetex=True)

x = 1 + arange(0, 10)

# Make a prior
q = exp(0.5*randn(x.size))
q /= q.sum()

# Probability of x \in {3, 4, 5} according to distribution q
print(sum(q[logical_and(x >= 3, x <= 5)]))

bar(x-0.5*0.35, q, width=0.35, alpha=0.3)
xlabel("$x$", fontsize=20)
ylabel("Probability, $q(x)$")
xlim([0.5, 10.5])
gca().set_xticks(x)
title("Prior Distribution")
savefig("distribution.pdf", bbox_inches="tight")
show()


# Make a posterior
p = q.copy()
p[logical_or(x < 3, x > 5)] = 0.
p /= p.sum()

bar(x-0.5*0.35, p, width=0.35, alpha=0.3)
xlabel("$x$", fontsize=20)
ylabel("Probability, $p(x)$")
xlim([0.5, 10.5])
gca().set_xticks(x)
title("Posterior Distribution")
savefig("distribution2.pdf", bbox_inches="tight")
show()

