function pstop=nnstop1(N,lamb,gamma,tspan)
Ntot=N*N;
arrlen=size(tspan);
arrlen=arrlen(1,2);
state=zeros(N,N);
S=0;
I=1;
R=2;
Itot=zeros(1,arrlen);
Rtot=zeros(1,arrlen);
Irandi=randi(N);
Irandj=randi(N);
state(Irandi,Irandj)=I;%Initially one is in the I state
In=0;
stopflag=0;
for t=tspan
    In=In+1;
    if t>3.5 && stopflag==0
       stopflag=1;
       state(Irandi,Irandj)=R;
       Rtot(In)=1;
    else
        if t>3.5 && stopflag==1
            Rtot(In)=Rtot(In-1); 
        end
    end

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
           if xl~=S
               rclap=rclap+1;
           end
           if xr~=S
               rclap=rclap+1;
           end
           if xu~=S
               rclap=rclap+1;
           end
           if xd~=S
               rclap=rclap+1;
           end
           rclap=rclap/4;
           p=rand;
           if p<lamb*rclap && stcp(i,j)==S
               state(i,j)=I;
               Itot(In)=Itot(In)+1;
           end
           if stopflag==1
              rstop=0;
            if xl==R
                rstop=rstop+1;
            end
            if xr==R
               rstop=rstop+1;
            end
            if xu==R
               rstop=rstop+1;
            end
            if xd==R
               rstop=rstop+1;
            end
            rstop=rstop/4; 
            p=rand;
            if p<gamma*rstop && stcp(i,j)==I
               state(i,j)=R;
               Rtot(In)=Rtot(In)+1;
            end
           end
       end
    end
end
pstop=Rtot./Ntot;
end