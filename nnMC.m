clear all;
close all;
clc;
format long;
N=5;
Ntot=N*N;
tspan=0:0.1:10;
arrlen=size(tspan);
arrlen=arrlen(1,2);
state=zeros(5,5);
S=0;
I=1;
R=2;
lamb=0.2;
Itot=zeros(1,arrlen);
Rtot=zeros(1,arrlen);
Irandi=randi(N);
Irandj=randi(N);
state(Irandi,Irandj)=I;%Initially one is in the I state
In=0;
for t=tspan
    In=In+1;
    if In==1
      Itot(In)=1;
    else
      Itot(In)=Itot(In-1);
    end
    stcp=state;
    for i=1:N
       for j=1:N
           if j==1
              xl=stcp(i,N);
           else
              xl=stcp(i,j-1);
           end
           if j==N
              xr=stcp(i,1);
           else
              xr=stcp(i,j+1);
           end
           if i==1
              xu=stcp(N,j);
           else
              xu=stcp(i-1,j);
           end
           if i==N
              xd=stcp(1,j);
           else
              xd=stcp(i+1,j);
           end
           rclap=0;
           if xl>0
               rclap=rclap+1;
           end
           if xr>0
               rclap=rclap+1;
           end
           if xu>0
               rclap=rclap+1;
           end
           if xd>0
               rclap=rclap+1;
           end
           rclap=rclap/4;
           p=rand;
           if p<lamb*rclap && stcp(i,j)==0
               state(i,j)=1;
               Itot(In)=Itot(In)+1;
           end
       end
    end
end
plot(tspan,Itot./N/N);