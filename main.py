import matplotlib.pyplot as plot
import numpy

x = numpy.linspace(-5, 100, 1000)
y = numpy.exp(-0.1 * x) * (numpy.sin(x) + numpy.cos(2 * x)) + numpy.log(x + 4)

plot.plot(x, y, label=r"$f(x)=e^{-0.1x}(\sin x+\cos 2x)+\ln(x+4)$")

plot.axhline(0, color="black", linewidth=0.8)
plot.axvline(0, color="black", linewidth=0.8)

plot.xlabel("x")
plot.ylabel("f(x)")
plot.legend()

plot.show()
