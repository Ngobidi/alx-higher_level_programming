#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - provides data for the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double value = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_str(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
/**
 * print_python_bytes - provide data for the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, j = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying str: %s\n", str);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (j < size + 1 && j < 10)
	{
		printf(" %02hhx", str[j]);
		j++;
	}
	printf("\n");
}
/**
 * print_python_list - provides data for the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *ref;
	int j = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < size)
		{
			ref = PyList_GET_REF(p, j);
			printf("Element %d: %s\n", J, ref->ob_type->tp_name);
			if (PyBytes_Check(ref))
				print_python_bytes(ref);
			else if (PyFloat_Check(ref))
				print_python_float(ref);
			j++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
