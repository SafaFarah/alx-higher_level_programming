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
	long int size;

	pylist = (PyListObject *)p;
	size = pylist->ob_base.ob_size;
	printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", pylist->allocated);
    for (i = 0; i < size; i++)
    {
        printf("Element %d: %s\n", i, pylist->ob_item[i]->ob_type->tp_name);
    }
}
