clear all;
close all;
clc;
format long;
N=70;
mu=3;
sigma=0.5;
Karr=0:0.01:2;
qarrsize=size(Karr);
qarrsize=qarrsize(1,1);
qarr=zeros(qarrsize,1);
tspan=[0 50];
kn=0;
for K=Karr
   kn=kn+1;
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
   qarr(kn,1)=mean(q(round(sizeq*0.5):sizeq,1));
end
plot(Karr,qarr,'ro');
xlabel('K');
ylabel('q');
saveas(1,'syn2.png');

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