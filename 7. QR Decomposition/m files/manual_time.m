# Pranit Zope
# AE20B046 
# AS2101 Task 07

#Manual Time plot code

N=[];
t1=[];
t2=[];
t3=[];
for n=1:45
  N=[N,n];
  a=randommatrix(n);
  b=rand(n,1);
  tic
  [Q1,R1]=manual(a);
  time_temp1=toc;
  t1=[t1,time_temp1];
  backsub(a,b,Q1,R1);
  time_temp2=toc;
  t2=[t2,time_temp2-time_temp1];
  time_temp3=toc;
  t3=[t3,time_temp3];
endfor
plot(N,t1,".-",'LineWidth',1.5);
hold on;
plot(N,t2,".-",'LineWidth',1.5);
plot(N,t3,".-",'LineWidth',1.5);
grid on;
axis([0 45 0 1.5])
xlabel("N","fontsize",14);
ylabel("Time(sec)","fontsize",14);
legend('Generation of QR','Back Substitution','Total');
hold off;