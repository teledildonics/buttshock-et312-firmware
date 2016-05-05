
int (*buttshock_main)(int argc, char* argv[]) = (int(*)(int argc, char* argv[])) 0x0054;

__attribute((used))
__attribute((naked))
int main(int argc, char* argv[]){
    buttshock_main(argc, argv);
    return 0;
}
