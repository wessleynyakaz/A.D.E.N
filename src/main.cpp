#include <iostream>
#define PY_SSIZE_T_CLEAN
#include <Python.h>

std::string Cstr ();

int main(){

    std::cout << " Welcome back " << Cstr();
    return 0;
}

std::string Cstr(){
    return "3";
}