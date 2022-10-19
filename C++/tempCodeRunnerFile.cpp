vector <int>code;
int N = 1;

void print_code(int pos)
{
    if(pos == N)
    {
        cout<<code;
        
    }
    code[pos] = 0;
    print_code(pos+1);
    code[pos] = 1;
    print_code(pos+1);
}

int main()
{
	print_code(0);
    
    return 0;
}