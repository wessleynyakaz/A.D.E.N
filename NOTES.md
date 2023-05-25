# Important Notes

## How to Link

>```make
>g++ -c ai.cpp
>ar rvs ai.a ai.o
>g++ -c client.cpp
>g++ -o program client.o ai.a -lm
