#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info -  print information about pyobject.
 * @p:  pyobject
 *
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *pylist;
	int n;
	int size;

	pylist = (PyListObject *)p;
	size = PyList_Size(pp);
	printf("[*] Size of the Python List = %d", size);
	printf("[*] Allocated = %d", pylist->allocated);
	for (n = 0; n < size; n++)
		printf("Element %d: %s\n", n, PyList_GetItem(pylist, n);
}
