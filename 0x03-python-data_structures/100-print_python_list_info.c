#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - write python list_info
 *
 * @p: PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int size, x;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (x = 0; x < size; x++)
	{
		item = PyList_GetItem(p, x);
		printf("Element %ld: %s\n", x, Py_TYPE(item)->tp_name);
	}
}
