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
	char *new_str;
	long int size, x, limit;

	printf("[.] bytes object infomation\n")
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", new_str);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (x = 0; x < limit; x++)
		if (new_str[x] >= 0)
			printf(" %02x", new_str[x]);
		else
			printf(" %02x", 256 + new_str[x]);

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
