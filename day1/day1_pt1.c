#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main( int argc, char *argv[] )
{
    char *p_captcha = argv[1];
    size_t captcha_size = strlen( p_captcha );
    int i, total = 0;
    for ( i=0; i<captcha_size; ++i )
        if ( p_captcha[i] == p_captcha[(i+1)%captcha_size] )
            total += ( int ) p_captcha[i] - 48;
    printf( "%d\n", total );
    return 0;
}