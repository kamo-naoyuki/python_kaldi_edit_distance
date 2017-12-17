"""
Copyright 2009-2011  Microsoft Corporation;  Haihua Xu;  Yanmin Qian

See ../../COPYING for clarification regarding multiple authors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

THIS CODE IS PROVIDED *AS IS* BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED
WARRANTIES OR CONDITIONS OF TITLE, FITNESS FOR A PARTICULAR PURPOSE,
MERCHANTABLITY OR NON-INFRINGEMENT.
See the Apache 2 License for the specific language governing permissions and
limitations under the License.
"""
from . import edit_distance as ed


def _get_ele(seq1, seq2):
    seq1 = list(seq1)
    seq2 = list(seq2)

    if len(seq1) == len(seq2) == 0:
        return 0
    first_ele = (seq1 + seq2)[0]
    if any(not isinstance(v, type(first_ele)) for v in (seq1 + seq2)):
        raise ValueError(
            'All types of elements in seq1 and seq2 should be same')
    return first_ele


def levenshtein_edit_distance(seq1, seq2, detail=False):
    """
    (This description comes from kaldi/src/util/edit-distance-inl.h)

    Algorithm:
        write A and B for the sequences, with elements a_0 ..
        let |A| = M and |B| = N be the lengths, and have
        elements a_0 ... a_{M-1} and b_0 ... b_{N-1}.
        We are computing the recursion
           E(m, n) = min(  E(m-1, n-1) + (1-delta(a_{m-1}, b_{n-1})),
                          E(m-1, n),
                          E(m, n-1) ).
        where E(m, n) is defined for m = 0..M and n = 0..N and out-of-
        bounds quantities are considered to be infinity (i.e. the
        recursion does not visit them).

    We do this computation using a vector e of size N+1.
    The outer iterations range over m = 0..M.

    Args:
        seq1 (List[Union[int, float, str]]):
        seq1 (List[Union[int, float, str]]):
        detail (bool):
    Returns:
        if detail:
            total (int)
            insertion (int)
            deletion (int),
            substitution (int)
        else:
            total (int)
    """
    if not isinstance(detail, bool):
        raise TypeError('details arg must have bool type')
    seq1 = tuple(seq1)
    seq2 = tuple(seq2)
    ele = _get_ele(seq1, seq2)

    if isinstance(ele, int):
        if detail:
            return ed.levenshtein_edit_distance_detail_long(seq1, seq2)
        else:
            return ed.levenshtein_edit_distance_long(seq1, seq2)
    elif isinstance(ele, float):
        if detail:
            return ed.levenshtein_edit_distance_detail_double(seq1, seq2)
        else:
            return ed.levenshtein_edit_distance_double(seq1, seq2)
    elif isinstance(ele, (str, bytes)):
        if isinstance(ele, str):
            seq1 = [i.encode() for i in seq1]
            seq2 = [i.encode() for i in seq2]
        if detail:
            return ed.levenshtein_edit_distance_detail_bytes(seq1, seq2)
        else:
            return ed.levenshtein_edit_distance_bytes(seq1, seq2)
    else:
        raise ValueError(
            'Not supported type: {}'.format(type(ele)))


def levenshtein_alignment(seq1, seq2, eps_symbol):
    """

    Args:
        seq1 (List[T]):
        seq1 (List[T]):
        eps_symbol (T):
    Returns:
        total (int):
        aligned1 (List[T]):
        aligned2 (List[T]):
    """
    seq1 = tuple(seq1)
    seq2 = tuple(seq2)

    ele = _get_ele(seq1, seq2)
    if not isinstance(eps_symbol, type(ele)):
        raise TypeError('eps_symbol must have {} type'.format(type(ele)))

    if isinstance(ele, int):
        total, output = ed.levenshtein_alignment_long(seq1, seq2, eps_symbol)
    elif isinstance(ele, float):
        total, output = ed.levenshtein_alignment_double(seq1, seq2, eps_symbol)
    elif isinstance(ele, (str, bytes)):
        if isinstance(ele, str):
            seq1 = [i.encode() for i in seq1]
            seq2 = [i.encode() for i in seq2]
            eps_symbol = eps_symbol.encode()
        total, output = ed.levenshtein_alignment_bytes(seq1, seq2, eps_symbol)
    else:
        raise ValueError(
            'Not supported type: {}'.format(type(ele)))
    rseq1 = [v1 for v1, v2 in output]
    rseq2 = [v2 for v1, v2 in output]
    if isinstance(ele, str):
        rseq1 = [i.decode() for i in rseq1]
        rseq2 = [i.decode() for i in rseq2]
    return total, rseq1, rseq2
