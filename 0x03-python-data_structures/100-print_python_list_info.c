#include <python3.4/python.h>

/**
 * print_python_list_info -  print information about pyobject.
 * @p:  pyobject
 *
 */
void print_python_list_info(PyObject *p)
{
	int n;
	int size;

	size = (PyVarObject *)p->ob_size;
	printf("[*] Size of the Python List = %d", size);
	printf("[*] Allocated = %d", (PyVarObject *)p->allocated);
	for (n = 0; n < size; n++)
		printf("Element %d: %s\n", n, (PyVarObject *)p->ob_item[n]->ob_type);
}
