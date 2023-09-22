#ifndef _GNU_SOURCE
#define _GNU_SOURCE
#endif
#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
/**
 * print_python_list -  print information about pyobject.
 * @p:  pyobject
 *
 */
void print_python_list(PyObject *p)
{
	int n;
	PyListObject *pylist;

	pylist = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", pylist->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pylist->allocated);
	for (n = 0; n < pylist->ob_base.ob_size; n++)
	{
		printf("Element %d: %s\n", n, pylist->ob_item[n]->ob_type->tp_name);
		if (PyBytes_Check(pylist->ob_item[n]))
			print_python_bytes(pylist->ob_item[n]);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects.
 * @p: pyobject
 */

void print_python_bytes(PyObject *p)
{
	long int size;
	long int n;
	long int i;
	PyBytesObject *pybyte;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	pybyte = (PyBytesObject *)p;
	size = pybyte->ob_base.ob_size;
	string = pybyte->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	n = size + 1;
	if (n >= 10)
		n = 10;
	printf("  first %ld bytes:", n);
	for (i = 0; i < n; i++)
	{
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);
		printf("\n");
}
