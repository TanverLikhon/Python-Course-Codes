#include <iostream>
using namespace std;

class node
{
public:
    int data;
    node *next;

};

int main()
{
    node *avail, *tmp, *save;

avail= new node [20];
if(avail==NULL){cout<<"Over Flow"<<endl; exit(0);}
tmp=avail;
for(int i=0;i<20;i++)
{
    cout<<"\nEnter data: "<<endl;
     tmp= new node;
        cin>>tmp->data;
        tmp->next=NULL;
save=tmp;
        if(i==1)
            avail=tmp;
        else
        {
            save->next=tmp;
        }



}
    while(tmp!=NULL)
    {
        cout<<tmp->data<<endl;
        tmp=tmp->next;
    }


    return 0;
}


