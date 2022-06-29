# Pranit Zope
# AE20B046
# AS2101 Task 06


x=linspace(-1,1,100);
y0=ones(1,100);
y1=p1(x);
y2=p2(x);
y3=p3(x);
y4=p4(x);
y5=p5(x);

plot(x, y0,'-','linewidth',1.2);
hold on
plot(x, y1,'-','linewidth',1.2);
plot(x, y2,'-','linewidth',1.2);
plot(x, y3,'-','linewidth',1.2);
plot(x, y4,'-','linewidth',1.2);
plot(x, y5,'-','linewidth',1.2);
grid on
axis([-1 1 -1 1]);
hold off;

set (gca,"fontsize",10);
xlabel('x');
ylabel('pn(x)');
legend("n=0","n=1","n=2","n=3","n=4","n=5",'location','southeast');