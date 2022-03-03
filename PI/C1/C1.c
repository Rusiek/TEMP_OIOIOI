// Szymon Rusiecki
#include <stdio.h>
#include <math.h>
#define N 100

void 	range				(double *v, double start, double step, 	int n);
void 	linspace			(double *v, double start, double stop, 	int n);
void 	multiply_by_scalar	(double *v, double scalar, 				int n);
void	add					(double *v1, const double *v2, 			int n);
double 	dot_product			(const double *v1, const double *v2, 	int n);

void 	read_vector			(double *v, 		int n);
void 	print_vector		(const double *v, 	int n);

int main(void) {

	int to_do, n;
	double start, stop, step, scalar;
	double vector_1[N], vector_2[N];

	scanf("%d", &to_do);

	switch (to_do) {
		case 1: // linspace
			scanf("%d %lf %lf", &n, &start, &stop);
			linspace(vector_1, start, stop, n);
			print_vector(vector_1, n);
			break;
		case 2: // add
			scanf("%d", &n);
			read_vector(vector_1, n);
			read_vector(vector_2, n);
			add(vector_1, vector_2, n);
			print_vector(vector_1, n);
			break;
		case 3: // dot product
			scanf("%d", &n);
			read_vector(vector_1, n);
			read_vector(vector_2, n);
			printf("%.2f\n", dot_product(vector_1, vector_2, n));
			break;
		case 4: // multiply by scalar
			scanf("%d %lf", &n, &scalar);
			read_vector(vector_1, n);
			multiply_by_scalar(vector_1, scalar, n);
			print_vector(vector_1, n);
			break;
		case 5: // range
			scanf("%d %lf %lf", &n, &start, &step);
			range(vector_1, start, step, n);
			print_vector(vector_1, n);
			break;
		default:
			printf("Unknown operation %d", to_do);
			break;
	}
	return 0;
}

void range(double *v, double start, double step, int n) {
	v[0] = start;
	for (int i = 1; i < n; ++i)
		v[i] += v[i - 1] + step;
}

void linspace(double *v, double start, double stop, int n) {
	if (n == 0) return;
	
	v[0] = start;
	if (n == 1) return;

	double diff = (stop - start) / (n - 1);
	for (int i = 1; i < n; ++i)
		v[i] = v[i - 1] + diff;
	return;
}

void multiply_by_scalar(double *v, double scalar, int n) {
	for (int i = 0; i < n; ++i)
		v[i] *= scalar;
	return;
}

void add(double *v1, const double *v2, int n) {
	for (int i = 0; i < n; ++i)
		v1[i] += v2[i];
	return;
}

double dot_product(const double *v1, const double *v2, int n) {
	double output = 0;
	for (int i = 0; i < n; ++i)
		output += v1[i] * v2[i];
	return output;
}

void read_vector(double *v, int n) {
	for (int i = 0; i < n; ++i)
		scanf("%lf", &v[i]);
	return;
}

void print_vector(const double *v, int n) {
	for (int i = 0; i < n; ++i)
		printf("%.2f ", v[i]);
	printf("\n");
	return;
}
