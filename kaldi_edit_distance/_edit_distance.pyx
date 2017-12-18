# distutils: language=c++

cimport cython
from libcpp.vector cimport vector
from libcpp.string cimport string
from libcpp.pair cimport pair


cdef extern from "edit-distance-inl.h" namespace "kaldi":
    int LevenshteinEditDistance[T](const vector[T] &a,
                                   const vector[T] &b)
    int LevenshteinEditDistance[T](const vector[T] &ref,
                                     const vector[T] &hyp,
                                     int *ins, int *_del, int *sub)
    int LevenshteinAlignment[T](const vector[T] &a,
                                const vector[T] &b,
                                T eps_symbol,
                                vector[pair[T, T] ] *output)


def levenshtein_edit_distance_long(seq1, seq2):
    cdef vector[long] vseq1 = seq1
    cdef vector[long] vseq2 = seq2
    return LevenshteinEditDistance[long](vseq1, vseq2)


def levenshtein_edit_distance_double(seq1, seq2):
    cdef vector[double] vseq1 = seq1
    cdef vector[double] vseq2 = seq2
    return LevenshteinEditDistance[double](vseq1, vseq2)


def levenshtein_edit_distance_bytes(seq1, seq2):
    cdef vector[string] vseq1 = seq1
    cdef vector[string] vseq2 = seq2
    return LevenshteinEditDistance[string](vseq1, vseq2)


def levenshtein_edit_distance_detail_long(seq1, seq2):
    cdef vector[long] vseq1 = seq1
    cdef vector[long] vseq2 = seq2
    cdef int* ins = [-1]
    cdef int* _del = [-1]
    cdef int* sub = [-1]
    total = LevenshteinEditDistance[long](vseq1, vseq2, ins, _del, sub)
    return total, ins[0], _del[0], sub[0],


def levenshtein_edit_distance_detail_double(seq1, seq2):
    cdef vector[double] vseq1 = seq1
    cdef vector[double] vseq2 = seq2
    cdef int* ins = [-1]
    cdef int* _del = [-1]
    cdef int* sub = [-1]
    total = LevenshteinEditDistance[double](vseq1, vseq2, ins, _del, sub)
    return total, ins[0], _del[0], sub[0],


def levenshtein_edit_distance_detail_bytes(seq1, seq2):
    cdef vector[string] vseq1 = seq1
    cdef vector[string] vseq2 = seq2
    cdef int* ins = [-1]
    cdef int* _del = [-1]
    cdef int* sub = [-1]
    total = LevenshteinEditDistance[string](vseq1, vseq2, ins, _del, sub)
    return total, ins[0], _del[0], sub[0],


def levenshtein_alignment_long(seq1, seq2, eps_symbol):
    cdef vector[long] vseq1 = seq1
    cdef vector[long] vseq2 = seq2
    cdef long _eps_symbol = eps_symbol
    cdef vector[pair[long, long]] output = [(-1, -1)]
    total = LevenshteinAlignment[long](vseq1, vseq2, _eps_symbol, &output)
    return total, output


def levenshtein_alignment_double(seq1, seq2, eps_symbol):
    cdef vector[double] vseq1 = seq1
    cdef vector[double] vseq2 = seq2
    cdef double _eps_symbol = eps_symbol
    cdef vector[pair[double , double]] output = [(-1., -1.)]
    total = LevenshteinAlignment[double](vseq1, vseq2, _eps_symbol, &output)
    return total, output


def levenshtein_alignment_bytes(seq1, seq2, eps_symbol):
    cdef vector[string] vseq1 = seq1
    cdef vector[string] vseq2 = seq2
    cdef string _eps_symbol = eps_symbol
    cdef vector[pair[string, string]] output = [(b'', b'')]
    total = LevenshteinAlignment[string](vseq1, vseq2, _eps_symbol, &output)
    rseq1 = [v1 for v1, v2 in output]
    rseq2 = [v2 for v1, v2 in output]
    return total, output
