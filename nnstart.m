clear all;
close all;
clc;
format long;
N=[5,10,20,50,80,100];
tspan=0:0.1:50;
arrlen=size(tspan);
arrlen=arrlen(1,2);
lamb=[0.1,0.2,0.3,0.5,0.8,1.0];
figure();
for n=N
    pstart=zeros(1,arrlen);
    for i=1:10
        pstart=pstart+nnstart1(n,0.2,tspan);
    end
    pstart=pstart./10;
    plot(tspan,pstart,'LineWidth',3);
    hold on
end
xlabel('Time (s)');
ylabel('Proportion of individuals');
legend('N=5','N=10','N=20','N=50','N=80','N=100');
saveas(1,'nnstartN.png');
figure();
tspan=0:0.1:40;
for l=lamb
    pstart=zeros(1,arrlen);
    for i=1:10
        pstart=nnstart1(20,l,tspan);
    end
    pstart=pstart./10;
    plot(tspan,pstart,'LineWidth',3);
    hold on
end
xlabel('Time (s)');
ylabel('Proportion of individuals');
legend('\lambda =0.1','\lambda =0.2','\lambda =0.3','\lambda =0.5','\lambda =0.8','\lambda =1.0');
saveas(2,'nnstartlamb.png');