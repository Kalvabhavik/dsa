#include <iostream>
#include <string>
using namespace std;
struct Node{
    int data;
    Node* left=nullptr;
    Node* right=nullptr;
};
struct Nodes{
    int data;
    Nodes *next;
};
class Queue{
    public:
        Nodes*head=nullptr;
    void enque(int val){
        if(head==nullptr){
            head=new Nodes();
            head->data=val;
        }
        else{
            Nodes* temp;
            temp=head;
            while(temp!=NULL){
                
            }
            
            
        }
    }
        
    
};
class Tree{
    public:
        Node* root;
    Tree(){
        root=nullptr;
    }
    void insert(int key){
        if(root==nullptr){
            
        }
        
        
        

    }
};

int main(){
    
    cout<<"Jelkrri";
    
    return 0;
}