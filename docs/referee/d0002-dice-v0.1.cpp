#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
using U=unsigned; const U ALL=(1u<<18)-1;
int wins(U a,U b){int w=0;while(a){U bit=a&-a;w+=__builtin_popcount(b&(bit-1));a^=bit;}return w;}
int sum(U a){int s=0;while(a){U bit=a&-a;s+=__builtin_ctz(bit)+1;a^=bit;}return s;}
void print(U m){for(int i=0;i<18;i++)if(m>>i&1)std::cout<<i+1<<' ';}
struct Result{long long cyc=0,count=0;int best=0;U a=0,b=0,c=0;void add(U A,U B,U C,int x,int y,int z){if(std::min({x,y,z})<=18)return;++cyc;int q=std::min({x,y,z});if(q>best){best=q;count=0;a=A;b=B;c=C;}if(q==best)++count;}};
int main(){Result equal,all;long long total=0,eq=0;for(U a=1;a<=ALL;a+=2){if(__builtin_popcount(a)!=6)continue;U rest=ALL^a,first=rest&-rest;for(U b=rest;b;b=(b-1)&rest){if(!(b&first)||__builtin_popcount(b)!=6)continue;U c=rest^b;++total;bool same=sum(a)==57&&sum(b)==57;eq+=same;int x=wins(a,b),y=wins(b,c),z=wins(c,a);if(x<18&&y<18&&z<18){std::swap(b,c); /* do not mutate loop variable: undo below */ all.add(a,b,c,36-z,36-y,36-x);if(same)equal.add(a,b,c,36-z,36-y,36-x);std::swap(b,c);}else{all.add(a,b,c,x,y,z);if(same)equal.add(a,b,c,x,y,z);}}}std::cout<<"partitions "<<total<<" equal "<<eq<<'\n';for(auto r:{equal,all}){std::cout<<"cyclic "<<r.cyc<<" optimum "<<r.best<<" count "<<r.count<<" wins "<<wins(r.a,r.b)<<' '<<wins(r.b,r.c)<<' '<<wins(r.c,r.a)<<" sums "<<sum(r.a)<<' '<<sum(r.b)<<' '<<sum(r.c)<<'\n';print(r.a);std::cout<<'\n';print(r.b);std::cout<<'\n';print(r.c);std::cout<<'\n';}}
