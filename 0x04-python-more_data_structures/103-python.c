#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - display bytes info
 *
 * @p: Python Object
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	char *new_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &new_str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", new_str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", new_str[i]);
	printf("\n");
}

/**
 * print_python_list - display list info
 *
 * @p: Python Object
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	 long int size = PyList_Size(p);
        int i;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", list->allocated);
        for (i = 0; i < size; i++)
        {
                type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[i]);
        }
}
