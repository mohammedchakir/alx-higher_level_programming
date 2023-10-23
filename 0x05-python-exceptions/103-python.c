#define PY_SSIZE_T_CLEAN
#include <Python.h>


/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		Py_ssize_t i;
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++)
		{
			PyObject *item = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_GET_SIZE(p);
			Py_ssize_t i;
		char *str = PyBytes_AsString(p);

		printf("[.] bytes object info\n");
		printf("  Size: %ld\n", size);
		printf("  Trying string: %s\n", str);

		printf("  First %ld bytes: ", size > 10 ? 10 : size);
		for (i = 0; i < size && i < 10; i++)
		{
			printf("%02hhx", str[i]);
			if (i + 1 < size && i + 1 < 10)
			{
				printf(" ");
			}
		}
		printf("\n");
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_float - gives data of the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	if (PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		printf("  Type: %s\n", Py_TYPE(p)->tp_name);
		printf("  Value: %lf\n", ((PyFloatObject *)p)->ob_fval);
	}
	else
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
	}
}
