# Pranit Zope
# AE20B046 
# AS2101 Task 07

# Plot code for N vs Time

N=[];
t1=[];
t2=[];
t3=[];
t4=[];
for n=1:45
  N=[N,n];
  a=randommatrix(n);
  b=rand(n,1);
  tic
  [Q1,R1]=manual(a);
  backsub(a,b,Q1,R1);
  time_temp=toc;
  t1=[t1,time_temp];
  tic
  [Q2,R2]=qr(a);
  backsub(a,b,Q2,R2);
  time_temp=toc;
  t2=[t2,time_temp];
  tic
  X=inverse(a)*b;
  time_temp=toc;
  t3=[t3,time_temp];
  tic
  X=a\b;
  time_temp=toc;
  t4=[t4,time_temp];
endfor
plot(N,t1,".-",'LineWidth',1.5);
hold on;
plot(N,t2,".-",'LineWidth',1.5);
plot(N,t3,".-",'LineWidth',1.5);
plot(N,t4,".-",'LineWidth',1.5);
grid on;
axis([1 45 0 1.5]);
xlabel("N","fontsize",14);
ylabel("Time(sec)","fontsize",14);
legend('QR Manual','QR octave function','Inverse Method','A\B');
hold off;