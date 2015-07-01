from pylab import *

seed(123)
rc("font", size=16, family="serif", serif="Computer Sans")
rc("text", usetex=True)

x = 1 + arange(0, 10)

# Make a prior
q = exp(0.5*randn(x.size))
q /= q.sum()

# Probability of x \in {3, 4, 5} according to distribution q
#print(sum(q[logical_and(x >= 3, x <= 5)]))

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

figure(figsize=(8, 10))
subplot(2,1,1)
bar(x-0.5*0.35, q, width=0.35, alpha=0.3)
xlim([0.5, 10.5])
ylim([0., 1.05*max(hstack([q, p]))])
gca().set_xticks(x)
ylabel("Probability, $q(x)$")
subplot(2,1,2)
bar(x-0.5*0.35, p, width=0.35, alpha=0.3)
xlabel("$x$", fontsize=20)
ylabel("Probability, $p(x)$")
xlim([0.5, 10.5])
ylim([0., 1.05*max(hstack([q, p]))])
gca().set_xticks(x)
savefig("distribution2.pdf", bbox_inches="tight")
show()

# Another posterior
lamb = 0.5163846 # The lagrange multiplier
p = q.copy()
p *= exp(-lamb*(x - 5.)**2)
p /= p.sum()
e = (p*(x - 5.)**2).sum()
# print(e)

figure(figsize=(8, 10))
subplot(2,1,1)
bar(x-0.5*0.35, q, width=0.35, alpha=0.3)
xlim([0.5, 10.5])
ylim([0., 1.05*max(hstack([q, p]))])
gca().set_xticks(x)
ylabel("Probability, $q(x)$")
subplot(2,1,2)
bar(x-0.5*0.35, p, width=0.35, alpha=0.3)
xlabel("$x$", fontsize=20)
ylabel("Probability, $p(x)$")
xlim([0.5, 10.5])
ylim([0., 1.05*max(hstack([q, p]))])
gca().set_xticks(x)
savefig("distribution3.pdf", bbox_inches="tight")
show()

