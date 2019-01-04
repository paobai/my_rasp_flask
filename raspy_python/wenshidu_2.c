#include<stdio.h> 
#include<wiringPi.h> 
#include<sys/time.h> 
#include<pthread.h> 
#include<unistd.h>
int data[5]={0,0,0,0,0}; 
int read_date() {
	data[0]=data[1]=data[2]=data[3]=data[4]=0;
	int i=0;
	int times=0;
	int j=0;
	int last=HIGH;
	float shidu,wendu;
	pinMode(4,OUTPUT);
	digitalWrite(4,LOW);
	delay(18);
	digitalWrite(4,HIGH);
	delayMicroseconds(40);
	pinMode(4,INPUT);
	for(i=0;i<85;i++)
	{
		times=0;
		while(digitalRead(4)==last)
		{
			/*state=digitalRead(29);
			if(state==1)
				times++;
			else
				break;
			if(times>=255)
				break;
			delayMicroseconds(1);*/
			times++;
			delayMicroseconds(1);
			if(times>=255)
				break;
		}
		if(times>=255)
			break;
		last=digitalRead(4);
		
		if(i>=4&&(i%2==0))
		{
			data[j/8]<<=1;
			if(times>30)
				data[j/8]|=1;
			j++;
		}
		//printf("%d---------\n",times);
	}
	//printf("%d---------\n",times);
	shidu=(data[0]*100+data[1])/100;
	wendu=(data[2]*100+data[3])/100;
	//printf("j=%d,shidu=%d.%d,wendu=%d.%d...%d.\n",j,data[0],data[1],data[2],data[3],data[4]);
	if(data[0]+data[1]+data[2]+data[3]==data[4] && shidu>1)
		{//printf("j=%d,shidu=%.2f,wendu=%.2f....\n",j,shidu,wendu);
		return shidu*1000+wendu;}
	else
	{//printf("error !\n");
	return -1;
	}
}
int main() {
	int result=0;
	if(wiringPiSetup()==-1)
		{
			//printf("return -1 error\n");
			return -1;
		}
		else
		{
			//printf("succeed setup!\n");
		}
		while(1)
		{
			result=read_date();
			if (result!=-1)
			{printf("%d",result);
			return result;}
			delay(1000);
		}
		
		return 0;
		
}
