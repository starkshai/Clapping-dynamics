clear all;
close all;
clc;
format long;
N=[5,10,20,50,80,100];
tspan=0:0.1:30;
arrlen=size(tspan);
arrlen=arrlen(1,2);
lamb=[0.1,0.2,0.3,0.5,0.8,1.0];
gamma=[0.1,0.2,0.3,0.5,0.8,1.0];
figure();
for g=gamma
    pstop=zeros(1,arrlen);
    for i=1:10
        pstop=pstop+nnstop1(20,0.3,g,tspan);
    end
    pstop=pstop./10;
    plot(tspan,pstop,'LineWidth',3);
    hold on
end
xlabel('Time (s)');
ylabel('Proportion of individuals');
legend('\gamma =0.1','\gamma =0.2','\gamma =0.3','\gamma =0.5','\gamma =0.8','\gamma =1.0');
saveas(1,'nnstopg.png');
figure();
for l=lamb
    pstop=zeros(1,arrlen);
    for i=1:10
        pstop=pstop+nnstop1(20,l,0.3,tspan);
    end
    pstop=pstop./10;
    plot(tspan,pstop,'LineWidth',3);
    hold on
end
xlabel('Time (s)');
ylabel('Proportion of individuals');
legend('\lambda =0.1','\lambda =0.2','\lambda =0.3','\lambda =0.5','\lambda =0.8','\lambda =1.0');
saveas(2,'nnstopl.png');
figure();
for n=N
    pstop=zeros(1,arrlen);
    for i=1:10
        pstop=pstop+nnstop1(n,0.3,0.3,tspan);
    end
    pstop=pstop./10;
    plot(tspan,pstop,'LineWidth',3);
    hold on
end
xlabel('Time (s)');
ylabel('Proportion of individuals');
legend('N=5','N=10','N=20','N=50','N=80','N=100');
saveas(3,'nnstopN.png');