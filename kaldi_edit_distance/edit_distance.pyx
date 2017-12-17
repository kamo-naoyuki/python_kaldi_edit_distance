# distutils: language=c++

cimport cython
from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.pair cimport pair


ctypedef int int32
cdef extern from "utils/edit-distance-inl.h" namespace "kaldi":
    int32 LevenshteinEditDistance[T](const vector[T] &a,
                                     const vector[T] &b)
    int32 LevenshteinEditDistance[T](const vector[T] &ref,
                                     const vector[T] &hyp,
                                     int32 *ins, int32 *_del, int32 *sub)
    int32 LevenshteinAlignment[T](const vector[T] &a,
                                  const vector[T] &b,
                                  T eps_symbol,
                                  vector[pair[T, T] ] *output)


def levenshtein_edit_distance_int(seq1, seq2):
    cdef vector[int] vseq1 = seq1
    cdef vector[int] vseq2 = seq2
    return LevenshteinEditDistance[int](vseq1, vseq2)


def levenshtein_edit_distance_float(seq1, seq2):
    cdef vector[float] vseq1 = seq1
    cdef vector[float] vseq2 = seq2
    return LevenshteinEditDistance[float](vseq1, vseq2)


def levenshtein_edit_distance_bytes(seq1, seq2):
    cdef vector[string] vseq1 = seq1
    cdef vector[string] vseq2 = seq2
    return LevenshteinEditDistance[string](vseq1, vseq2)


def levenshtein_edit_distance_detail_int(seq1, seq2):
    cdef vector[int] vseq1 = seq1
    cdef vector[int] vseq2 = seq2
    cdef int* ins = [-1]
    cdef int* _del = [-1]
    cdef int* sub = [-1]
    total = LevenshteinEditDistance[int](vseq1, vseq2, ins, _del, sub)
    return total, ins[0], _del[0], sub[0],


def levenshtein_edit_distance_detail_float(seq1, seq2):
    cdef vector[float] vseq1 = seq1
    cdef vector[float] vseq2 = seq2
    cdef int* ins = [-1]
    cdef int* _del = [-1]
    cdef int* sub = [-1]
    total = LevenshteinEditDistance[float](vseq1, vseq2, ins, _del, sub)
    return total, ins[0], _del[0], sub[0],


def levenshtein_edit_distance_detail_bytes(seq1, seq2):
    cdef vector[string] vseq1 = seq1
    cdef vector[string] vseq2 = seq2
    cdef int* ins = [-1]
    cdef int* _del = [-1]
    cdef int* sub = [-1]
    total = LevenshteinEditDistance[string](vseq1, vseq2, ins, _del, sub)
    return total, ins[0], _del[0], sub[0],


def levenshtein_alignment_int(seq1, seq2, eps_symbol):
    cdef vector[int] vseq1 = seq1
    cdef vector[int] vseq2 = seq2
    cdef int _eps_symbol = eps_symbol
    cdef vector[pair[int, int]] output = [(-1, -1)]
    total = LevenshteinAlignment[int](vseq1, vseq2, _eps_symbol, &output)
    return total, output


def levenshtein_alignment_float(seq1, seq2, eps_symbol):
    cdef vector[float] vseq1 = seq1
    cdef vector[float] vseq2 = seq2
    cdef float _eps_symbol = eps_symbol
    cdef vector[pair[float , float]] output = [(-1., -1.)]
    total = LevenshteinAlignment[float](vseq1, vseq2, _eps_symbol, &output)
    return total, output


def levenshtein_alignment_bytes(seq1, seq2, eps_symbol):
    cdef vector[string] vseq1 = seq1
    cdef vector[string] vseq2 = seq2
    cdef string _eps_symbol = eps_symbol
    cdef vector[pair[string, string]] output = [(b'', b'')]
    total = LevenshteinAlignment[string](vseq1, vseq2, _eps_symbol, &output)
    return total, output
