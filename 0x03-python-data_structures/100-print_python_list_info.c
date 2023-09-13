#ifndef _GNU_SOURCE
#define _GNU_SOURCE
#endif
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info -  print information about pyobject.
 * @p:  pyobject
 *
 */
void print_python_list_info(PyObject *p)
{
	int n;
	PyListObject *pylist;

	pylist = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", pylist->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pylist->allocated);
	for (n = 0; n < pylist->ob_base.ob_size; n++)
	{
		printf("Element %d: %s\n", n, pylist->ob_item[n]->ob_type->tp_name);
	}
}
