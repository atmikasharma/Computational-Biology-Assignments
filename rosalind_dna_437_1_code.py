#include<iostream>
#include<cstdlib>
#include<string>
#include<algorithm>
#include<conio.h>

using namespace std ;

class NucleoCount{
    private:
        int countA, countC, countG, countT ;
        string strand ;
    public:
        NucleoCount() ;
        void get_strand() ;
        void count_nucleo(string) ;
        void print() ;
};

NucleoCount::NucleoCount(){
    countA=countC=countG=countT=0 ;
    strand='\0' ;
}

void NucleoCount::get_strand(){
    cin>>strand ;
    count_nucleo(strand) ;
}

void NucleoCount::count_nucleo(string){

    countA = std::count(strand.begin(), strand.end(), 'A') ;
    countC = std::count(strand.begin(), strand.end(), 'C') ;
    countG = std::count(strand.begin(), strand.end(), 'G') ;
    countT = std::count(strand.begin(), strand.end(), 'T') ;

}

void NucleoCount::print(){
    cout<<countA<<" "<<countC<<" "<<countG<<" "<<countT ;
}

int main(){
    NucleoCount counting ;
    counting.get_strand() ;
    counting.print() ;
    getch() ;
}