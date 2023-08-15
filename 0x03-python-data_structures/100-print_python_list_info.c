#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int size;

	size = (((PyVarObject*)(p))->ob_size);
	printf("[*] Size of the Python List = %d", size)
}

