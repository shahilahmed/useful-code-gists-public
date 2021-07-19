#include<stdio.h>
#include<stdlib.h>

typedef struct _type_env{
	int x;
	int (*closure)(struct _type_env *env,int y);
}type_env;

int add(type_env *env,int y) {
	return (env->x + y);
}

int mul(type_env *env,int y) {
	return (env->x * y);
}

type_env * times(int x,int (*closure)(struct _type_env *env,int y)) {
	type_env *env = (type_env *)malloc(sizeof(type_env));
	env->x = x;
	env->closure = closure;
	return env;
}

int main() {
	type_env *t6 = times(6,mul);
	type_env *t9 = times(9,add);
	printf("closure(t6,mul)(4): %d Excepted: 24\n",t6->closure(t6,4));
	printf("closure(t9,add)(4): %d Excepted: 13\n",t9->closure(t9,4));
	printf("\n");
	return 0;
}
