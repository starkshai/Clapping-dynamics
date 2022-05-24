clear all;
close all;
clc;
format long;
N=70;
mu=3;
sigma=0.5;
Karr=0:0.4:2;
tspan=[0 50];
for K=Karr
   phi0=2*pi*rand(1,N);
   w=normrnd(mu,sigma,1,N);
   KN=K/N;
   [t,phi]=ode45(@odefun,tspan,phi0,[],w,KN,N);
   sizeq=size(t);
   sizeq=sizeq(1,1);
   q=zeros(sizeq,1);
   for k=1:sizeq
      tmpq=0;
      for j=1:N
         tmpq=tmpq+exp(1i*phi(k,j));
      end
      q(k,1)=abs(tmpq)/N;
   end
   plot(t,q);
   hold on
end
xlabel('Time (s)');
ylabel('q');
legend('K=0','K=0.4','K=0.8','K=1.2','K=1.6','K=2.0');
saveas(1,'syn1.png');

function dy=odefun(t,y,w,KN,N)
    dy=zeros(N,1);
    for yi=1:N
        sum=0;
        for xi=1:N
           sum=sum+sin(y(xi)-y(yi));
        end
        dy(yi)=w(yi)+KN*sum;
    end
end