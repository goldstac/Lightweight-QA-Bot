#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "csearch.h"

static PyObject* csearch_search(PyObject* self, PyObject* args) {
    PyObject *query_obj, *vectors_obj;

    if (!PyArg_ParseTuple(args, "OO", &query_obj, &vectors_obj))
        return NULL;

    if (!PyList_Check(query_obj)) {
        PyErr_SetString(PyExc_TypeError, "query must be a list");
        return NULL;
    }
    if (!PyList_Check(vectors_obj)) {
        PyErr_SetString(PyExc_TypeError, "vectors must be a list");
        return NULL;
    }

    Py_ssize_t qlen = PyList_Size(query_obj);
    std::vector<double> query(static_cast<std::size_t>(qlen));
    for (Py_ssize_t i = 0; i < qlen; ++i) {
        PyObject* item = PyList_GetItem(query_obj, i);
        if (!item) return NULL;
        query[static_cast<std::size_t>(i)] = PyFloat_AsDouble(item);
        if (PyErr_Occurred()) return NULL;
    }

    Py_ssize_t vlen = PyList_Size(vectors_obj);
    std::vector<std::vector<double>> vectors(static_cast<std::size_t>(vlen));
    for (Py_ssize_t i = 0; i < vlen; ++i) {
        PyObject* vec = PyList_GetItem(vectors_obj, i);
        if (!vec) return NULL;
        if (!PyList_Check(vec)) {
            PyErr_SetString(PyExc_TypeError, "each vector must be a list");
            return NULL;
        }
        Py_ssize_t dim = PyList_Size(vec);
        vectors[static_cast<std::size_t>(i)].resize(static_cast<std::size_t>(dim));
        for (Py_ssize_t j = 0; j < dim; ++j) {
            PyObject* item = PyList_GetItem(vec, j);
            if (!item) return NULL;
            vectors[static_cast<std::size_t>(i)][static_cast<std::size_t>(j)] = PyFloat_AsDouble(item);
            if (PyErr_Occurred()) return NULL;
        }
    }

    SearchResult result = cosine_search(query, vectors);
    return Py_BuildValue("(id)", result.index, result.score);
}

static PyMethodDef CSearchMethods[] = {
    {"search", csearch_search, METH_VARARGS, "Fast cosine similarity search"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef csearchmodule = {
    PyModuleDef_HEAD_INIT,
    "csearch",
    "Fast cosine similarity search in C++",
    -1,
    CSearchMethods
};

PyMODINIT_FUNC PyInit_csearch(void) {
    return PyModule_Create(&csearchmodule);
}
